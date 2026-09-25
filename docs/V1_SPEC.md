# Proposed v1 product specification — product approval pending

**Direction:** k4 foundation + major UX/visual polish + selected high-value Droppy workflows + our own identity. Qt 6/QML/Quickshell, Wayland/Hyprland, a narrow compositor seam, plugin compatibility, MIT compatibility and local-first architecture are approved. This **product scope** still needs approval before implementation. See [daily experience](V1_EXPERIENCE.md), [feature evidence](FEATURE_MATRIX.md), and [decisions](DECISIONS.md).

V1 succeeds when the four forms feel like one predictable desktop product: apps and clipboard are quick to reach, file handoff is safe, media and system events do not interrupt work, and display/fullscreen behavior is understandable. Module count is not a success measure. Preserve useful inherited features by default. Remove one only with evidence that it is dead, redundant, broken, unsafe, rights-incompatible, unmaintainable, or harmful to the new direction; document the removal and user impact.

## MUST HAVE — CORE V1

1. **One surface, four modes.** Notch attaches to a top/bottom edge; Island floats off that edge; Dock centers app/task navigation; Hybrid keeps activity access and dock tasks together. Reuse k4's host and `Dual` dock, with no parallel host. Switching modes preserves open work, IPC shortcuts and plugin state. Existing side placement remains, with top/bottom as v1 visual gates.
2. **An early, original design system.** Define shared QML tokens/components for typography, spacing, radii, icon sizes, elevation, opacity, shadows, restrained blur, compact/expanded dimensions, motion, focus, hover, dark/light and reduced motion. Start with the core surface, settings navigation and dock; carry that grammar into each touched module. This is a release requirement, not a final cosmetic pass. Do not copy k4 branding, Droppy assets or Apple's exact island.
3. **Clear input rules.** Hover reveals a lightweight preview after a configurable delay; click deliberately opens a destination; drag exposes a file drop target; shortcuts open a predictable view; ESC and click-outside close intentional views without focus theft. Expansion, hide delays and fullscreen interaction need safe defaults. See [interaction rules](UX_DIRECTION.md).
4. **Bounded geometry and display policy.** Expose mode, top/bottom edge, width, height, alignment, offsets, applicable radius, reserve/overlay behavior, preferred monitor, focused-monitor behavior and fullscreen policy. Rehome the active surface after hotplug/monitor loss; keep one expanded activity owner in v1. Validate persisted settings and recover from offscreen states. Free movement across the desktop is later.
5. **Coherent live activities and HUDs.** Extend k4's existing owner and priority policy; do not add a competing Activity Router. Existing media, volume, notifications, recording, battery, Wi-Fi, Bluetooth and system status get clear compact/persistent/expanded roles where a real signal exists. Brief HUDs may interrupt media and restore it; user-opened views retain focus; recording remains visible; stale transients expire. Brightness joins only if a real backlight control/event source is verified. Legacy plugin `active/priority/view` keeps working through a tested compatibility path.
6. **Local file Shelf and small action foundation.** Accept file/folder URI drops from supported Wayland apps, stage local references, allow drag-out, open, reveal, copy path, remove, clear and optional pin. Provide a non-drag keyboard path. Preserve originals by default and advertise copy on drag-out; no implicit move. Show missing sources and unsupported offers. Initial actions stay small and extensible; optional compression is allowed only if low-cost and does not delay the core flow. Confirm cross-app drag-in/out in a Hyprland feasibility gate before final Shelf mechanics are locked.
7. **Richer clipboard experience on existing storage.** Keep current text/image history, search and pin as the base. Improve preview hierarchy, type distinction, surface entry, keyboard search/selection, pin feedback and sensitive-content behavior. Evaluate file-reference offers against the `wl-paste` watcher/storage architecture; include them only if semantics and security are reliable. Do not require a storage rewrite for visual improvement.
8. **Existing dock and Linux essentials stay usable.** Preserve pinned/running apps, focus, previews, reordering and drawer; media, launcher, notifications, clipboard, control center, audio/network/Bluetooth, capture/recording, editor, wallpaper/theme, settings, terminal/SSH, plugins and optional modules remain available unless an individually documented removal passes the evidence rule. Missing optional dependencies should show a clear unavailable state.
9. **Trust, access and resource discipline.** No telemetry; local clipboard and Shelf metadata; explicit network controls. Keyboard access, visible focus, accessible names, contrast, text scaling and reduced motion apply across the core surface and settings. Measure idle/media/dock/transition CPU, RSS, GPU and frames on named hardware before setting numerical budgets. Suspend hidden visualizers/animations, avoid duplicate watchers and unnecessary polling, and keep disabled optional modules inactive.

## SHOULD HAVE — V1 POLISH

- Reorganize the existing searchable settings window by user intent: Appearance, Surface, Behavior, Dock, Activities, Files, Clipboard, Display, Performance, Privacy, Plugins and Advanced. Preserve stable setting IDs/IPC aliases; show previews and a recovery path for bad geometry. [UX_DIRECTION.md](UX_DIRECTION.md) maps current groups.
- Give the launcher, media, notification center, control center, capture entry points and dock consistent hierarchy, motion and empty/error states. Keep the existing depth of editor, games and other optional modules without redesigning every screen in v1.
- Offer “send captured file to Shelf” if existing capture output supports a safe handoff without expanding the capture pipeline; retain existing destinations.
- Maintain plugin compatibility and diagnostics. Future additive roles may include compact activity, expanded view, dock item, background provider, actions and settings page; v1 adds only roles its own features require. No plugin store work.
- Document a clear manual Hyprland install/dependency path without a multi-distro installer program.

## OPTIONAL / LATER — DEFER NEW WORK

Basket and shake-to-summon; OCR; PDF/general conversion suite; AI background removal; calendar/reminders/meetings; advanced dictation; cloud upload/providers; extensive agent HUDs; universal camera/privacy detection; advanced gestures; per-monitor independent activity queues; Niri/KDE/GNOME/X11; universal distro packaging; plugin store or widget marketplace. Existing k4 functionality in these categories remains a keep candidate; “defer” means no major **new** build for v1. Side-edge visual parity and full media queue/lyrics are later unless cheap during core polish.

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
| Notification arrives | Briefly interrupts eligible passive activity, enters history and never displaces an intentional user session. |
| Volume changes | Short HUD replaces passive media, expires, then current media returns; rapid changes coalesce. Brightness behaves likewise only where verified. |
| Recording starts | Persistent, reachable indicator and stop path survive notifications and mode switches. |
| File approaches / drops | Shelf target appears; stage, inspect, act and drag/copy out while original stays untouched. Missing files are explicit. |
| Clipboard shortcut | Searchable text/image previews, clear pin/copy feedback, keyboard selection and honest secret handling. |
| Dock / Hybrid switch | Pinned/running apps and task state persist; activity affordance remains understandable. |
| Fullscreen / monitor loss | Apply policy per affected display; rehome before focus or controls are stranded. |
| Reduced motion | State remains legible with direct changes or short fades; decorative travel, pulse and idle shaders stop. |

These scenarios are the implementation's behavioral reference, with fuller plain-language detail in [V1_EXPERIENCE.md](V1_EXPERIENCE.md). Remaining product choices are in [DECISIONS.md](DECISIONS.md). No implementation begins before scope approval.
