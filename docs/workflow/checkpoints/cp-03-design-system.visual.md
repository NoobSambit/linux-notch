# CP-03 — owner visual-generation brief

## Purpose

Choose one original visual grammar for all four forms and shared controls before it spreads to later screens.

## Before generating

Wait until Codex activates this checkpoint after its prerequisites are approved. Start from the approved desktop-instrument-rail intent in UX_DIRECTION, not the inherited k4 palette. No final palette/type/radius is selected yet. Later checkpoints inherit this accepted set.
Codex lists exact prior approved sets/real-app captures in its activation message; if they are missing,
ask Codex to recover them before generating. Give your external image tool this whole brief and those
earlier images. Final palette/proportions are your selection, subject to feasibility and the approved scope.

## Required static images

Save all these files in **`review/cp-03-design-system/references/submitted/`**.
Each row is one complete board, not one file per crop. Label crops clearly; use harmless sample content.

| Exact recommended filename | Required? | Canvas / treatment | Detailed composition, hierarchy, geometry, states and controls |
| --- | --- | --- | --- |
| `cp-03__surface-family__dark__r01.png` | Required | 1920 × 1080; dark | Four labelled desktop crops: top attached Notch idle/expanded, detached Island idle/expanded, bottom Dock and Hybrid with reachable activity. Use calm dark material on a neutral Linux wallpaper. Keep the desktop edge visible. Compact content: clock/status and small media hint; expanded content: artwork, two-line track title and transport. Dock: 6–8 legally usable generic app icons and running markers; Hybrid retains both task and activity access. Show attached inward corners versus detached gap, consistent center/alignment anchor, small spacing rhythm, readable type hierarchy and bounded padding; suggest proportions rather than fixing every future geometry value. |
| `cp-03__surface-family__light__r01.png` | Required | 1920 × 1080; light | Same crops, content, alignment and scale as the dark family board, using a genuinely light surface, dark readable text and restrained elevation. Do not make light mode a dark pill pasted onto a pale wallpaper. Show opaque fallback and a selected/focused control with sufficient contrast; retain the same radius/type/icon and spacing roles. |
| `cp-03__controls-settings__both__r01.png` | Required | 1600 × 1000; both | Two equal dark/light columns. Above: shared button, slider, switch, card and input in normal/hover/pressed/focus/selected/disabled/loading/error states. Below: a separate searchable settings window with short navigation and appearance/surface preview pane. Prioritize label then value then help text; consistent 4/8 px starting rhythm and around 40–44 px hit areas where practical, no cramped icon-only controls. Include long translated label/enlarged-text example and an opaque material swatch. This is a control/navigation grammar, not a new settings architecture. |

Preserve approved semantic color/type/icon/motion roles. Show compact/expanded relationships explicitly,
comfortable spacing and focus; dark/light must retain equivalent hierarchy. Dimensions above are reference
canvases, not hardcoded application sizes. Generated text may be approximate; Codex converts it into
real accessible controls rather than baking the board into the UI.

## Motion reference

Required file: **`review/cp-03-design-system/references/storyboards/cp-03__expansion-motion__both__r01.png`**.
Use a wide **1920 × 1080** board, with readable labelled frames in order and dark/light rows (or clearly
paired theme strips). Four labelled frames per theme: compact Notch → expansion start → content appearing → settled expanded; add a reduced-motion before/after pair. Keep the edge/alignment anchor fixed, grow inward; text/art fade after usable space exists. Identify stationary anchor, moving boundaries and fading content with small annotations. Use feedback 100–180 ms and expansion 220–360 ms only as trial ranges, no prescribed spring overshoot. Reduced motion changes directly or briefly fades, with no travel/pulse.

Optional individual keyframes use the same stem with `__frame-01`, `__frame-02`, etc. Optional video
uses the same stem with `.webm` or `.mp4` in this storyboard folder; a labelled PNG/WebP storyboard is
still mandatory. Video is local by default. These are proposed transitions; actual animation/focus/frame
behavior must be proven later by recording the running app. A static image alone proves no motion.

## Variants and revisions

One complete dark/light family is mandatory. Optionally explore one additional original family in alternatives/r02; do not generate many minor color variants. Owner chooses one coherent family, not incompatible fragments.
Alternatives belong in **`review/cp-03-design-system/references/alternatives/`**, with `r02`, `r03`, etc. in the filename.
Use `review/cp-03-design-system/references/NOTES.md` or a message to identify preferred files and what you like.
For a proposed replacement, put a new revision in submitted/storyboards; never overwrite approved images.
Codex preserves selected sets in `review/cp-03-design-system/references/approved/rNN/` only after your explicit approval.

## Constraints

- Qt 6/QML/Quickshell, Wayland/Hyprland for v1; top/bottom supported, sides compatibility-only.
- No copied Apple/Droppy/k4 branding, exact proprietary pill, logos, artwork or unlicensed production assets.
  Use neutral placeholder app icons/content where rights are unknown.
- Stay inside [V1_SPEC](../../V1_SPEC.md), [UX_DIRECTION](../../UX_DIRECTION.md) and this checkpoint’s
  [scope](cp-03-design-system.md); no Basket/shake, OCR/conversion/cloud, Apple-only actions, unsupported device signals
  or independently expanded activity queues. Preserve one recognizable design language.
- No technically imaginary global drag tracking, impossible desktop interception, fake focus behavior or
  unnecessary clutter. Accessibility/opaque fallback must remain possible. Material feasibility changes
  are shown to you for approval, never silently invented during coding.

## Owner deliverables and submission

- [ ] `cp-03__surface-family__dark__r01.png` — submitted folder.
- [ ] `cp-03__surface-family__light__r01.png` — submitted folder.
- [ ] `cp-03__controls-settings__both__r01.png` — submitted folder.
- [ ] `cp-03__expansion-motion__both__r01.png` — storyboards folder.
- [ ] Optionally save one alternate proposal in the alternatives folder, clearly named with a new revision.
- [ ] Name your preferred set/files and add short preferences. PNG recommended; JPEG/WebP with matching
  extension is supported. Aim below 2 MB per image; keep large originals local.
- [ ] Tell Codex: **“References ready for CP-03 in `review/cp-03-design-system/references/`. I prefer r01 [list any mixed revisions].
  Please open them and check completeness and feasibility.”** This submits them; it does not approve coding.
- [ ] After Codex shows the exact feasible selection, say **“I approve Gate A for CP-03, set r01, as listed,
  including the feasibility notes.”** Codex records your words, exact paths and hashes before visual coding.

After implementation, use [your personal tests](../../../owner/checkpoints/cp-03-design-system.md) to approve the actual app separately
(Gate B). Concepts are guidance, not pixel-perfect requirements or automatically licensed runtime assets.
