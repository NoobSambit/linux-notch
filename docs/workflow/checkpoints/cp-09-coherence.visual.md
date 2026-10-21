# CP-09 — owner visual-generation brief

## Purpose

Unify remaining daily entry points and make settings easy to find without redesigning supported deep tools.

## Before generating

Wait until Codex activates this checkpoint after its prerequisites are approved. Use CP-03 shared system and actual approved app captures from CP-04–08 supplied by Codex; do not invent another palette/control system or rearrange persisted values.
Codex lists exact prior approved sets/real-app captures in its activation message; if they are missing,
ask Codex to recover them before generating. Give your external image tool this whole brief and those
earlier images. Final palette/proportions are your selection, subject to feasibility and the approved scope.

## Required static images

Save all these files in **`review/cp-09-coherence/references/submitted/`**.
Each row is one complete board, not one file per crop. Label crops clearly; use harmless sample content.

| Exact recommended filename | Required? | Canvas / treatment | Detailed composition, hierarchy, geometry, states and controls |
| --- | --- | --- | --- |
| `cp-09__settings-navigation__dark__r01.png` | Required | 1600 × 1000; dark | Separate searchable settings window with manageable user-intent navigation, current Surface/Display choice, live preview, values/help and safe reset. Show Appearance, Surface, Behavior, Dock, Activities, Files, Clipboard, Display, Performance, Privacy, Plugins and Advanced as grouped/searchable destinations without forcing twelve equally prominent tabs. Hierarchy: search/nav, section title, labelled value/control, supporting help. Approved padding, rows, focus, small radius/elevation and readable preview at laptop size. |
| `cp-09__settings-privacy-plugins__light__r01.png` | Required | 1600 × 1000; light | Matching light settings window showing privacy/network toggles, local Shelf/clipboard retention explanation, plugin enable/dependency state and clear in-process/no-sandbox disclosure. Include unavailable optional tool, safe saved-setting feedback and search match. Use existing stable meanings; do not expose implementation internals except where they inform plugin/network decisions. Shared light contrast, row spacing, focus/error states and a long translated label. |
| `cp-09__core-entry-states__both__r01.png` | Required | 1920 × 1080; both | Dark/light pairs of launcher search/results, control-center essentials, Own notification history/action versus External unavailable message, and capture entry/cancel. Keep recognizable module functions but shared type/icons/spacing/material and keyboard focus. Show compact entry and expanded bounds; capture selector/editor may keep a separate surface. Optional capture→Shelf appears only if the existing output handoff proves simple. No deep editor/game redesign or speculative tools. |

Preserve approved semantic color/type/icon/motion roles. Show compact/expanded relationships explicitly,
comfortable spacing and focus; dark/light must retain equivalent hierarchy. Dimensions above are reference
canvases, not hardcoded application sizes. Generated text may be approximate; Codex converts it into
real accessible controls rather than baking the board into the UI.

## Motion reference

Required file: **`review/cp-09-coherence/references/storyboards/cp-09__settings-and-entry-navigation__both__r01.png`**.
Use a wide **1920 × 1080** board, with readable labelled frames in order and dark/light rows (or clearly
paired theme strips). Four frames: deliberate settings open → search result → chosen section/preview updated → close with focus return. Add core surface → capture entry → canceled selection → restored prior surface. Settings stays a separate window; nav/content fade only where useful, controls do not travel between windows. Include reduced-motion direct changes and identify all anchors/focus-transfer points.

Optional individual keyframes use the same stem with `__frame-01`, `__frame-02`, etc. Optional video
uses the same stem with `.webm` or `.mp4` in this storyboard folder; a labelled PNG/WebP storyboard is
still mandatory. Video is local by default. These are proposed transitions; actual animation/focus/frame
behavior must be proven later by recording the running app. A static image alone proves no motion.

## Variants and revisions

One coherent navigation solution based on the approved settings map; optionally one alternative grouping in the alternatives folder with revision r02 if it reduces clutter without hiding options or changing saved meaning.
Alternatives belong in **`review/cp-09-coherence/references/alternatives/`**, with `r02`, `r03`, etc. in the filename.
Use `review/cp-09-coherence/references/NOTES.md` or a message to identify preferred files and what you like.
For a proposed replacement, put a new revision in submitted/storyboards; never overwrite approved images.
Codex preserves selected sets in `review/cp-09-coherence/references/approved/rNN/` only after your explicit approval.

## Constraints

- Qt 6/QML/Quickshell, Wayland/Hyprland for v1; top/bottom supported, sides compatibility-only.
- No copied Apple/Droppy/k4 branding, exact proprietary pill, logos, artwork or unlicensed production assets.
  Use neutral placeholder app icons/content where rights are unknown.
- Stay inside [V1_SPEC](../../V1_SPEC.md), [UX_DIRECTION](../../UX_DIRECTION.md) and this checkpoint’s
  [scope](cp-09-coherence.md); no Basket/shake, OCR/conversion/cloud, Apple-only actions, unsupported device signals
  or independently expanded activity queues. Preserve one recognizable design language.
- No technically imaginary global drag tracking, impossible desktop interception, fake focus behavior or
  unnecessary clutter. Accessibility/opaque fallback must remain possible. Material feasibility changes
  are shown to you for approval, never silently invented during coding.

## Owner deliverables and submission

- [ ] `cp-09__settings-navigation__dark__r01.png` — submitted folder.
- [ ] `cp-09__settings-privacy-plugins__light__r01.png` — submitted folder.
- [ ] `cp-09__core-entry-states__both__r01.png` — submitted folder.
- [ ] `cp-09__settings-and-entry-navigation__both__r01.png` — storyboards folder.
- [ ] Optionally save one alternate proposal in the alternatives folder, clearly named with a new revision.
- [ ] Name your preferred set/files and add short preferences. PNG recommended; JPEG/WebP with matching
  extension is supported. Aim below 2 MB per image; keep large originals local.
- [ ] Tell Codex: **“References ready for CP-09 in `review/cp-09-coherence/references/`. I prefer r01 [list any mixed revisions].
  Please open them and check completeness and feasibility.”** This submits them; it does not approve coding.
- [ ] After Codex shows the exact feasible selection, say **“I approve Gate A for CP-09, set r01, as listed,
  including the feasibility notes.”** Codex records your words, exact paths and hashes before visual coding.

After implementation, use [your personal tests](../../../owner/checkpoints/cp-09-coherence.md) to approve the actual app separately
(Gate B). Concepts are guidance, not pixel-perfect requirements or automatically licensed runtime assets.
