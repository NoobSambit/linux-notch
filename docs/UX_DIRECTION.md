# Distinct UX and visual direction — design brief, not final artwork

## Product idea

A **desktop instrument rail**: a calm, precise surface that changes shape to match the task. The identity should feel native to a configurable Linux workstation: legible, efficient, restrained, and visibly under the user's control. Retain k4's useful depth while making daily actions simpler. Design-system and core-surface work start early, before major feature expansion; this brief is not a production palette or borrowed Droppy/Apple skin. See the [plain-language experience](V1_EXPERIENCE.md).

## Surface behavior

| Mode | Resting form | Expansion | Main use |
| --- | --- | --- | --- |
| Notch | Attached to top or bottom edge, compact status | Grows inward from the same anchor | Activity and quick access |
| Island | Detached from edge by a chosen gap; no fake hardware cutout | Grows around a stable center or chosen alignment | Focused floating surface |
| Dock | Persistent or hiding app/task row | Drawer and window previews emerge from dock | App navigation |
| Hybrid | Compact activity surface plus dock; two linked but independently useful parts | Activity expands in place; dock keeps task context | Workstation dashboard without a full panel |

Click, hover, drag and keyboard are different intents. Hover shows a compact preview after a tunable entry delay and never takes keyboard focus; click opens the chosen destination and gives it focus only when needed; a file drag reveals a visible Shelf target; dock drag reorders/pins. A keyboard shortcut opens a predictable destination on the preferred or focused display and returns focus correctly. Exit delay must tolerate moving from pill to preview. ESC and click-outside close an intentional view in a documented order; click-outside behavior stays configurable for compatibility. A transient HUD must never reopen a view just dismissed by the user. Avoid a full-screen input catcher unless testing proves it is needed and does not block underlying apps.

Full-screen choices: stay visible, overlay only on explicit action, or hide until deliberate reveal; keep a recovery shortcut. Reserving space must be explicit, because changing exclusive zones moves application windows. Default proposal: reserve compact height in Notch, overlay in Island, reserve in Dock, independent choices in Hybrid. On multiple monitors, use a persisted preferred display if available; a pointer/shortcut interaction on a different enabled display can temporarily claim the expanded view, and focused-monitor fallback applies when no preferred display survives. Compact affordances may appear on enabled displays, but only one expanded activity owns focus in v1. Apply fullscreen policy to the affected display and rehome safely after unplugging; do not promise independent per-monitor activity queues.

The file Shelf is a **temporary workspace**, not a second file manager. Make it clear when a file is merely referenced, when a copy is being made, and whether the source exists. Provide a visible count, pin state, open/reveal/copy-path/remove/clear actions and keyboard navigation. Keep file cards small enough to scan, with type/name/path, not giant thumbnails by default. Use a small list of actions with availability and handler rules so later conversion/OCR/share actions can be added without hardcoding them into file cards; do not expose speculative actions in v1 or redesign the plugin registry. Do not make the Shelf the only location of user data.

Clipboard is another frequent surface destination. k4 already has text/image history, substring search, pinning and keyboard selection (`services/Clipboard.qml`, `plugins/Clipboard/*`, `tools/portapapeles.py`). Keep those foundations. Use distinct text/image previews, readable source/age/size metadata where known, clear pinned state, quick search focus and copy feedback. A “file” category requires a proven file-reference MIME/watch path; do not label plain paths as copied files. Secret exclusion needs real password-manager tests and honest wording because current MIME heuristics are not a universal guarantee.

For activities, the compact layer should answer “what is happening?” and the expanded layer “what can I do?” Media may persist passively; volume and routine notifications are short; recording and critical status remain reachable. Coalesce repeat changes, expire hidden transients, restore from current source state, and never steal focus from a deliberate session. Wi-Fi/Bluetooth/battery use the Linux services already present. Brightness is conditional on a real backlight signal; camera/microphone claims require separate evidence.

## Motion rules

- Morph size and content within the current surface for brief HUDs, media and user-opened views. Use a separate window only where a real editor, settings, fullscreen selector or accessibility/focus boundary needs it. `plugins/Settings` already uses a dedicated settings window; keep that separation.
- Interruption has a beginning, duration and return path. A transient should not restart its clock simply because the pointer lingers; a persistent recording state should not vanish under music.
- Use a small set of motion roles: fast feedback (roughly 100–180 ms), surface expansion (roughly 220–360 ms), and deliberate mode transition (roughly 350–600 ms). These are design starting points to validate on hardware, not measured promises. The existing `Dual` 1–2 second travel effect can remain as an optional expressive setting; default should be shorter.
- Animate geometry/opacity sparingly; pause visualizers, shaders and background effects when not visible. Avoid expensive full-screen blur for every frame. Do not stack independent springs on nested elements so the result wobbles unpredictably.
- Reduced motion chooses direct changes or short fades and disables decorative travel, pulse and unnecessary parallax. Respect system preference if available and expose a local override.

## Practical QML design-system layer

Build on `core/Theme.qml`, `core/Island*`, `core/SiluetaIsla.qml`, public `api/K4/Tema.qml`, shared `widgets/*` and reusable `api/K4` controls. The current theme already centralizes some palette/geometry while `plugins/Dual/Muelle.qml` has its own dimensions and effects. Add semantic tokens to the existing theme and shared components before spreading them through the host and plugins; do not create a second competing theme singleton or force external plugins to adopt new tokens immediately. Separate **semantic roles** (surface, text, accent, warning, focus) from raw values so dark/light, contrast and user customization can change values without rewriting screens.

| Area | Shared contract to define early | Validation |
| --- | --- | --- |
| Spacing and dimensions | Small spacing scale, compact height, expanded padding, item gap and hit-area minimum; mode-specific geometry remains configurable. | Dense and roomy layouts, laptop/external screens, fractional scale, clipping. |
| Shape and elevation | Radius scale for attached edge, floating body, cards and controls; a few elevation levels with opacity/shadow tokens. | Attached vs floating reads clearly without one universal pill. |
| Typography and icons | Display/body/label roles, weight and line-height; icon size/optical alignment scale and legally usable family. | Long translations, text scaling, missing glyph fallback. |
| Color and material | Semantic foreground/background/status roles; light/dark variants; bounded blur/opaque fallback. | Contrast in both themes and over varied wallpapers; blur cost measured. |
| Motion | Feedback, expansion and mode-change duration roles; one spring family with bounded overshoot; explicit interruption/restore timing. | Rendered transition video and frame traces; no nested spring wobble. |
| Interaction states | Focus ring, hover, pressed, selected, disabled, loading and error states in shared controls. | Keyboard-only use, click/hover separation, non-color status cues. |
| Reduced motion | One setting/system-preference resolution feeding shared motion tokens. | No decorative travel, pulse or idle shader when enabled. |

These are token **categories**, not final colors or exact measurements. The 4/8 px rhythm and motion ranges below are starting hypotheses to validate on real hardware and content, not a fixed aesthetic. Preserve current `K4.Tema` compatibility while new screens adopt the shared roles. Optional plugins can continue rendering their own UI; first-party modules touched for v1 should use the system.

## Settings grouped by user intent

Keep `plugins/Settings/VentanaAjustes.qml` as a searchable separate window. `services/Settings.qml` already has stable section IDs, and `plugins/Settings/FilaPlugin.qml` exposes plugin settings; group the navigation and descriptions without renaming persisted keys or breaking `k4 settingsSection` aliases. Proposed mapping:

| New group | Existing source and what belongs there |
| --- | --- |
| Appearance | `apariencia`, `efectos`; theme, type, icon, motion and light/dark controls. |
| Surface | `island`, `colocacion`; mode, size, edge, reserve/overlay and previews. |
| Behavior | `cerrarConClicFuera`, hover/hide/shortcut behavior and safe recovery. |
| Dock | `Dual` plugin settings (`ambas`, effect, app pins, hide behavior), surfaced with the four modes. |
| Activities | Notification-on-hover/focus rules, media/HUD visibility and durations, recording status. |
| Files | Shelf retention/actions and existing file/capture destination entry points. |
| Clipboard | Existing history/search/pin behavior and secret-handling controls. |
| Display | Preferred/focused monitor, hotplug and fullscreen policy; `ventanas`/per-view placement where relevant. |
| Performance | Reduced motion, visualizer/blur options and measured-cost explanations. |
| Privacy | `datos` personal-source toggles, network lookups, clipboard retention and local-file metadata. |
| Plugins | Existing `plugins` group and plugin-contributed settings; show active/dependency state. |
| Advanced | Language (`idioma`), capture/recording/editor technical options, optional game (`mazmorra`), diagnostics and compatibility controls. |

This is an information-architecture proposal, not an instruction to hide core capture or game features. Search should find an option across groups, and plugin-owned settings stay next to their enable controls where useful. An option can be linked from multiple user journeys without duplicating its stored value. Avoid twelve equally prominent top-level tabs if usability testing shows a smaller visible navigation works better.

## Original visual identity to explore after approval

Explore 2–3 original directions using visual references from editorial/productivity tools and Linux desktop surfaces, with a documented originality check. Candidate grammar: a purposeful type hierarchy, a compact 4/8 px spacing rhythm, a small radius scale, restrained shadow and tint, and a subtle seam between attached and floating forms. Icons need a legally usable family with consistent optical weight; k4's Nerd Font glyph dependence needs legibility and licensing review before changing. No Droppy assets, current k4 branding or Apple's exact black pill proportions. Final naming, palette and artwork remain later decisions, but the shared token/component structure is early work.

Create dark and light variants with stable contrast, opaque fallback where blur harms reading, minimum hit target around 40–44 px where space permits, keyboard focus ring, text scaling checks and clear state labels that do not rely on color alone. View the design at small laptop, large external monitor and fractional scale. The next phase must use rendered screenshots/video and keyboard/assistive-tech review before a final style is locked.

Evidence behind these choices: k4's existing [surface/interaction host](../shell.qml) and [dock](../plugins/Dual/DualPlugin.qml); Droppy's documented [Shelf](https://getdroppy.app/docs/shelf), [notch/island controls](https://getdroppy.app/docs/notch) and [multiple activities](https://getdroppy.app/docs/live-activities). The proposed visual grammar is our own recommendation, not a claim that either product already implements it.
