# Isolated runtime, rollback and recovery contract

This is a procedure for future authorized checkpoints. **No runtime or launch/stop helper is created
by workflow setup.** CP-00 must prove the procedure on the available machine before offering a test.
If no safe environment is available, record NEEDS HELP; do not improvise on the live desktop.

## Isolation before first launch

Preferred: a dedicated test user/session or a disposable VM with Hyprland, separate HOME, session D-Bus,
settings/cache, clipboard, notification owner and dummy files. A nested Hyprland session is acceptable
only after confirming its separate Wayland socket, session D-Bus and HOME-dependent paths and avoiding
host device/service changes. A private D-Bus alone does not isolate audio/network/hardware. Inventory
each shared capability; use fixtures/disable device-changing actions until explicitly authorized.

Use a pinned checkout under `/scratch/` for test code. A different checkout, `-p`, XDG variables,
`K4_LOG=0` or a private process group alone **does not isolate** HOME-based k4 state, data-control
clipboard, D-Bus ownership, `hyprctl` commands or personal credentials. Never repurpose the shell's HOME
variable in ad hoc scripts. Prefer an actual test account with its own home; audit subprocess paths.
Do not copy personal clipboard histories, credentials or plugin executables into fixtures.

CP-00 records code SHA, runtime/Qt/Hyprland/GPU versions, monitor geometry/scale, current notification
owner (read-only), process inventory, state paths and approved shared capabilities. Prepare launch,
stop and restore commands for that **specific** environment. Prove on dummy state that test writes
cannot reach personal settings and notification ownership is confined to the test bus. Do not use
`instalar`; inherited behavior can already conflict before CP-01 fixes it.

## Instance identity and handoff

At each launch record full config path, full instance ID, PID, process start time, checkout SHA,
Wayland socket and bus identity. Inspect local `quickshell --help`, `quickshell kill --help` and
`quickshell ipc --help`; do not rely on flags from a different release. The inspected 0.2.1 CLI supports
`quickshell list --all --json`, `quickshell kill --id FULL_ID` and `quickshell ipc --id FULL_ID ...`.
These are agent examples, not commands the owner must construct.

Before stopping, verify that the recorded ID still maps to the same config/PID/start time/session.
Use the **full** instance ID, never newest/default/substring selection. If the ID is absent, the old
instance is already stopped; do not kill a replacement. If IPC fails, signal only the verified PID
and its verified test children, first TERM, then KILL only if required; verify identities again to
avoid PID reuse. Never `pkill quickshell`, `killall`, global daemon restarts or arbitrary process-group
termination. A frozen nested desktop can be stopped via its separately verified nested compositor PID;
the host Hyprland session must remain running.

Before owner handoff Codex supplies tested, copyable **Start CP-NN**, **Stop CP-NN**, **Restore previous**
actions and a visible terminal labelled with CP ID/run/SHA. These may be short scripts prepared in
CP-00 after approval; they must guard identity and must not modify autostart or install over the live app.
If the owner cannot use a terminal, provide equivalent launchers in the isolated environment. Never
publish placeholders as working commands. No test is ready until Start/Stop/Restore have been exercised.

## Backups and last-good version

- Preserve the previous accepted Git SHA and launchable checkout. Do not reset or overwrite the working tree.
  CP-00 has no preceding accepted checkpoint: use the original source baseline recorded in progress.json
  as its recovery target, with a separately captured matching disposable state snapshot.
- Before each checkpoint run, stop the intended test instance and snapshot its state with UTC date,
  source paths, SHA and checksums under ignored `scratch/backups/<checkpoint>/<run>/`. Include settings,
  enabled-plugin state, per-plugin state and Shelf/clipboard dummy stores; restrict permissions.
- Test backup restore against disposable files. Retain the current and previous accepted snapshots until
  the new checkpoint is approved and recovery has been proven. Keep required private backups outside Git.
- Rollback: verify/stop the candidate instance; retain failure logs and current state snapshot; start
  the previous accepted checkout with its matching **test** snapshot; recheck basic launcher/settings
  behavior. Do not feed a migrated/newer store into old code without a compatibility check.
- Personal state/config restoration always requires explicit approval of exact paths and backup date;
  compare newer personal data first. Never overwrite original files or silently discard later settings.

## Operations touching the real session

Real Hyprland keybindings/config reload, exclusive zones/fullscreen/focus, monitor modes/hotplug,
audio output/volume, Wi-Fi/Bluetooth, capture, clipboard watching and notification ownership may affect
the owner. Plan/test these in isolation first. Before unavoidable live validation explain the concrete
effect, identify rollback, and obtain explicit permission. Never stop swaync/mako/dunst or steal their
bus name. The owner may deliberately disable their daemon themselves for an approved Own-mode test;
record the prior state and let them restore it. Do not install dependencies or enable startup without
authorization. If a test device/display is unavailable, record the limitation honestly.

Owner's short version: [Recovery](../../owner/RECOVERY.md).
