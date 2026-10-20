# CP-08 — owner visual-generation brief

## Purpose

Make existing text/image history searchable and readable while visually separating true file offers from plain text paths.

## Before generating

Wait until Codex activates this checkpoint after its prerequisites are approved. Use accepted shared tokens/input/focus and CP-07 small-action conventions. Current watcher/store remains; true file offers are conditional, not guaranteed by the artwork.
Codex lists exact prior approved sets/real-app captures in its activation message; if they are missing,
ask Codex to recover them before generating. Give your external image tool this whole brief and those
earlier images. Final palette/proportions are your selection, subject to feasibility and the approved scope.

## Required static images

Save all these files in **`review/cp-08-clipboard/references/submitted/`**.
Each row is one complete board, not one file per crop. Label crops clearly; use harmless sample content.

| Exact recommended filename | Required? | Canvas / treatment | Detailed composition, hierarchy, geometry, states and controls |
| --- | --- | --- | --- |
| `cp-08__clipboard-text-search__dark__r01.png` | Required | 1600 × 1000; dark | Expanded clipboard with focused search input, text results with first-line title and secondary age/size only where known, selected row, pin marker, copy feedback and keyboard hint. Include long/multiline text preview that wraps/truncates predictably without huge cards; compact entry shows count/type hint. Shared dark surface, padding, row spacing, radius/type hierarchy and visible focus; no invented source-app provenance or tags. |
| `cp-08__clipboard-images-pins__light__r01.png` | Required | 1600 × 1000; light | Same layout in approved light material: distinct image thumbnail and text rows, clear pinned section/marker, chosen image preview with known size and copy/delete actions. Keep search first, content second, metadata quiet, equal hit areas and small consistent card geometry. Include a broken-image placeholder that does not collapse the row and a larger-text narrow crop. Do not make image thumbnails the entire surface. |
| `cp-08__clipboard-empty-secret-file__both__r01.png` | Required | 1600 × 1000; both | Dark/light columns: empty/no-result, history unavailable, honest concealed-copy explanation and conditional true file offer with missing-source state. Show plain copied path text separately from a real file item; conditional panel is labelled “only if MIME proof succeeds”. No password value appears; use harmless explanatory placeholder. Keep recovery/help below primary message, shared focus/disabled/warning roles and small action spacing. |

Preserve approved semantic color/type/icon/motion roles. Show compact/expanded relationships explicitly,
comfortable spacing and focus; dark/light must retain equivalent hierarchy. Dimensions above are reference
canvases, not hardcoded application sizes. Generated text may be approximate; Codex converts it into
real accessible controls rather than baking the board into the UI.

## Motion reference

Required file: **`review/cp-08-clipboard/references/storyboards/cp-08__clipboard-entry-feedback__both__r01.png`**.
Use a wide **1920 × 1080** board, with readable labelled frames in order and dark/light rows (or clearly
paired theme strips). Four frames per theme: compact entry → expanded search with focus → selected result/copied feedback → closed with focus returned. Add pin feedback without large travel and image decode placeholder → loaded image without layout jump. Bounds stay at the CP-04 anchor; typing focus only follows deliberate open; reduced motion changes/fades directly. No bouncing lists or invented watcher/source animation.

Optional individual keyframes use the same stem with `__frame-01`, `__frame-02`, etc. Optional video
uses the same stem with `.webm` or `.mp4` in this storyboard folder; a labelled PNG/WebP storyboard is
still mandatory. Video is local by default. These are proposed transitions; actual animation/focus/frame
behavior must be proven later by recording the running app. A static image alone proves no motion.

## Variants and revisions

One text/image system; omit conditional file panel from implementation if MIME proof fails. Optional tighter row density in alternatives/r02, no new organizing taxonomy.
Alternatives belong in **`review/cp-08-clipboard/references/alternatives/`**, with `r02`, `r03`, etc. in the filename.
Use `review/cp-08-clipboard/references/NOTES.md` or a message to identify preferred files and what you like.
For a proposed replacement, put a new revision in submitted/storyboards; never overwrite approved images.
Codex preserves selected sets in `review/cp-08-clipboard/references/approved/rNN/` only after your explicit approval.

## Constraints

- Qt 6/QML/Quickshell, Wayland/Hyprland for v1; top/bottom supported, sides compatibility-only.
- No copied Apple/Droppy/k4 branding, exact proprietary pill, logos, artwork or unlicensed production assets.
  Use neutral placeholder app icons/content where rights are unknown.
- Stay inside [V1_SPEC](../../V1_SPEC.md), [UX_DIRECTION](../../UX_DIRECTION.md) and this checkpoint’s
  [scope](cp-08-clipboard.md); no Basket/shake, OCR/conversion/cloud, Apple-only actions, unsupported device signals
  or independently expanded activity queues. Preserve one recognizable design language.
- No technically imaginary global drag tracking, impossible desktop interception, fake focus behavior or
  unnecessary clutter. Accessibility/opaque fallback must remain possible. Material feasibility changes
  are shown to you for approval, never silently invented during coding.

## Owner deliverables and submission

- [ ] `cp-08__clipboard-text-search__dark__r01.png` — submitted folder.
- [ ] `cp-08__clipboard-images-pins__light__r01.png` — submitted folder.
- [ ] `cp-08__clipboard-empty-secret-file__both__r01.png` — submitted folder.
- [ ] `cp-08__clipboard-entry-feedback__both__r01.png` — storyboards folder.
- [ ] Optionally save one alternate proposal in the alternatives folder, clearly named with a new revision.
- [ ] Name your preferred set/files and add short preferences. PNG recommended; JPEG/WebP with matching
  extension is supported. Aim below 2 MB per image; keep large originals local.
- [ ] Tell Codex: **“References ready for CP-08 in `review/cp-08-clipboard/references/`. I prefer r01 [list any mixed revisions].
  Please open them and check completeness and feasibility.”** This submits them; it does not approve coding.
- [ ] After Codex shows the exact feasible selection, say **“I approve Gate A for CP-08, set r01, as listed,
  including the feasibility notes.”** Codex records your words, exact paths and hashes before visual coding.

After implementation, use [your personal tests](../../../owner/checkpoints/cp-08-clipboard.md) to approve the actual app separately
(Gate B). Concepts are guidance, not pixel-perfect requirements or automatically licensed runtime assets.
