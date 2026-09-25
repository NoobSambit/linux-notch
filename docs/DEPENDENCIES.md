# Dependency inventory and packaging boundary

Source: [`dependencias.tsv`](../dependencias.tsv), [`instalar`](../instalar), QML imports and helper calls. This is an inventory, **not** a request to change packages. Package availability can drift; recheck at implementation. Current `dependencias.tsv` treats many feature dependencies as `base` because it describes the whole k4 installation, not the smallest new surface.

| Group | Current dependencies | Role / portability issue |
| --- | --- | --- |
| Core shell | Quickshell, Qt 6 Declarative/Wayland, Hyprland, Python, git | Quickshell/Qt are stack lock; Hyprland target is v1 compositor. `qt6-multimedia` and FFmpeg backend are base for editor playback. |
| Visual assets | Meslo Nerd Font, Adwaita fonts, QML shaders/images | Icons rely on Nerd glyphs; check fonts and asset redistribution rights before new branding. |
| Capture/record/editor | grim, slurp, satty, wf-recorder, ffmpeg/ffprobe, ImageMagick, zenity; optional gpu-screen-recorder, whisper-cpp | Multiple external processes and codec/GPU variation. `gpu-screen-recorder` is detected in source, with wf-recorder fallback. Portal capture may help later but is not currently used as the main path. |
| Desktop utilities | wl-clipboard (`wl-copy`, `wl-paste`), fd, pactl/libpulse, WirePlumber (`wpctl`), NetworkManager (`nmcli`), BlueZ, libnotify, xdg-utils, xdg-user-dirs, desktop-file-utils | Quickshell also exposes reactive PipeWire/Networking/Bluetooth/MPRIS/notifications. CLI and reactive paths coexist; do not blindly remove one. |
| Wallpaper and network | swaybg, curl, Open-Meteo, ipwho.is, optional Anthropic usage endpoint | Weather/IP lookup and agent usage are network features, not telemetry; they need user-facing transparency/consent. |
| Optional tools | kitty, uwsm, yay, nvidia-smi, Claude/Codex CLIs, k4term, whisper-cli | Feature-specific requirements. App should show unavailable states instead of making them core unless necessary. |
| New Shelf | Qt/Wayland DnD and local storage; no mandatory new system package proposed | Confirm Quickshell/QML accepts `text/uri-list` from tested apps and can drag out. Basket would require a separate feasibility spike. |

`instalar` maps Arch package names to some apt/dnf/zypper names for diagnosis but automatically installs only through pacman. It writes Hyprland config and may restart Quickshell processes globally; this deserves targeted safety work before recommending it to users with other Quickshell configurations. The v1 scope is a documented Hyprland manual path and dependency check, not installers for every distribution. A future packaging layer can translate logical capabilities into distro packages independently of the `CompositorBackend`.

The host imports `Quickshell.Hyprland` only in specific services/plugins, while MPRIS, PipeWire, Networking and Bluetooth are general Linux paths. This is the natural separation between compositor portability and distro packaging. The [Quickshell PanelWindow documentation](https://quickshell.org/docs/types/Quickshell/PanelWindow) and [portal ScreenCast interface](https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.ScreenCast.html) should be consulted when a new mode/capture path is implemented. No dependency replacement is justified by this research.
