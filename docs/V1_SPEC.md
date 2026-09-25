# V1 product specification — direction approved, implementation pending

**Direction:** k4 foundation + major UX/visual polish + selected high-value Droppy workflows + our own identity. Qt 6/QML/Quickshell, Wayland/Hyprland, a narrow compositor seam, plugin compatibility, MIT compatibility and local-first architecture are approved. This document does **not** authorize implementation. See [daily experience](V1_EXPERIENCE.md), [feature evidence](FEATURE_MATRIX.md), and [decisions](DECISIONS.md).

V1 succeeds when the four forms feel like one predictable desktop product: apps and clipboard are quick to reach, file handoff is safe, media and system events do not interrupt work, and display/fullscreen behavior is understandable. Module count is not a success measure. Preserve useful inherited features by default. Remove one only with evidence that it is dead, redundant, broken, unsafe, rights-incompatible, unmaintainable, or harmful to the new direction; document the removal and user impact.

## MUST HAVE — CORE V1

1. **One surface, four modes.** Notch attaches to a top/bottom edge; Island floats off that edge; Dock centers app/task navigation; Hybrid keeps activity access and dock tasks together. Reuse k4's host and `Dual` dock, with no parallel host. Switching modes preserves open work, IPC shortcuts and plugin state. Existing left/right host paths are **experimental/compatibility-only** in v1; top/bottom are the supported release gates.
2. **An early, original design system.** Define shared QML tokens/components for typography, spacing, radii, icon sizes, elevation, opacity, shadows, restrained blur, compact/expanded dimensions, motion, focus, hover, dark/light and reduced motion. Start with the core surface, settings navigation and dock; carry that grammar into each touched module. This is a release requirement, not a final cosmetic pass. Do not copy k4 branding, Droppy assets or Apple's exact island.
3. **Clear input rules.** Hover reveals a lightweight preview after a configurable delay; click deliberately opens a destination; drag exposes a file drop target; shortcuts open a predictable view; ESC and click-outside close intentional views without focus theft. Expansion, hide delays and fullscreen interaction need safe defaults. See [interaction rules](UX_DIRECTION.md).
4. **Bounded geometry and display policy.** Expose mode, top/bottom edge, width, height, alignment, offsets, applicable radius, reserve/overlay behavior, preferred monitor, focused-monitor behavior and fullscreen policy. Rehome the active surface after hotplug/monitor loss; keep one expanded activity owner in v1. Validate persisted settings and recover from offscreen states. Free movement across the desktop is later.
5. **Coherent live activities and HUDs.** Extend k4's existing host Activity Policy; never add a second activity owner. Media, volume, recording, battery, Wi-Fi, Bluetooth and system status get clear roles where a real signal exists. Notification activity/history/actions require **Own notification mode**; External/off mode leaves another daemon in control and honestly marks those views unavailable. Brief HUDs may interrupt media and restore it; user-opened views retain focus; recording remains visible; stale transients expire. Brightness joins only if a real backlight source is verified. Legacy plugin `active/priority/view` keeps working through a tested compatibility path.
6. **Local file Shelf and small action foundation.** The **first technical gate after baseline/safety** is an isolated Hyprland/Quickshell layer-shell DnD spike, before major geometry/activity work. It must test file managers, `text/uri-list`, folders, multiple files, drag-out, copy/move, cancellation, missing source, keyboard fallback and same/multi-monitor behavior where practical. If it fails, record the exact limitation and return Shelf scope for product review; no silent workaround. After a positive gate, stage local references, allow drag-out, open, reveal, copy path, remove, clear and optional pin. Preserve originals and advertise copy by default; no implicit move.
7. **Richer clipboard experience on existing storage.** Keep current text/image history, search and pin as the base. Improve preview hierarchy, type distinction, surface entry, keyboard search/selection, pin feedback and sensitive-content behavior. Evaluate file-reference offers against the `wl-paste` watcher/storage architecture; include them only if semantics and security are reliable. Do not require a storage rewrite for visual improvement.
8. **Tiered inherited support.** Dock, media, notifications in Own mode, clipboard, control-center essentials, settings and plugin host are release blockers. Existing editor, wallpaper, capture depth, terminal/SSH, window and agent tools remain supported with smoke/regression checks; peripheral games, Digivice and GPU-heavy Atalaya remain available as optional/experimental candidates subject to rights and performance checks. A tier is a validation promise, never deletion permission. Missing optional dependencies show an unavailable state.
9. **Trust, access and resource discipline.** **No telemetry in the Notchbar core.** Network-capable features and plugins are disclosed and user-controllable where practical; the whole application cannot guarantee no network use, and third-party QML plugins are in-process and unsandboxed. Clipboard and Shelf metadata stay local. Keyboard access, visible focus, accessible names, contrast, text scaling and reduced motion apply across the core surface and settings. Measure idle/media/dock/transition CPU, RSS, GPU and frames before numerical budgets; suspend hidden effects and disabled optional modules.

## Support tiers and release gates

Assign tiers by **daily product role, source integration depth, default enablement, change exposure, optional dependencies, measured cost and rights evidence**, not by a feature's novelty. See the [source audit](RESEARCH_K4.md) and [migration map](K4_MIGRATION_PLAN.md). Every tier receives targeted regression checks when changed.

| Tier | Included inherited/new paths | Release expectation |
| --- | --- | --- |
| **CORE V1** | Core surface/four modes, dock/Hybrid, host Activity Policy, media, volume/recording/system HUDs, notifications **when Own mode is selected**, clipboard, Shelf, launcher/control-center essentials, settings and plugin host/IPC. | End-to-end scenario, focus/accessibility, one/two-monitor and performance checks; broken core path blocks release. External notification mode must remain usable and honest, but cannot provide standard notification history/actions. |
| **SUPPORTED INHERITED** | Capture and recording depth/editor, wallpaper/Hypr theme, terminal/SSH, window/workspace tools, Files search, agent/Ask tools, session utilities and existing plugin discovery. | Keep available, test startup/key workflows and dependencies; no major v1 redesign. A regression caused by v1 work must be fixed. Existing network paths need disclosure/controls. |
| **EXPERIMENTAL / OPTIONAL INHERITED** | Game, Digivice, GPU-heavy Atalaya previews and other niche modules after individual review. Game/Digivice are default-off in `plugins/catalog.json`; Atalaya is currently **default-on**, so its idle/input cost and opt-out/default require a baseline check. | Keep available in development; test no crash or collateral regression when enabled. Feature depth is not a v1 quality gate, but safety, rights and severe performance problems can block *shipping that payload/default*. Document any release exclusion separately. |

The [asset/data/IP audit](ASSET_LICENSE_AUDIT.md) gates distribution of questionable bundled material, not the start of core implementation. Tier changes require evidence; no tier authorizes deleting a module.

## SHOULD HAVE — V1 POLISH

- Reorganize the existing searchable settings window by user intent: Appearance, Surface, Behavior, Dock, Activities, Files, Clipboard, Display, Performance, Privacy, Plugins and Advanced. Preserve stable setting IDs/IPC aliases; show previews and a recovery path for bad geometry. [UX_DIRECTION.md](UX_DIRECTION.md) maps current groups.
- Give the launcher, media, notification center **in Own mode**, control center, capture entry points and dock consistent hierarchy, motion and empty/error states. In External notification mode, show an honest unavailable state. Keep supported/optional depth without redesigning every screen in v1.
- Offer “send captured file to Shelf” if existing capture output supports a safe handoff without expanding the capture pipeline; retain existing destinations.
- Maintain plugin compatibility and diagnostics. Future additive roles may include compact activity, expanded view, dock item, background provider, actions and settings page; v1 adds only roles its own features require. No plugin store work.
- Document a clear manual Hyprland install/dependency path without a multi-distro installer program.

## OPTIONAL / LATER — DEFER NEW WORK

Basket and shake-to-summon; OCR; PDF/general conversion suite; AI background removal; calendar/reminders/meetings; advanced dictation; cloud upload/providers; extensive agent HUDs; universal camera/privacy detection; advanced gestures; per-monitor independent activity queues; Niri/KDE/GNOME/X11; universal distro packaging; new plugin store or widget marketplace. Existing k4 functionality in these categories remains a keep candidate; “defer” means no major **new** build for v1. Full left/right parity and media queue/lyrics are later unless separately proven cheap.

## REJECT

- Copying proprietary Droppy code/assets, Apple's exact pill, or k4 branding as the new identity.
- A stack rewrite without a demonstrated blocker, silent cloud traffic, telemetry, or implicit sensitive sharing.
- Presenting AirDrop, iMessage, Finder Services, Mission Control or Apple Clock parity as Linux v1 features.
- Deleting optional inherited features just to shorten the spec. Actual removal follows the evidence rule above.

## V1 feature lock by product role

| Category | Feature | Why now |
| --- | --- | --- |
| CORE V1 | Four modes, geometry, display and fullscreen rules | User control of form is the product identity. |
| CORE V1 | Design system and core-surface polish | Coherence guides every subsequent screen and motion decision. |
| CORE V1 | Interaction semantics and activity handoff | Predictable behavior matters more than HUD count. |
| CORE V1 | Existing Linux services, dock, plugin and IPC continuity | The k4 foundation avoids rebuilding working plumbing. |
| DROPPY-INSPIRED V1 | Shelf plus small file actions | High-value local handoff with bounded scope. |
| DROPPY-INSPIRED V1 | Richer clipboard UX | Improves an existing daily tool without a default storage rewrite. |
| DROPPY-INSPIRED V1 | Clear hover/click/drag and activity presentation | Adapts strong interaction ideas to k4's owner and Linux signals. |
| V1 POLISH | Settings, launcher, media, notifications, dock, control center, capture | Frequent touchpoints share one visual and behavioral language. |
| DEFER | Basket, OCR/conversion suite, cloud, meetings, AI breadth, new backends/store | Distinct platform, privacy or maintenance scope. |
| REJECT | Product copying, silent uploads/telemetry, novelty rewrite | Conflicts with identity or trust. |

## Core experience and acceptance

| Moment | Expected v1 behavior |
| --- | --- |
| Idle | Quiet compact status/activity, or task dock in Dock mode; optional modules do not animate or poll merely to decorate idle. |
| Hover | Delayed lightweight reveal without keyboard focus theft; moving into revealed content does not immediately close it. |
| Click / shortcut | Opens the configured destination; shortcut targets the chosen display and places focus in the view. ESC/click-outside closes predictably. |
| Media starts | Compact playback information appears where mode permits; expanded controls are available without replacing unrelated persistent indicators. |
| Notification arrives | In Own mode, briefly interrupts eligible passive activity, enters history and never displaces an intentional user session. In External mode, the other daemon owns delivery; Notchbar does not claim mirrored history/actions. |
| Volume changes | Short HUD replaces passive media, expires, then current media returns; rapid changes coalesce. Brightness behaves likewise only where verified. |
| Recording starts | Persistent, reachable indicator and stop path survive notifications and mode switches. |
| File approaches / drops | Shelf target appears; stage, inspect, act and drag/copy out while original stays untouched. Missing files are explicit. |
| Clipboard shortcut | Searchable text/image previews, clear pin/copy feedback, keyboard selection and honest secret handling. |
| Dock / Hybrid switch | Pinned/running apps and task state persist; activity affordance remains understandable. |
| Fullscreen / monitor loss | Apply policy per affected display; rehome before focus or controls are stranded. |
| Reduced motion | State remains legible with direct changes or short fades; decorative travel, pulse and idle shaders stop. |

These scenarios are the behavioral reference, with plain-language detail in [V1_EXPERIENCE.md](V1_EXPERIENCE.md). [D20](DECISIONS.md#d20-detail--notification-ownership) explains notification ownership. No implementation begins before explicit implementation approval.
