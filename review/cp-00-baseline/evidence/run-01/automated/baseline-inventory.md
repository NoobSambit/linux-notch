# Source and workstation baseline

Synchronized main: 6478e25c52adbbbe3e2f00e2c5cf975b09e6732b (merged PR #1). Clean starting tree.
Recovery product source: ff520e3, expanded to the full SHA in inventory.json/progress.json.
Pinned detached worktree: scratch/cp00/original. Product tree is unchanged from that baseline;
workflow files are the only differences on merged main. No upstream update is imported.

Observed: Arch, kernel 7.2.8-arch1-2, Intel i7-13700HX, Intel UHD 770 plus NVIDIA RTX 4050 Mobile;
Qt 6.11.2; Quickshell 0.2.1 revision 7511545ee20664e3b8b8d3322c0ffe7567c56f7a;
Hyprland 0.56.2; bubblewrap 0.13.0. One physical eDP-1 1920x1080 at scale 1 / 165 Hz.
See inventory.json for exact observed commands, package versions and dependency checks.

The running unrelated Quickshell config is end4-pC, full ID xzn1r8nt, PID 1293; the notification
owner is :1.14. These are observation-time identities, never permission to signal them. Recheck live.
Personal k4 state/config/cache/share paths are absent; personal Quickshell config exists. No contents
of private settings, clipboard, credentials or personal screenshots were read or copied.

Missing declared dependencies: Meslo Nerd Font package, swaybg; optional whisper-cli. No packages
installed. Existing fonts/rendering still require actual observation. A package-name query is not a
proof of a binary's availability: pacman resolves quickshell-git through an installed provider while
the executable reports its own version. Record both rather than treating the package label as ABI proof.

## Isolation hazards from actual source

- api/K4/Paths.qml and services/{Settings,PluginManager,Weather,Game,Tokens,Ambiente,Digivice}.qml
  construct HOME/.local/state/k4; PluginManager discovers HOME/.config/k4/plugins and caches catalog/
  enabled state plus backup. tools/portapapeles.py has a HOME-based text/image store.
- tools/agentes.py and vigia-tokens.py can inspect Codex/Claude session/credential paths. huella.py
  can inspect Steam/packages. A fake XDG_STATE_HOME alone leaves these personal paths reachable.
- shell.qml eagerly initializes Notifs, Clipboard, Audio, Wifi, Bt, Workspaces, Weather and others.
  Notifs.qml unconditionally instantiates NotificationServer. Clipboard.qml launches two wl-paste
  watchers. Audio uses PipeWire/pactl; networking/Bluetooth use system services; weather can use curl.
- hyprctl is called for windows/monitors/focus/configuration. Inherited instance signature/runtime
  can address the live compositor. Capture/clipboard must see only nested Wayland.
- instalar is inspection-only: package/config/autostart changes and broad Quickshell restart paths
  make it unsuitable for test startup. arrancar sets imports and writes/rotates a state log.
- Manifest permission declarations are advisory; trusted inherited QML executes in-process.

source-path-audit.txt preserves source locations and snippets, not runtime proof. No application has
been launched at this preparation stage. A corrected bubblewrap true probe (with /lib64 loader link)
succeeds; the initial probe omitted that loader link and failed before executing true. This is not an
isolation or app-runtime PASS. Host services have only been queried read-only.

## Atalaya and rights preparation

plugins/catalog.json has enabledByDefault=true for atalaya. PluginManager.estaHabilitado gives an
explicit saved habilitados override precedence over that inherited catalog value. No personal k4 saved
file exists on this host; the test store has not been created or characterized yet. Do not infer
closed-state CPU/GPU or effective runtime enablement from this source observation.

Atalaya/Tarjeta.qml uses live thumbnails with a 600 ms settling interval and visibility checks;
Lienzo.qml includes open-dependent work. Actual open/closed costs remain required.
Existing docs/ASSET_LICENSE_AUDIT.md supplies the preliminary rights boundary; code MIT does not
clear Game/Digivice media, fonts or inherited screenshots. A file-level inventory will be collected
in T04 without downloading or publishing assets.
