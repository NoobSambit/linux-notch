# CP-04 — owner visual-generation brief

## Purpose

Show four-mode shape, bounded settings and display policies while retaining CP-03’s chosen identity.

## Before generating

Wait until Codex activates this checkpoint after its prerequisites are approved. Use the Gate A/B CP-03 family/control captures listed by Codex at activation. Keep its semantic colors, type, spacing and radius roles; new geometry must be configurable and feasible on a layer-shell panel.
Codex lists exact prior approved sets/real-app captures in its activation message; if they are missing,
ask Codex to recover them before generating. Give your external image tool this whole brief and those
earlier images. Final palette/proportions are your selection, subject to feasibility and the approved scope.

## Required static images

Save all these files in **`review/cp-04-surfaces/references/submitted/`**.
Each row is one complete board, not one file per crop. Label crops clearly; use harmless sample content.

| Exact recommended filename | Required? | Canvas / treatment | Detailed composition, hierarchy, geometry, states and controls |
| --- | --- | --- | --- |
| `cp-04__top-mode-geometry__dark__r01.png` | Required | 1920 × 1080; dark | A top-edge desktop board with four labelled crops for Notch, Island, Dock and Hybrid, each showing compact and expanded boundaries at equal scale. Notch attaches and expands downward; Island has visible gap and a stable center/alignment anchor; Dock shows tasks plus small activity route; Hybrid keeps both parts reachable. Include width/height/alignment/offset/radius callouts and a safe maximum-size outline. Reuse CP-03 hierarchy/padding/icons; avoid overlapping reserved and expanded bounds. |
| `cp-04__bottom-mode-geometry__light__r01.png` | Required | 1920 × 1080; light | Corresponding bottom-edge crops in the approved light treatment; expansion grows upward into available space. Include long track title and large-text label so clipping is visible. Show reserve compact height versus overlay with the underlying app edge as a guide; Hybrid reservation choices are independent. Maintain identical semantic control spacing and corner family; do not rotate text. |
| `cp-04__display-fullscreen-settings__both__r01.png` | Required | 1600 × 1000; both | Two theme columns of a separate Surface/Display settings window: mode picker, edge, size/offset, reserve choice, preferred/focused monitor and fullscreen stay/explicit-overlay/hide controls with preview and safe reset. Include a two-display schematic with only one expanded owner and a disconnected preferred-display fallback. Primary hierarchy is current choice/preview, then recovery/help; control rows have consistent padding, focus and honest unavailable secondary display. No twelve equal tabs or independent queues. |

Preserve approved semantic color/type/icon/motion roles. Show compact/expanded relationships explicitly,
comfortable spacing and focus; dark/light must retain equivalent hierarchy. Dimensions above are reference
canvases, not hardcoded application sizes. Generated text may be approximate; Codex converts it into
real accessible controls rather than baking the board into the UI.

## Motion reference

Required file: **`review/cp-04-surfaces/references/storyboards/cp-04__mode-and-display-motion__both__r01.png`**.
Use a wide **1920 × 1080** board, with readable labelled frames in order and dark/light rows (or clearly
paired theme strips). Four major frames: attached compact Notch → detached Island at stable aligned anchor → Dock task row → Hybrid retaining task/activity. Add monitor-lost → view rehomed and fullscreen-hidden → explicit reveal panels. Label which bounds move/fade and when focus transfers after settling; no free-floating pointer-following or fake compositor windows. Add direct/fade reduced-motion equivalent. Mode 350–600 ms is a trial range only.

Optional individual keyframes use the same stem with `__frame-01`, `__frame-02`, etc. Optional video
uses the same stem with `.webm` or `.mp4` in this storyboard folder; a labelled PNG/WebP storyboard is
still mandatory. Video is local by default. These are proposed transitions; actual animation/focus/frame
behavior must be proven later by recording the running app. A static image alone proves no motion.

## Variants and revisions

No new identity alternatives. One geometry solution per supported edge plus configurable alignment examples is sufficient; optional alternative control layout goes in the alternatives folder with revision r02.
Alternatives belong in **`review/cp-04-surfaces/references/alternatives/`**, with `r02`, `r03`, etc. in the filename.
Use `review/cp-04-surfaces/references/NOTES.md` or a message to identify preferred files and what you like.
For a proposed replacement, put a new revision in submitted/storyboards; never overwrite approved images.
Codex preserves selected sets in `review/cp-04-surfaces/references/approved/rNN/` only after your explicit approval.

## Constraints

- Qt 6/QML/Quickshell, Wayland/Hyprland for v1; top/bottom supported, sides compatibility-only.
- No copied Apple/Droppy/k4 branding, exact proprietary pill, logos, artwork or unlicensed production assets.
  Use neutral placeholder app icons/content where rights are unknown.
- Stay inside [V1_SPEC](../../V1_SPEC.md), [UX_DIRECTION](../../UX_DIRECTION.md) and this checkpoint’s
  [scope](cp-04-surfaces.md); no Basket/shake, OCR/conversion/cloud, Apple-only actions, unsupported device signals
  or independently expanded activity queues. Preserve one recognizable design language.
- No technically imaginary global drag tracking, impossible desktop interception, fake focus behavior or
  unnecessary clutter. Accessibility/opaque fallback must remain possible. Material feasibility changes
  are shown to you for approval, never silently invented during coding.

## Owner deliverables and submission

- [ ] `cp-04__top-mode-geometry__dark__r01.png` — submitted folder.
- [ ] `cp-04__bottom-mode-geometry__light__r01.png` — submitted folder.
- [ ] `cp-04__display-fullscreen-settings__both__r01.png` — submitted folder.
- [ ] `cp-04__mode-and-display-motion__both__r01.png` — storyboards folder.
- [ ] Optionally save one alternate proposal in the alternatives folder, clearly named with a new revision.
- [ ] Name your preferred set/files and add short preferences. PNG recommended; JPEG/WebP with matching
  extension is supported. Aim below 2 MB per image; keep large originals local.
- [ ] Tell Codex: **“References ready for CP-04 in `review/cp-04-surfaces/references/`. I prefer r01 [list any mixed revisions].
  Please open them and check completeness and feasibility.”** This submits them; it does not approve coding.
- [ ] After Codex shows the exact feasible selection, say **“I approve Gate A for CP-04, set r01, as listed,
  including the feasibility notes.”** Codex records your words, exact paths and hashes before visual coding.

After implementation, use [your personal tests](../../../owner/checkpoints/cp-04-surfaces.md) to approve the actual app separately
(Gate B). Concepts are guidance, not pixel-perfect requirements or automatically licensed runtime assets.
