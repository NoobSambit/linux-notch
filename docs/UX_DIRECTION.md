# Distinct UX and visual direction — design brief, not final artwork

## Product idea

A **desktop instrument rail**: a calm, precise surface that changes shape to match the task. The identity should feel native to a configurable Linux workstation: legible, efficient, restrained, and visibly under the user's control. Retain k4's useful depth while making daily actions simpler. This is a direction for future visual exploration, not a production palette or borrowed Droppy/Apple skin.

## Surface behavior

| Mode | Resting form | Expansion | Main use |
| --- | --- | --- | --- |
| Notch | Attached to top or bottom edge, compact status | Grows inward from the same anchor | Activity and quick access |
| Island | Detached from edge by a chosen gap; no fake hardware cutout | Grows around a stable center or chosen alignment | Focused floating surface |
| Dock | Persistent or hiding app/task row | Drawer and window previews emerge from dock | App navigation |
| Hybrid | Compact activity surface plus dock; two linked but independently useful parts | Activity expands in place; dock keeps task context | Workstation dashboard without a full panel |

Click, hover, drag and keyboard are different intents. Hover shows a compact preview after a tunable delay; click opens the chosen destination; file drag opens a visible drop target; dock drag reorders/pins. A keyboard shortcut opens a predictable destination on the preferred or focused display and returns focus correctly. Exit delay should tolerate the cursor moving from compact pill into expanded content. A click outside closes only intentionally opened views, consistent with existing k4 policy.

Full-screen choices: stay visible, overlay only on explicit action, or hide until deliberate reveal; keep a recovery shortcut. Reserving space must be explicit, because changing exclusive zones moves application windows. Default recommendation: reserve compact height in Notch, overlay in Island, reserve in Dock, independent choices in Hybrid. On multi-monitor setups, compact affordances may appear on all enabled displays, but only one expanded activity owns focus in v1; preferred monitor and active-interaction monitor take precedence in that order unless the user triggered a surface on a specific display. Rehome safely after unplugging.

The file Shelf is a **temporary workspace**, not a second file manager. Make it clear when a file is merely referenced, when a copy is being made, and whether the source exists. Provide a visible count, pin state, remove/clear and keyboard navigation. Keep file cards small enough to scan, with type/name/path, not giant thumbnails by default. Do not make the Shelf the only location of user data.

## Motion rules

- Morph size and content within the current surface for brief HUDs, media and user-opened views. Use a separate window only where a real editor, settings, fullscreen selector or accessibility/focus boundary needs it. `plugins/Settings` already uses a dedicated settings window; keep that separation.
- Interruption has a beginning, duration and return path. A transient should not restart its clock simply because the pointer lingers; a persistent recording state should not vanish under music.
- Use a small set of motion roles: fast feedback (roughly 100–180 ms), surface expansion (roughly 220–360 ms), and deliberate mode transition (roughly 350–600 ms). These are design starting points to validate on hardware, not measured promises. The existing `Dual` 1–2 second travel effect can remain as an optional expressive setting; default should be shorter.
- Animate geometry/opacity sparingly; pause visualizers, shaders and background effects when not visible. Avoid expensive full-screen blur for every frame. Do not stack independent springs on nested elements so the result wobbles unpredictably.
- Reduced motion chooses direct changes or short fades and disables decorative travel, pulse and unnecessary parallax. Respect system preference if available and expose a local override.

## Visual system to explore after approval

Explore 2–3 original directions using visual references from editorial/productivity tools and Linux desktop surfaces, with a documented originality check. Candidate design grammar: a purposeful type hierarchy (one display face for time/track, one highly readable UI face), a compact 4/8 px spacing rhythm, a small radius scale rather than one pill everywhere, restrained shadow and tint, and a subtle edge or seam that makes attached vs floating modes obvious. Icons should come from a legally usable family with consistent optical weight; k4's current Nerd Font glyph dependence needs legibility and licensing review before changing. No Droppy assets or Apple's exact black pill proportions.

Create dark and light variants with stable contrast, opaque fallback where blur harms reading, minimum hit target around 40–44 px where space permits, keyboard focus ring, text scaling checks and clear state labels that do not rely on color alone. View the design at small laptop, large external monitor and fractional scale. The next phase must use rendered screenshots/video and keyboard/assistive-tech review before a final style is locked.

Evidence behind these choices: k4's existing [surface/interaction host](../shell.qml) and [dock](../plugins/Dual/DualPlugin.qml); Droppy's documented [Shelf](https://getdroppy.app/docs/shelf), [notch/island controls](https://getdroppy.app/docs/notch) and [multiple activities](https://getdroppy.app/docs/live-activities). The proposed visual grammar is our own recommendation, not a claim that either product already implements it.
