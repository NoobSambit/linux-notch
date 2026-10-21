# CP-06 — owner visual-generation brief

## Purpose

Refine the existing dock task hierarchy and mode transitions while retaining shared surface identity and stable pins.

## Before generating

Wait until Codex activates this checkpoint after its prerequisites are approved. Use CP-03 controls/materials, CP-04 geometry and CP-05 compact activity affordance. Existing Dual task behavior remains; this is not a new dock product.
Codex lists exact prior approved sets/real-app captures in its activation message; if they are missing,
ask Codex to recover them before generating. Give your external image tool this whole brief and those
earlier images. Final palette/proportions are your selection, subject to feasibility and the approved scope.

## Required static images

Save all these files in **`review/cp-06-dock/references/submitted/`**.
Each row is one complete board, not one file per crop. Label crops clearly; use harmless sample content.

| Exact recommended filename | Required? | Canvas / treatment | Detailed composition, hierarchy, geometry, states and controls |
| --- | --- | --- | --- |
| `cp-06__dock-task-states__dark__r01.png` | Required | 1920 × 900; dark | Bottom dock with 6–8 generic legally usable app icons; pinned/running distinction, two-window marker, focused/hovered/pressed item and visible keyboard focus. Above it, a small window-preview group and app title, anchored to the correct task. Show reorder insertion marker and a labelled pin/unpin action. Keep consistent icon optical weight, inter-item gaps and hit areas; task navigation is primary and activity route secondary. Include a small top-edge inset using the same grammar. |
| `cp-06__hybrid-activity__light__r01.png` | Required | 1920 × 900; light | Hybrid desktop crop showing task row and compact media/recording affordance together. Expanded activity must leave tasks reachable and maintain one expanded owner. Show underlying app window edge to explain independent reservation/overlay choices; light material uses approved contrast/elevation. Do not paste the dark dock into light mode. Preserve pin order and type/radius roles, clear space between parts with no giant decorative rail. |
| `cp-06__drawer-and-unavailable__both__r01.png` | Required | 1600 × 1000; both | Dark/light columns: dock drawer with search focus, app grid/list consistent with launcher and empty/no-result message; window preview unavailable state plus long app labels. Show focused item, disabled action and feedback. Content hierarchy is search, result/app name, supporting status; shared spacing/padding and bounded width/height fit a laptop. No new marketplace/store controls. |

Preserve approved semantic color/type/icon/motion roles. Show compact/expanded relationships explicitly,
comfortable spacing and focus; dark/light must retain equivalent hierarchy. Dimensions above are reference
canvases, not hardcoded application sizes. Generated text may be approximate; Codex converts it into
real accessible controls rather than baking the board into the UI.

## Motion reference

Required file: **`review/cp-06-dock/references/storyboards/cp-06__notch-island-dock-hybrid__both__r01.png`**.
Use a wide **1920 × 1080** board, with readable labelled frames in order and dark/light rows (or clearly
paired theme strips). Four settled states plus intermediate collapse/reform frames for Notch → Island → Dock → Hybrid. Label source/destination anchors, task continuity and when activity fades/reappears. Default travel is brief; optional expressive inherited journey may be a small annotated alternative, not the default. Include reversal/cancel settling and reduced-motion direct/fade version. No invisible fullscreen input catcher; indicate clickable task regions through the transition.

Optional individual keyframes use the same stem with `__frame-01`, `__frame-02`, etc. Optional video
uses the same stem with `.webm` or `.mp4` in this storyboard folder; a labelled PNG/WebP storyboard is
still mandatory. Video is local by default. These are proposed transitions; actual animation/focus/frame
behavior must be proven later by recording the running app. A static image alone proves no motion.

## Variants and revisions

One default dock treatment; optional expressive-motion storyboard is the only extra concept requested. Reuse established pins/task semantics.
Alternatives belong in **`review/cp-06-dock/references/alternatives/`**, with `r02`, `r03`, etc. in the filename.
Use `review/cp-06-dock/references/NOTES.md` or a message to identify preferred files and what you like.
For a proposed replacement, put a new revision in submitted/storyboards; never overwrite approved images.
Codex preserves selected sets in `review/cp-06-dock/references/approved/rNN/` only after your explicit approval.

## Constraints

- Qt 6/QML/Quickshell, Wayland/Hyprland for v1; top/bottom supported, sides compatibility-only.
- No copied Apple/Droppy/k4 branding, exact proprietary pill, logos, artwork or unlicensed production assets.
  Use neutral placeholder app icons/content where rights are unknown.
- Stay inside [V1_SPEC](../../V1_SPEC.md), [UX_DIRECTION](../../UX_DIRECTION.md) and this checkpoint’s
  [scope](cp-06-dock.md); no Basket/shake, OCR/conversion/cloud, Apple-only actions, unsupported device signals
  or independently expanded activity queues. Preserve one recognizable design language.
- No technically imaginary global drag tracking, impossible desktop interception, fake focus behavior or
  unnecessary clutter. Accessibility/opaque fallback must remain possible. Material feasibility changes
  are shown to you for approval, never silently invented during coding.

## Owner deliverables and submission

- [ ] `cp-06__dock-task-states__dark__r01.png` — submitted folder.
- [ ] `cp-06__hybrid-activity__light__r01.png` — submitted folder.
- [ ] `cp-06__drawer-and-unavailable__both__r01.png` — submitted folder.
- [ ] `cp-06__notch-island-dock-hybrid__both__r01.png` — storyboards folder.
- [ ] Optionally save one alternate proposal in the alternatives folder, clearly named with a new revision.
- [ ] Name your preferred set/files and add short preferences. PNG recommended; JPEG/WebP with matching
  extension is supported. Aim below 2 MB per image; keep large originals local.
- [ ] Tell Codex: **“References ready for CP-06 in `review/cp-06-dock/references/`. I prefer r01 [list any mixed revisions].
  Please open them and check completeness and feasibility.”** This submits them; it does not approve coding.
- [ ] After Codex shows the exact feasible selection, say **“I approve Gate A for CP-06, set r01, as listed,
  including the feasibility notes.”** Codex records your words, exact paths and hashes before visual coding.

After implementation, use [your personal tests](../../../owner/checkpoints/cp-06-dock.md) to approve the actual app separately
(Gate B). Concepts are guidance, not pixel-perfect requirements or automatically licensed runtime assets.
