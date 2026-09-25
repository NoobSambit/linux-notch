# Proposed architecture — after source audit, no code changed

This proposal extends the existing k4 structure. `shell.qml` already owns arbitration; `PluginManager` already owns instances; `Island` already publishes geometry; `Dual` already implements a dock. Introducing duplicate hosts, plugin registries, or state stores would make migration riskier. See [source audit](RESEARCH_K4.md).

```mermaid
flowchart TD
  Input[IPC / shortcuts / pointer / drag] --> Host[Surface host: shell.qml + Island]
  Settings[Validated settings + per-plugin Guardado] --> Host
  Plugins[PluginManager + K4.Plugin compatibility] --> Activity[Host activity policy]
  Services[MPRIS / PipeWire / NM / BlueZ / notifications / clipboard / capture] --> Activity
  Activity --> Host
  Host --> Screens[Per-screen Quickshell windows]
  Host --> Dock[Existing Dual/Muelle dock]
  Host --> Shelf[New local Shelf module]
  Backend[HyprlandBackend seam: windows/workspaces/focus/fullscreen/monitors] --> Host
  Backend --> Dock
  Backend --> Services
```

## Layers and ownership

- **UI layer:** existing `core/`, `widgets/`, and plugin `*View.qml` remain presentation components. Shared typography/motion/spacing tokens should live in an evolved `core/Theme.qml` or public theme adapter. Settings remains a separate window; capture/editor/fullscreen tools retain their own surfaces when focus or geometry requires them.
- **Surface system:** one host model determines `mode`, screen, edge, compact geometry, expansion geometry, exclusive zone, visibility and focus. Initially implemented within/refactored from `shell.qml`, `services/Island.qml`, `services/Settings.qml` and `plugins/Dual`. A new `SurfaceController` module is justified only when code extraction reduces the present cross-file state coupling and tests can cover its rules. Do not add a window manager framework for geometry that Quickshell already supplies.
- **System services:** keep `services/Media`, `Audio`, `Wifi`, `Bt`, `Notifs`, `Clipboard`, `Captura`, `Archivos`, `Fondos`, etc. Event-driven Quickshell services stay in use. Helpers stay where subprocesses have a real benefit (clipboard watcher, ffmpeg, file search); a large new daemon is not required.
- **Plugins:** `services/PluginManager.qml` remains catalog/lifecycle owner. `api/K4/Plugin.qml`, `K4.Puente`, `K4.Ipc`, `K4.Ajustes`, `K4.Guardado` and existing manifest keys remain a compatibility contract. New optional contribution roles can be additive after compatibility tests: `compactActivity`, `expandedActivity`, `dockItem`, `backgroundProvider`, `actions`, `settingsPage`. Do not make old `view` plugins invalid; map them to the primary expanded slot. The current manifest permission list is disclosure and static checking, not a sandbox. Show that honestly at enable/install time.
- **IPC:** retain `k4` compatibility verbs in `shell.qml` and plugin targets such as `k4.launcher`. New mode/Shelf commands can be additive. IPC response/error behavior should be specified and tested rather than silently ignoring missing plugins. Any eventual product-name change can add aliases after a migration window.
- **Persistence:** retain existing state paths and plugin files for compatibility. Add versioned/validated surface settings with migration from `posicionBarra`, `alineacionBarra`, `reservaIsla` and `Dual` saved settings; keep backup/last-good behavior where PluginManager already has it. Shelf stores local references/metadata with atomic writes and retention rules, not duplicated original files by default. Respect XDG paths where feasible, with a documented migration.

## Activity policy: extend existing arbitration

Current basis: `shell.qml:34-109` picks highest `active`/`priority`, closes transients when a user view wins, and publishes occupant/open to `Island`; `api/K4/Plugin.qml` provides `transitorio`, focus and hover rules. The proposed **Activity Router** is a named policy inside that host, not a second competing service.

| Field | Proposed meaning |
| --- | --- |
| `id`, `source`, `screenHint` | Stable activity identity, producer and requested display. |
| `kind` | `background`, `persistent`, `transient`, or `userSession`. |
| `priorityBand` | Policy bands: emergency/critical, explicit user session, privacy/recording, transient HUD/notification, persistent media, idle. Numeric legacy plugin priority maps into a band/order; exact mapping is tested, not guessed. |
| `createdAt`, `expiresAt`, `dismissed` | Lifetime and deterministic expiry; a transient can expire while hidden rather than reappear stale. |
| `compact`, `expanded`, `actions` | Optional contribution data/view factories; old plugin `view` fills expanded and current pill indicators remain compatible. |
| `interruptible`, `restorable` | Whether another activity may temporarily take the primary seat, and whether prior state returns. |

The host holds an ordered set of eligible activities per active screen and selects **one primary expanded view**. Compact persistent badges may coexist if their provider supports it; recording/privacy must remain accessible even while another primary view is open. Brief volume and notification activity may replace media, expire, then media resumes if still playing. An explicit launcher/file/settings session outranks automatic transients. A critical battery alert can preempt only under a documented critical rule, with an accessible dismissal path. Events arriving behind a user session are coalesced or logged in notification history; avoid a backlog of stale popups. “Queue” is a bounded pending event list, not a queue of every media tick. Existing plugin booleans remain the source of truth for their lifecycle until an adapter is proven; no parallel `active` flag is introduced. User customization in v1: enable/disable activity categories, brief duration, preferred monitor and reduced motion; arbitrary numeric priority editing is later.

Restore on state changes, not fixed timeout guesses: if volume expires, recompute from current media/recording/plugin state. When monitor disappears, rehome to a surviving screen, clear stale geometry, and return focus. Separate **activity selection** from **surface mode**: the same event can show in Notch/Island/Hybrid, while Dock mode uses a small status affordance and keeps the dock's task role.

## Hyprland backend seam

Do **not** wrap all Qt or Quickshell objects. A narrow `CompositorBackend` is justified because source imports and commands already spread across `Workspaces`, `Ventanas`, `Notifs`, `Captura`, `Dual`, `Atalaya`, `Pantallas` and `HyprTheme`. Its first implementation is `HyprlandBackend`, potentially as QML services plus existing helper commands. Contract candidates: monitor identities/geometry/scale, focused monitor, fullscreen/workspace state, toplevel enumeration and app identity, focus/activate/close, window thumbnails capability, reserved-space/layer capability and compositor configuration actions. Return capability flags and explicit errors. Theme/monitor configuration remains Hyprland-only feature modules; do not force generic methods for them. The Quickshell `PanelWindow` layer-shell surface itself stays in the surface layer unless a future compositor proves it needs a different adapter.

Do not introduce `DesktopBackend`, `WindowManagerBackend` and `CompositorBackend` simultaneously. One `CompositorBackend` around the concrete repeated seams is enough. Keep MPRIS, PipeWire, NetworkManager, BlueZ and local files outside it. No Niri/KDE/GNOME backend is included in v1.

## Tests at architectural seams

Pure policy tests for activity selection/expiry/restoration and settings migration; fixture-driven parsers for Hyprland monitor/client payloads; IPC command response tests; plugin lifecycle/compatibility test using `ejemplos/hola` and a failing sample; Shelf file-URI and missing-file semantics; one/two-monitor Hyprland integration scripts; rendered visual/accessibility checks. The existing Python validators remain gates. Avoid trying to unit-test pixel-perfect QML animation; use rendered screenshots/video plus frame/resource traces for those claims.
