# CP-03 — Shared design system and original visual direction

## WHAT YOU NEED TO DO NOW

Follow the current action on [Progress](../PROGRESS.md). Use this note when Codex activates this checkpoint; test only its supplied ready version.

## What are we building, and why?

All later screens need one clear, recognizable appearance. Shared colors, type, spacing, shapes, focus and motion; first application to core surfaces, settings navigation and dock examples.

## What must you provide?

Generate the required boards in the linked brief, choose a direction, then approve the exact feasible set. This is the first visual-generation checkpoint, after the Shelf decision.

Yes, visual references are needed. Use [this complete brief](../../docs/workflow/checkpoints/cp-03-design-system.visual.md). Static images go in `review/cp-03-design-system/references/submitted/`; motion in `review/cp-03-design-system/references/storyboards/`; extras in `review/cp-03-design-system/references/alternatives/`. The brief lists every exact filename. Approve the selected feasible images before Codex changes the visual code.

## What will Codex do?

Use your chosen images to build shared colors, text, shapes and controls, then show you the real results in both themes. Codex handles setup, technical checks, debugging, evidence, Git commits and a safe
Start/Stop/Restore handoff. You only test after Codex supplies a ready version labelled CP-03, its version
and evidence run. Expect the visible results in the checklist below; any remaining limitation must be listed.

## Your checklist

Report each ID as **PASS / FAIL / NOT TESTED / NEEDS HELP**. Current results are on [Progress](../PROGRESS.md).
You can send results in one short message; Codex records them for you.
All `run-01` paths below are first-run examples. Use the current run and exact save folder from Codex’s handoff; never overwrite an earlier run.
Missing equipment/software means **NOT TESTED — ENVIRONMENT LIMITATION** with a short reason.

| Test | What to check |
| --- | --- |
| M01 | One visual family |
| M02 | Keyboard and states |
| M03 | Reading and background |
| M04 | Motion comfort |

### M01 — One visual family

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Compare Notch, Island, Dock, Hybrid and settings samples with your selected boards.
2. Switch between dark and light.

**Expected result:** Type, spacing, icons and materials feel related; settings stays a separate window.

**Failure examples:** Unapproved visual change, mixed styles, unreadable labels or clipped controls.

**Evidence:** Capture the mismatching sample and name the approved image. Save in `review/cp-03-design-system/evidence/run-01/owner/` with test ID `M01`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M02 — Keyboard and states

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Put the mouse aside.
2. Tab through sample controls.
3. Activate a button and change a slider.
4. Inspect disabled/error samples.

**Expected result:** Focus is easy to see; controls have readable labels and states do not rely only on color.

**Failure examples:** Invisible focus, keyboard trap or selected/disabled states look identical.

**Evidence:** Screenshot showing focus, or a short recording of the trapped key sequence. Save in `review/cp-03-design-system/evidence/run-01/owner/` with test ID `M02`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M03 — Reading and background

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Use Codex’s larger-text setting.
2. View a long-label sample.
3. Try busy/light wallpaper and the opaque fallback.

**Expected result:** Text remains readable and no content overlaps or clips.

**Failure examples:** Low contrast, missing glyph, cropped label or unreadable blur.

**Evidence:** Capture whole sample and chosen text size/background. Save in `review/cp-03-design-system/evidence/run-01/owner/` with test ID `M03`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M04 — Motion comfort

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Open and close the sample.
2. Enable reduced motion.
3. Repeat.

**Expected result:** Normal motion is calm; reduced motion keeps the same information with no decorative travel.

**Failure examples:** Wobble, flicker, lost controls or continued decorative motion.

**Evidence:** Short recording with normal and reduced-motion labels. Save in `review/cp-03-design-system/evidence/run-01/owner/` with test ID `M04`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

## If something goes wrong

Use Stop for CP-03; use Restore previous if needed. If either fails, follow [Quick recovery](../RECOVERY.md)
and tell Codex NEEDS HELP. Do not diagnose the code or run the installer yourself.

For the first test run save failures in **`review/cp-03-design-system/evidence/run-01/owner/`**.
Name a screenshot **`cp-03__M01__short-problem__run-01.png`**; use the real test ID and `.webm`/`.mp4`
for video. Codex supplies a new run number after fixes, so old failures are kept.

```text
Test / run:
What happened:
What should have happened:
Screenshot/video:
Can you reproduce it? Yes / No / Sometimes
```

## How to approve

Your earlier image approval is Gate A; it does not approve the app.
After the requested tests, tell Codex **“I approve CP-03 Gate B for version [SHA Codex supplies], [current run].
My requested tests passed.”** Name any untested case honestly; required gaps must be resolved before
approval is recorded. Or say **“Changes requested: CP-03 [test ID and problem].”**
Approval is only for the tested version. Codex records it and prepares the next eligible checkpoint;
it does not publish or replace your everyday desktop. [General testing guide](../TESTING.md).
