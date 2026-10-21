# CP-00 environment isolation proof (engineering exploration)

Preparation commit: 2c0b4ca. Runtime tools in this run are bound by tools.patch. No k4 launch yet.
Two independent bubblewrap 0.13.0 sandboxes share only the ignored synthetic lab home/runtime.
The compositor uses Hyprland 0.56.2/Aquamarine 0.15.1 with a minimal Lua configuration and no
exec/autostart/keybindings. It creates a normal nested window; no host configuration is changed.
Actual nested output is WAYLAND-1, 951x1028, scale 1, 60 Hz (host tiling determines window size).
Requested 1280x720 is not claimed as the observed resolution. No physical dual-output proof exists.

## Boundary observations before any k4 launch

`python3 tools/cp00.py exec -- python3 /lab/probe.py` runs the exact public tools/cp00_probe.py.
The final output is isolation-probe.json; host-comparison.json compares live namespace/bus identities.
Every mount/PID/network/IPC/user namespace differs from the host. The app sees five sandbox processes,
a synthetic HOME, private /tmp session bus and private runtime only. Its network has only loopback.
Both source aliases /original and /lab/original reject writes. Dummy state writes appear under
scratch/cp00/lab/home/.local/state/k4, while the host's personal k4 path remains absent.

Host HOME, parent display socket, /run/user/1000, system bus, audio/input/camera/DRM-card devices are
absent. The parent display socket exists only in the compositor sandbox; app /proc cannot expose that
separate process namespace. The app has no host compositor signature. Read-only /sys exposes hardware
metadata, not device-changing access. RenderD128/129 are shared rendering capability, not DRM modeset
nodes. /usr, font configuration and loader cache are read-only system dependencies. No credentials,
personal clipboard/history or saved personal settings are mounted or copied.

pactl info, wpctl status and system-bus listing fail inside the app sandbox as expected; separate JSON
files retain exact commands/results. A private session bus has no service activation directories,
portal, notification owner or host agent. The initial default dbus-run-session config listed installed
activatable names; the first probe refused it. The final bus config deliberately excludes activation.
The initial failure is retained in isolation-probe-initial-failure.json.

`grim /lab/isolated-empty.png` captures the nested empty output successfully. The agent opened that
951x1028 image and observed only the synthetic dark background; it is a compositor plumbing check,
not a k4 application capture. `private-clipboard.json` records harmless wl-copy/wl-paste roundtrip
through only the nested Wayland socket. Host clipboard contents were never requested.

Host unrelated Quickshell still lists xzn1r8nt/PID 1293/end4-pC and notification owner :1.14, matching
run-01. No global kill, installer, package install, session-service restart or personal restore occurred.

## Source basis for the compositor boundary

Version-matched primary source:
- https://raw.githubusercontent.com/hyprwm/Hyprland/v0.56.2/src/Compositor.cpp (backend setup and private runtime/signature).
- https://raw.githubusercontent.com/hyprwm/aquamarine/v0.15.1/src/backend/Wayland.cpp (registry binding, lines 106–133).
- https://raw.githubusercontent.com/hyprwm/aquamarine/v0.15.1/docs/env.md (installed backend environment inventory).

Aquamarine's parent connection binds seat, compositor, shell, shared memory and dmabuf interfaces;
that version's registry code does not bind clipboard/data-control interfaces. This supports the
inference that the nested compositor does not forward the host selection. More decisively the k4
sandbox cannot connect to the parent socket at all. Source review complements actual endpoint probes;
it does not certify a general-purpose adversarial sandbox or all future third-party plugins.

## Tooling failures found and corrected before k4

- Initial bwrap true probe omitted the /lib64 loader link; corrected probe succeeds.
- Explicit --unshare-user is required with --disable-userns on this installed release.
- Read-only /etc mounts require precreated font/cache mount points; those are now synthetic fixtures.
- Signalling bwrap's outer wrapper can leave its namespace child running. The tool now identifies and
  pins the actual payload PID/start-time/exe/argv/namespace plus lab inode, using pidfd for termination.
  The two known task payloads were verified and stopped, then recreated. No unrelated process was signalled.

T02 recovery/full-ID checks, backup/restore and a clean pinned k4 launch still remain. This document
provides no owner Start/Stop/Restore promise and cannot make all of R01 PASS.

Clipboard runner lesson: daemonized wl-copy retains captured pipes, so a combined shell roundtrip
waited for pipe EOF despite wl-paste succeeding. Its exact dummy wl-copy PID was verified inside
the app namespace and stopped with pidfd; the command completed. Future fixtures must launch
long-lived producers through the background/log interface and read clipboard in a separate command.
