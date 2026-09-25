# Ordered implementation plan — begins only after user approval

**Status: planning only.** This was written after the research, matrix, spec, architecture, migration, portability, dependency, UX and decision documents. No milestone below is authorized yet. Each is intended to be a small reviewable change with its own acceptance evidence. Preserve existing features and plugin compatibility unless a separately evidenced change is approved.

| Milestone | Goal and affected modules | Dependencies | Main risks | Validation / exit evidence |
| --- | --- | --- | --- | --- |
| 0. Baseline and rights inventory | Capture current top/bottom/dock/hybrid behavior, 1/2 monitors, fullscreen, capture/editor and plugin samples. Inventory non-code image/font/game asset provenance. No behavior change. | Approved spec, Hyprland test session | Snapshot lacks `.git` metadata and runtime evidence; asset rights unknown | Versioned baseline screenshots/video, hardware/Quickshell versions, resource readings, plugin fixtures and license inventory |
| 1. High-value regression harness | Add pure tests for settings migration, activity selection rules as characterized, plugin manifest/lifecycle, IPC and Hyprland JSON parsing; keep existing CI validators. `tools/prueba_*`, new small fixtures, `.github/workflows/validar.yml` if justified. | Baseline | Over-testing QML pixels or freezing accidental behavior | Existing CI gates + new state/parser fixtures pass; no UI rewrite |
| 2. Privacy and install safety | Make automatic weather IP lookup and agent network usage discoverable/controlled; scope Quickshell restart to k4. `services/Weather.qml`, `tools/agentes.py`/plugin settings, `instalar`. | Settings tests | Existing-user behavior change, installer side effects | Offline test, opt-in/out test, manual install rehearsal without killing unrelated Quickshell |
| 3. Surface settings and geometry | Versioned validated mode/edge/size/offset/reservation/monitor settings. `services/Settings.qml`, `Island.qml`, `shell.qml`, Settings preview. | Baseline, migration tests | Offscreen/focus/exclusive-zone bugs | Invalid-state recovery; 1/2 monitors, top/bottom, fractional scale, hotplug, fullscreen rendered proof |
| 4. Activity policy extension | Adapt existing highest-priority owner to explicit lifetime/restoration rules, legacy plugin mapping and compact persistent badges. `shell.qml`, `api/K4/Plugin.qml` additive only, `Notifs`, `Media`, `Audio`, `Captura`. | Milestone 1 and geometry | Two competing sources of truth, priority inversion, focus theft | Media→volume→media; notification during launcher; recording remains visible; old plugin fixture passes |
| 5. Dock and Hybrid coherence | Reuse `Dual/Muelle`; separate dock task state from travel animation, connect four named modes, shorten default transition and add reduced-motion path. `plugins/Dual/*`, host/Settings. | Milestones 3–4 | Window polling, incorrect focus/warps, multi-monitor transition | Pin/reorder/focus/multiple windows/drawer; reserve reflow; 1/2-monitor video; idle/dock resource traces |
| 6. Shelf DnD feasibility gate | Small throwaway experiment in a separate test fixture or branch: file URI drop in/out between Quickshell and target apps, no product integration. | Hyprland session | Wayland MIME/drag-source limitations | Matrix of file managers/targets, copy/move/cancel behavior and decision to proceed or rescope |
| 7. Local Shelf | Add Shelf UI/state/persistence and optional capture handoff only after feasibility passes. New module, settings, activity host, local store. | Milestones 3–4, 6 | Data loss, inaccessible drag-only flow, file metadata privacy | Original untouched, drag cancellation, missing source, keyboard path, restart retention, URI/path safety, no network traffic |
| 8. Distinct visual pass | Create references and original visual tokens; update shell, dock, settings, media/notification/launcher and Shelf progressively. `core/Theme.qml`, shared widgets and affected views. | Interaction stable | Copying another product, GPU-heavy blur, regressions | Desktop/mobile-size-equivalent viewport references, dark/light, keyboard/focus, contrast, reduced motion, screenshots/video, frame timings |
| 9. Plugin compatibility and docs | Exercise built-in and sample external plugins, update API docs for additive contribution roles, errors and migration; keep `PluginManager` behavior. | Milestones 4–8 | Hot reload/IPC QML cache, in-process security misconceptions | `tools/plugins.py`, `tools/api.py`, sample fixtures, reload/failure scenarios, user-facing permission disclosure |
| 10. V1 acceptance and release preparation | Full Hyprland scenario sweep; dependency/manual install guide; license notices/asset gate; confirm scope. | All prior milestones | Environmental gaps or unproven claims | Exact CI commands, live QA matrix, performance report, unresolved issues, release decision. No release if asset rights or core DnD remain unresolved. |

## Stop/go gates

The DnD gate can remove Shelf from the v1 proposal **only after** measured incompatibility is documented and the user approves a revised spec. A failed plugin compatibility gate blocks an API migration, not the ability to keep the old API. A visual pass is not done on screenshots alone: actual focus, monitor, fullscreen, reduced-motion and resource behavior must be checked. Backend extraction should be limited to repeated Hyprland seams identified in [ARCHITECTURE.md](ARCHITECTURE.md); it is not an independent rewrite milestone.

## Highest technical risks to monitor

1. Cross-app Wayland file DnD into/out of a layer-shell window, especially drag cancellation and copy/move semantics.
2. One global active plugin versus multi-monitor focus, fullscreen and a persistent dock; mode switch must not strand an expanded view.
3. Existing `Dual` transition and Hyprland Lua/`hyprctl` behavior under current Hyprland versions.
4. Plugin API/lifecycle compatibility when activity roles and geometry change; enabled external QML runs in process.
5. GPU/CPU cost of live previews, shaders, blur and continuous timers; actual cost is not yet measured.
6. Privacy/default-network and asset-license provenance before distribution.

Every milestone records what changed, commands/tests, hardware/runtime context and any unmet scenario. Green static validators alone do not prove the rendered product or live Linux integrations.
