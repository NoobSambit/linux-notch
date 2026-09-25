# k4 component migration map — proposal only

No product code is changed by this plan. Preserve first, characterize behavior second, then make the smallest targeted change. Classification refers to **future treatment**, not current quality certification. `REPLACE` and `REMOVE` have no current candidate: source research found no component whose replacement or deletion is justified. `UNCERTAIN` items need live or rights evidence before a stronger verdict. See [RESEARCH_K4.md](RESEARCH_K4.md).

| Component (actual files/modules) | Verdict | Reason and migration boundary |
| --- | --- | --- |
| `shell.qml` host/IPC/window creation | REFACTOR | Keep compatibility IPC and one host; extract testable surface/activity policy from large monolith only where needed for modes. |
| `services/Island.qml`, `core/SiluetaIsla.qml` | KEEP + POLISH | Geometry and per-screen publication already useful; add validated mode geometry and reduced motion without breaking K4.Isla. |
| `plugins/Dual/DualPlugin.qml`, `Muelle.qml`, `Escena.qml`, `Caida.qml`, `Gota.qml` | REFACTOR | Existing dock, hybrid, drag and transition are product assets. Isolate dock state from journey animation and Hyprland commands; retain opt-in expressive transition. |
| `services/PluginManager.qml`, `tools/plugins.py`, `plugins/catalog.json`, `plugins/registro.json` | KEEP + POLISH | Dynamic load, state backup, registry validation and reload are valuable. Add compatibility fixtures and honest security messages; avoid breaking manifests. |
| `api/K4/*`, `core/K4Plugin.qml`, `api/K4/Puente.qml` | KEEP | Public compatibility surface. Additive APIs only after old sample plugins pass. |
| `core/Theme.qml`, `core/Island*`, common `widgets/*` | REDESIGN | New visual grammar and motion tokens, but keep component semantics and accessibility. Avoid one wholesale QML rewrite. |
| `services/Settings.qml`, `plugins/Settings/*` | REDESIGN | Searchable separate window is good; make mode/geometry preview and privacy controls understandable, validate/migrate JSON. |
| `services/Media.qml`, `plugins/Player/*`, `widgets/Artwork.qml`, `Visualizer.qml` | KEEP + POLISH | MPRIS and playback exist; refine hierarchy, player choice and pause animation while hidden. |
| `services/Notifs.qml`, `plugins/Toast/*`, `widgets/NotifStrip.qml` | KEEP + POLISH | Notification actions/history and server exist; align activity interruption and focus. |
| `services/Clipboard.qml`, `tools/portapapeles.py`, `plugins/Clipboard/*` | KEEP + POLISH | Local history exists; improve search, copy feedback, secret tests and persistence limits. No format rewrite by default. |
| `services/Archivos.qml`, `plugins/Files/*`, `tools/buscar.py` | KEEP | File search is distinct from Shelf. Reuse file naming/icons cautiously; do not retrofit it into a tray. |
| New Shelf module and local staging store | NEW, not a replacement | Add file handoff workflow via standard DnD, safe copy default and local metadata. |
| `plugins/Launcher/*`, `plugins/Apps/*`, `services/Items.qml` | KEEP + POLISH | App launcher, app center and package search exist; make entry points coherent with dock drawer. |
| `services/Audio.qml`, `Wifi.qml`, `Bt.qml`, `Tray.qml`, `Indicadores.qml`, `Sistema.qml`; `plugins/Panel/*`, `Sonido`, `Volume`, `System`, `Tray` | KEEP + POLISH | Linux service plumbing is a key reason to fork k4. Keep reactive Quickshell integrations; profile fallback polling. |
| `services/Captura.qml`, `plugins/Captura/*`, `tools/captura.py` | KEEP + POLISH | Capture/recording pipelines are valuable; improve state visibility and Shelf handoff only after core Shelf works. |
| `services/Editor.qml`, `EditorProcesos.qml`, `tools/editar.py`, `tools/transcribir.py` | KEEP | Large video editor remains functional candidate; no v1 rewrite. Add regression tests only where refactor touches it. |
| `services/Fondos.qml`, `Ambiente.qml`, `plugins/HyprTheme/*`, `Pantallas/*` | KEEP + POLISH | Preserve wallpaper/desktop customization. Move repeated Hyprland operations behind a narrow backend where it pays off; Hyprland theme UI remains explicitly specific. |
| `services/Workspaces.qml`, `Ventanas.qml`, `Submapas.qml`, `plugins/Windows/*`, `Atalaya/*` | REFACTOR | Window/workspace/thumbnail behavior is backend-sensitive. Characterize features, then isolate query/activation seams. Atalaya GPU cost requires measurement. |
| `plugins/Session/*`, `services/Sesion.qml` | KEEP | Linux session lock is a distinct native workflow. Avoid Mac lock screen parity work. |
| `plugins/Terminal/*`, `Ssh/*`, `services/Consola.qml` | KEEP | Useful optional Linux tools; `k4term` requirement is documented. Test no-op state when missing. |
| `plugins/Ask/*`, `Agentes/*`, `services/Tokens.qml`, `tools/agentes.py` | KEEP + POLISH | Developer features differentiate k4; clarify credential/network access and let users disable watchers. |
| `plugins/Weather/*`, `services/Weather.qml` | KEEP + POLISH | Useful but IP-based auto-location is a privacy decision; expose opt-in/place setting. |
| `plugins/Game/*`, `Digivice/*`, `services/Game*`, `Digivice*`, `Logros.qml` | UNCERTAIN for new product spotlight; KEEP for compatibility | Optional game code should not consume v1 redesign budget. Audit bundled artwork/data rights and measured idle cost before packaging. No deletion proposed. |
| `plugins/Keys/*`, `Submap/*`, `Idle/*`, `Clock/*`, `Tienda/*` | KEEP + POLISH | Existing shortcuts, baseline pill, clock and plugin store are core supporting tools. |
| `instalar`, `arrancar`, `hypr/k4.conf`, `hypr/k4.lua`, `dependencias.tsv` | REFACTOR (later targeted) | Preserve Hyprland setup; prevent all-Quickshell process termination and clarify optional vs base dependencies. No broad distro installer work. |
| `traducciones/*`, `services/Idioma.qml` | KEEP + POLISH | Preserve localization; identify hardcoded strings in touched screens and verify fallbacks. |
| `.github/workflows/*`, `tools/prueba_*`, validators | KEEP + POLISH | Existing gates useful. Add pure state, config, backend parser, IPC and plugin compatibility tests before risky refactors. |

## Compatibility work before any plugin API change

Record current `K4.Plugin` properties/signals, all `api/K4` exports, manifest keys (`permisos`, `superficies`, `host`, `requiere`, `aplicacion`), lifecycle and IPC verbs. Test `ejemplos/hola`, `piezas`, `efectos`, `snake` and at least one installed external plugin if the user supplies one. `tools/plugins.py` static checks do not sandbox runtime code. A new activity or dock contribution is optional and additive; old `view` remains renderable. Disabled means uninstantiated; hot reload and failure diagnostics remain. Any unavoidable break requires versioned manifest/API migration and a documented fallback before implementation.
