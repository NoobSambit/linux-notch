# Portability and Droppy-to-Linux feasibility

V1 is **Wayland + Hyprland only**. Distro packaging and compositor support are separate tasks. Quickshell's [PanelWindow](https://quickshell.org/docs/types/Quickshell/PanelWindow) supports edge anchors and exclusive zones; its [WlrLayershell](https://quickshell.org/docs/v0.2.0/types/Quickshell.Wayland/WlrLayershell/) access is protocol-specific. [Hyprland IPC](https://wiki.hypr.land/0.54.0/IPC/) exposes monitor/window events; [Quickshell.Hyprland](https://quickshell.org/docs/v0.2.0/types/Quickshell.Hyprland/Hyprland/) supplies a reactive view. These are appropriate for the first backend, but must not leak into a new generic Shelf or activity policy.

## Dependency classes

- **COMMON LINUX API:** MPRIS, PipeWire/WirePlumber, NetworkManager, BlueZ, UPower, freedesktop notifications/desktop entries, local filesystem, ffmpeg, Ghostscript, OCR/ASR engines.
- **WAYLAND STANDARD/PORTAL:** layer shell (supported by the target compositor), Wayland drag and drop and data offers, data-control protocol, xdg-desktop-portal screenshot/screencast, session lock.
- **HYPRLAND-SPECIFIC:** `hyprctl`, event socket, workspace/fullscreen/window identity, Hyprland toplevel export/thumbnail and Lua configuration.
- **COMPOSITOR-SPECIFIC:** protocol support and behavior for global pointer/drag observation, top-level activation, capture, layer focus and exclusive zones; may differ later.
- **DESKTOP-ENVIRONMENT-SPECIFIC:** calendars via Evolution Data Server/Akonadi, GNOME/KDE settings, app-specific meeting control.
- **DIFFICULT/NO CLEAN LINUX EQUIVALENT:** passive global drag detection under Wayland, universal camera-use status, Apple-only services and exact Mac lock-screen behavior.

## Feasibility of desirable Droppy-exclusive workflows

| Workflow | Dependency class and actual path | V1 decision / unresolved point |
| --- | --- | --- |
| File Shelf, drag in/out | WAYLAND STANDARD/PORTAL: `wl_data_device` DnD offers (`text/uri-list`) to a QML `DropArea`; drag-out via Qt drag source. [Protocol](https://wayland.app/protocols/wayland). | V1, test file managers and targets. URI offers and copy/move negotiation vary by source; do not promise all payload types. |
| Floating Basket during any app drag | DIFFICULT/NO CLEAN LINUX EQUIVALENT: Wayland delivers DnD enter/motion to target surfaces, not a passive global drag-start feed. [Wayland DnD](https://wayland.app/protocols/wayland). A full-screen invisible catcher may interfere with normal drops. | Later feasibility spike. An explicit shortcut while dragging or Hyprland integration may be viable, but is not verified. |
| Multi-basket/pointer following | COMPOSITOR-SPECIFIC pointer/drag state and focus rules, then COMMON local storage. | Later, contingent on Basket spike. |
| Rich clipboard and source app | WAYLAND STANDARD/PORTAL data control; [ext-data-control-v1](https://wayland.app/protocols/ext-data-control-v1) supports clipboard managers. The [portal Clipboard API](https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.Clipboard.html) is session-bound, not an always-on universal history feed. | V1 improves existing local history; source-app attribution may need compositor-specific metadata and is later unless reliable. |
| Concealed clipboard exclusion | WAYLAND STANDARD/PORTAL MIME hints plus app conventions; no universal password flag established. | V1 test common password managers; never claim perfect exclusion. |
| OCR of capture/image/PDF | COMMON LINUX API local OCR/PDF rasterizer plus WAYLAND STANDARD/PORTAL screenshot or current grim/slurp path. [Screenshot portal](https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.Screenshot.html). | Later; fully feasible but models/languages and workflow add scope. |
| Voice transcription/dictation | COMMON LINUX API PipeWire recording + local whisper.cpp/Vosk-like runtime; desktop text injection is COMPOSITOR-SPECIFIC. | Later; k4's video transcription does not establish global dictation. |
| General conversion/PDF/target-size compression | COMMON LINUX API ffmpeg/ImageMagick/Ghostscript. | Later as file actions; k4's existing editor stays. |
| Quick tiles/local sharing | COMMON LINUX API local file command/LocalSend where installed; cloud requires explicit provider/network/consent. | Later. Reject AirDrop/iCloud parity claim. |
| Calendar/reminders | DESKTOP-ENVIRONMENT-SPECIFIC EDS/Akonadi or CalDAV; no single universal desktop calendar store. | Later. |
| Pomodoro/notes | COMMON LINUX API local clock/storage. | Later or third-party plugin; low technical risk, scope cost. |
| Meetings mute/camera/share | DESKTOP-ENVIRONMENT-SPECIFIC/app-specific; PipeWire can see streams but cannot universally toggle arbitrary meeting apps. | Later per-app integration only. |
| Termi-Notch | COMMON LINUX API PTY; k4 already has optional k4term-dependent terminal. | Preserve current integration. |
| Agent progress HUD | COMMON LINUX API local agent logs where available; optional network for usage limits. | Preserve k4 agent features with disclosure; new HUD later. |
| Window snapping and per-display move | HYPRLAND-SPECIFIC dispatch/IPC in v1; eventual `CompositorBackend`. | Existing k4 window/workspace tools preserved; Droppy-like snap shortcuts later. |
| Media queue/lyrics/AirPlay | COMMON LINUX API [MPRIS](https://specifications.freedesktop.org/mpris/latest/interfaces.html) for transport/optional TrackList; lyrics provider or player integration varies. AirPlay is Apple ecosystem, no direct equivalent. | Later. Keep k4 MPRIS media. |
| Media visualizer/per-app volume | COMMON LINUX API PipeWire/WirePlumber streams. | Existing k4 capability; measure/polish v1. |
| Battery, external drives, VPN | COMMON LINUX API UPower/UDisks2/NetworkManager, where available. | Battery existing; richer activity later. |
| Mic/camera/screen privacy status | COMMON LINUX API PipeWire can observe some stream/capture state; portal sessions offer consent for app-initiated capture; universal camera status is DIFFICULT across V4L2, portals and apps. | Do not show an untrustworthy universal indicator. Later after coverage proof. |
| Physical notch masking, Apple lock screen, Mission Control, Finder/iMessage/Apple Clock | DIFFICULT/NO CLEAN LINUX EQUIVALENT as exact workflows. | Reject exact parity. Linux-native alternatives would be separate proposals. |

## Architecture rule for future compositor support

Keep `HyprlandBackend` focused on what the source actually needs: monitors, focused workspace/fullscreen, top-level list/activation, window preview capability and compositor configuration. Let general services talk to Linux APIs directly. Feature code asks for capabilities rather than assuming every compositor can export a thumbnail or set a reserved zone. Read-only `CompositorBackend` contract tests can later run against recorded Hyprland payloads; a future backend requires its own proof. Do not add stub Niri/KDE/GNOME implementations.

For distro portability, maintain a **logical dependency list** separate from package names, explain manual installation, and keep `dependencias.tsv` as the current Arch map until a packaging task is approved. No v1 effort goes into distro-by-distro installers. See [DEPENDENCIES.md](DEPENDENCIES.md).
