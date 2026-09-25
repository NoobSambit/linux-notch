# Portability and Droppy-to-Linux feasibility

V1 is **Wayland + Hyprland only**. Distro packaging and compositor support are separate tasks. Quickshell's [PanelWindow](https://quickshell.org/docs/types/Quickshell/PanelWindow) provides an API for anchored surfaces, but the Hyprland implementation relies on the **[`zwlr_layer_shell_v1` protocol extension](https://wayland.app/protocols/wlr-layer-shell-unstable-v1)**. Layer shell is not core Wayland and this does not imply GNOME/KDE support. [Hyprland IPC](https://wiki.hypr.land/0.54.0/IPC/) exposes monitors/windows; [Quickshell.Hyprland](https://quickshell.org/docs/v0.2.0/types/Quickshell.Hyprland/Hyprland/) supplies reactive state. These are appropriate for the first backend, not for generic Shelf or Activity Policy logic.

## Dependency classes

- **CORE WAYLAND:** `wl_data_device` clipboard selection and drag/drop, data offers, copy/move action negotiation and input tied to a focused surface. The [core protocol](https://wayland.freedesktop.org/docs/html/apa.html) does not provide passive global drag observation or an unfocused clipboard-history feed.
- **WAYLAND PROTOCOL EXTENSION:** [`ext-data-control-v1`](https://wayland.app/protocols/ext-data-control-v1) for privileged clipboard managers, [`ext-session-lock-v1`](https://wayland.app/protocols/ext-session-lock-v1) for session locks, and [`ext-image-copy-capture-v1`](https://wayland.app/protocols/ext-image-copy-capture-v1) or foreign-toplevel extensions where supported. Published in wayland-protocols does not mean every compositor or tool implements them.
- **WLROOTS/COMPOSITOR EXTENSION:** [`zwlr_layer_shell_v1`](https://wayland.app/protocols/wlr-layer-shell-unstable-v1) for panels, anchors/focus/exclusive zones; `wlr-screencopy` and `wlr-foreign-toplevel` where used. These are **not** core Wayland and cannot be assumed on GNOME/KDE.
- **XDG DESKTOP PORTAL:** [Screenshot](https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.Screenshot.html) and [ScreenCast](https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.ScreenCast.html) are D-Bus mediated APIs with desktop-specific backends. They are separate from layer shell and do not supply an always-on global clipboard history or notification mirror.
- **FREEDESKTOP / DBUS API:** [notifications](https://specifications.freedesktop.org/notification/latest-single/) (one session owner), [MPRIS](https://specifications.freedesktop.org/mpris/latest/), desktop entries, NetworkManager, BlueZ and UPower interfaces.
- **LINUX SERVICE / FILESYSTEM:** PipeWire/WirePlumber audio/streams, local files, XDG file helpers, ffmpeg/Ghostscript/OCR/ASR tools; not inherently compositor protocols.
- **HYPRLAND-SPECIFIC:** `hyprctl`, Hyprland event socket/Quickshell integration, workspace/fullscreen/window identity, dispatch and Lua configuration.
- **DESKTOP-ENVIRONMENT-SPECIFIC:** EDS/Akonadi calendars, desktop settings, app-specific meeting control and portal backend availability.
- **DEVICE/DRIVER-SPECIFIC:** backlight, camera and hardware metrics; verify device support before promising a HUD.
- **NO RELIABLE PORTABLE API:** passive global drag-start, universal camera-in-use status and exact Apple-only integration/lock-screen behavior.

## Feasibility of desirable Droppy-exclusive workflows

| Workflow | Dependency class and actual path | V1 decision / unresolved point |
| --- | --- | --- |
| File Shelf, drag in/out | **CORE WAYLAND** `wl_data_device` offers (`text/uri-list` is a MIME convention) to QML `DropArea`; Qt drag source for drag-out. Layer-shell target itself needs **WLROOTS/COMPOSITOR EXTENSION** on Hyprland. [Core DnD protocol](https://wayland.freedesktop.org/docs/html/apa.html). | **Early isolated v1 spike**, before design/geometry/activity work. Test files/folders/multiple items, action negotiation, cancel, missing source, keyboard route and monitor behavior; return failures for scope review. |
| Notification ownership | **FREEDESKTOP / DBUS API** [Desktop Notifications](https://specifications.freedesktop.org/notification/latest-single/) has one `org.freedesktop.Notifications` session owner; not a Wayland layer-shell feed. | V1 Own for full toast/history/actions, External/off to coexist without mirroring; see [D20](DECISIONS.md#d20-detail--notification-ownership). |
| Floating Basket during any app drag | **NO RELIABLE PORTABLE API:** core Wayland delivers DnD events to target surfaces, not a passive global drag-start feed. A full-screen catcher may interfere with drops. | Later separate spike; no assumed compositor hook. |
| Multi-basket/pointer following | **NO RELIABLE PORTABLE API** for passive drag tracking; any compositor-specific path would need proof. | Later, contingent on Basket spike. |
| Rich clipboard and source app | **WAYLAND PROTOCOL EXTENSION / WLROOTS-COMPOSITOR EXTENSION** data control for an unfocused manager; [ext-data-control](https://wayland.app/protocols/ext-data-control-v1) is one protocol, with compositor/tool support to verify. [Portal Clipboard](https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.Clipboard.html) is session-bound, not universal always-on history. | V1 polish on current `wl-paste --watch` path; test file-reference offers separately. Source-app attribution later unless reliable. |
| Concealed clipboard exclusion | Clipboard MIME/app conventions over supported data-control path; **NO RELIABLE PORTABLE API** for universal password labeling. | Test common managers; never claim perfect exclusion. |
| OCR of capture/image/PDF | **LINUX SERVICE / FILESYSTEM** OCR/PDF tool plus current Hyprland/wlroots capture or **XDG DESKTOP PORTAL** Screenshot where implemented. | Later; workflow/model scope. |
| Voice transcription/dictation | **LINUX SERVICE / FILESYSTEM** PipeWire + local model; desktop text injection is compositor/desktop-specific. | Later; current video transcription is not dictation. |
| General conversion/PDF/target-size compression | **LINUX SERVICE / FILESYSTEM** ffmpeg/ImageMagick/Ghostscript. | Later; existing editor stays. |
| Small Shelf file actions / quick tiles / sharing | **LINUX SERVICE / FILESYSTEM** XDG/open/reveal/copy-path; sharing adds installed provider/network/consent. | V1 small actions; conversion/sharing later. |
| Calendar/reminders | **DESKTOP-ENVIRONMENT-SPECIFIC** EDS/Akonadi or network CalDAV. | Later. |
| Pomodoro/notes | Local clock/filesystem. | Later or existing plugin. |
| Meetings mute/camera/share | App-specific controls; PipeWire stream state is not universal meeting control. | Later per-app only. |
| Termi-Notch | Linux PTY; optional k4term-dependent current plugin. | Supported inherited. |
| Agent progress HUD | Local logs and optional account-usage network endpoint. | Supported inherited; new HUD later. |
| Window snapping and per-display move | **HYPRLAND-SPECIFIC** dispatch/IPC now; optional foreign-toplevel **WAYLAND PROTOCOL EXTENSION** does not guarantee control/thumbnails. | Supported inherited window tools; new snap shortcuts later. |
| Media queue/lyrics/AirPlay | **FREEDESKTOP / DBUS API** MPRIS transport/optional TrackList; lyrics and AirPlay vary by player/ecosystem. | Queue/lyrics later; core MPRIS media. |
| Media visualizer/per-app volume | **LINUX SERVICE** PipeWire/WirePlumber. | Core audio polish; measure visualization. |
| Battery, external drives, VPN | **FREEDESKTOP / DBUS API** UPower/UDisks2/NetworkManager where available. | Battery core status; richer drive/VPN activity later. |
| Mic/camera/screen privacy status | PipeWire and **XDG DESKTOP PORTAL** expose some sessions; **DEVICE/DRIVER-SPECIFIC** V4L2 paths prevent universal coverage. | No universal indicator claim; later. |
| Physical notch masking, Apple lock screen, Mission Control, Finder/iMessage/Apple Clock | **NO RELIABLE PORTABLE API** for exact Mac workflows. | Reject exact parity. |

## Architecture rule for future compositor support

Keep `HyprlandBackend` focused on what the source actually needs: monitors, focused workspace/fullscreen, top-level list/activation, window preview capability and compositor configuration. Let general services talk to Linux APIs directly. Feature code asks for capabilities rather than assuming every compositor can export a thumbnail or set a reserved zone. Read-only `CompositorBackend` contract tests can later run against recorded Hyprland payloads; a future backend requires its own proof. Do not add stub Niri/KDE/GNOME implementations.

Current host code accepts left/right, but public API prose and `Toast/BandaToast.qml` have top/bottom assumptions; side placement is **experimental/compatibility-only** for v1. That is a product validation boundary, not evidence that another compositor would support the same geometry or layer protocol.

For distro portability, maintain a **logical dependency list** separate from package names, explain manual installation, and keep `dependencias.tsv` as the current Arch map until a packaging task is approved. No v1 effort goes into distro-by-distro installers. See [DEPENDENCIES.md](DEPENDENCIES.md).
