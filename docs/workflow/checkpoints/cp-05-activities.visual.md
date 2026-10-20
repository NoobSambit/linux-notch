# CP-05 — owner visual-generation brief

## Purpose

Visualize compact persistent status, transient interruption and deliberate views so one host can implement predictable activity behavior.

## Before generating

Wait until Codex activates this checkpoint after its prerequisites are approved. Use CP-03 colors/type/controls and CP-04 mode anchors. Copy no vendor HUDs; content priority follows ARCHITECTURE’s existing-host policy. Dock keeps apps primary.
Codex lists exact prior approved sets/real-app captures in its activation message; if they are missing,
ask Codex to recover them before generating. Give your external image tool this whole brief and those
earlier images. Final palette/proportions are your selection, subject to feasibility and the approved scope.

## Required static images

Save all these files in **`review/cp-05-activities/references/submitted/`**.
Each row is one complete board, not one file per crop. Label crops clearly; use harmless sample content.

| Exact recommended filename | Required? | Canvas / treatment | Detailed composition, hierarchy, geometry, states and controls |
| --- | --- | --- | --- |
| `cp-05__media-volume-states__both__r01.png` | Required | 1600 × 1000; both | Matched dark/light columns with compact media, expanded media and temporary volume HUD at the same anchor. Media hierarchy: artwork, title/artist, transport/seek; compact retains only the useful hint. Volume has readable icon, level/mute and bounded progress, with no unrelated controls. Keep geometry/padding/icon sizes from CP-03 and demonstrate long title truncation. Include a small Dock activity route without replacing task icons. |
| `cp-05__recording-user-status__both__r01.png` | Required | 1600 × 1000; both | In each theme show recording badge/elapsed time and reachable stop while launcher/user file view owns expanded content. Include a critical battery alert with explicit dismissal and Wi-Fi/Bluetooth status using real-signal labels; unavailable brightness is labelled rather than invented. Prioritize user typing/focus and stop safety over decoration, visible focus ring and non-color recording cue. Keep cards compact with clear spacing; no camera/microphone universal-monitor promises. |
| `cp-05__notification-intent-states__both__r01.png` | Required | 1600 × 1000; both | Own-mode notice with source, short body, action and close; alongside External/off unavailable-history explanation and a link to mode settings. Below show hover preview versus deliberately opened keyboard-search view: passive preview has no keyboard-focus claim; user view has visible focus, ESC/close affordance. Same radius/material/type roles and text/action hierarchy in both themes. Include coalesced repeated event indicator without a stale popup queue. |

Preserve approved semantic color/type/icon/motion roles. Show compact/expanded relationships explicitly,
comfortable spacing and focus; dark/light must retain equivalent hierarchy. Dimensions above are reference
canvases, not hardcoded application sizes. Generated text may be approximate; Codex converts it into
real accessible controls rather than baking the board into the UI.

## Motion reference

Required file: **`review/cp-05-activities/references/storyboards/cp-05__media-volume-restore__both__r01.png`**.
Use a wide **1920 × 1080** board, with readable labelled frames in order and dark/light rows (or clearly
paired theme strips). Six labelled frames per theme: playing media → volume arrives → repeated update in same HUD → expiry → current media restored → media stopped while HUD active, so idle returns instead. Add user launcher open with event hidden/expired and recording badge staying anchored throughout. Boundaries morph in place, contents fade without moving user focus; no replay after dismissal. Include reduced-motion direct/fade path. Real timing is later measured, not proven by these frames.

Optional individual keyframes use the same stem with `__frame-01`, `__frame-02`, etc. Optional video
uses the same stem with `.webm` or `.mp4` in this storyboard folder; a labelled PNG/WebP storyboard is
still mandatory. Video is local by default. These are proposed transitions; actual animation/focus/frame
behavior must be proven later by recording the running app. A static image alone proves no motion.

## Variants and revisions

One consistent policy sequence, no competing priority systems. Optional alternate HUD arrangement in the alternatives folder with revision r02 only if the same hierarchy/stop visibility is preserved.
Alternatives belong in **`review/cp-05-activities/references/alternatives/`**, with `r02`, `r03`, etc. in the filename.
Use `review/cp-05-activities/references/NOTES.md` or a message to identify preferred files and what you like.
For a proposed replacement, put a new revision in submitted/storyboards; never overwrite approved images.
Codex preserves selected sets in `review/cp-05-activities/references/approved/rNN/` only after your explicit approval.

## Constraints

- Qt 6/QML/Quickshell, Wayland/Hyprland for v1; top/bottom supported, sides compatibility-only.
- No copied Apple/Droppy/k4 branding, exact proprietary pill, logos, artwork or unlicensed production assets.
  Use neutral placeholder app icons/content where rights are unknown.
- Stay inside [V1_SPEC](../../V1_SPEC.md), [UX_DIRECTION](../../UX_DIRECTION.md) and this checkpoint’s
  [scope](cp-05-activities.md); no Basket/shake, OCR/conversion/cloud, Apple-only actions, unsupported device signals
  or independently expanded activity queues. Preserve one recognizable design language.
- No technically imaginary global drag tracking, impossible desktop interception, fake focus behavior or
  unnecessary clutter. Accessibility/opaque fallback must remain possible. Material feasibility changes
  are shown to you for approval, never silently invented during coding.

## Owner deliverables and submission

- [ ] `cp-05__media-volume-states__both__r01.png` — submitted folder.
- [ ] `cp-05__recording-user-status__both__r01.png` — submitted folder.
- [ ] `cp-05__notification-intent-states__both__r01.png` — submitted folder.
- [ ] `cp-05__media-volume-restore__both__r01.png` — storyboards folder.
- [ ] Optionally save one alternate proposal in the alternatives folder, clearly named with a new revision.
- [ ] Name your preferred set/files and add short preferences. PNG recommended; JPEG/WebP with matching
  extension is supported. Aim below 2 MB per image; keep large originals local.
- [ ] Tell Codex: **“References ready for CP-05 in `review/cp-05-activities/references/`. I prefer r01 [list any mixed revisions].
  Please open them and check completeness and feasibility.”** This submits them; it does not approve coding.
- [ ] After Codex shows the exact feasible selection, say **“I approve Gate A for CP-05, set r01, as listed,
  including the feasibility notes.”** Codex records your words, exact paths and hashes before visual coding.

After implementation, use [your personal tests](../../../owner/checkpoints/cp-05-activities.md) to approve the actual app separately
(Gate B). Concepts are guidance, not pixel-perfect requirements or automatically licensed runtime assets.
