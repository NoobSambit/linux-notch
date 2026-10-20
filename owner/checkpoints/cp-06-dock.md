# CP-06 — Dock and Hybrid polish

## WHAT YOU NEED TO DO NOW

Wait until Codex activates this checkpoint on [Progress](../PROGRESS.md). Do not generate files or test an unfinished version yet.

## What are we building, and why?

Your pinned apps and open windows should remain easy to reach across mode changes. Dock hierarchy, pin/reorder/focus/drawer feedback and Hybrid transitions; expressive travel stays optional.

## What must you provide?

Supply dock/task states and mode-transition storyboard derived from previous approved visuals.

Yes, visual references are needed. Use [this complete brief](../../docs/workflow/checkpoints/cp-06-dock.visual.md). Static images go in `review/cp-06-dock/references/submitted/`; motion in `review/cp-06-dock/references/storyboards/`; extras in `review/cp-06-dock/references/alternatives/`. The brief lists every exact filename. Approve the selected feasible images before Codex changes the visual code.

## What will Codex do?

Polish the existing dock, preserve your pinned apps and make mode changes brief and comfortable. Codex handles setup, technical checks, debugging, evidence, Git commits and a safe
Start/Stop/Restore handoff. You only test after Codex supplies a ready version labelled CP-06, its version
and evidence run. Expect the visible results in the checklist below; any remaining limitation must be listed.

## Your checklist

Report each ID as **PASS / FAIL / NOT TESTED / NEEDS HELP**. Current results are on [Progress](../PROGRESS.md),
initially all NOT TESTED. You can send results in one short message; Codex records them for you.
Missing equipment/software means **NOT TESTED — ENVIRONMENT LIMITATION** with a short reason.

| Test | What to check |
| --- | --- |
| M01 | Pins and order |
| M02 | Tasks, drawer and Hybrid |
| M03 | Transition and desktop input |
| M04 | Motion and scale |

### M01 — Pins and order

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Pin a prepared app.
2. Reorder it.
3. Switch to Notch and back.
4. Restart.
5. Unpin it using keyboard controls.

**Expected result:** Pin and order survive; keyboard action is reachable; unpin works.

**Failure examples:** Missing/duplicate pin, changed order or keyboard cannot reach action.

**Evidence:** Before/after dock captures. Save in `review/cp-06-dock/evidence/run-01/owner/` with test ID `M01`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M02 — Tasks, drawer and Hybrid

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Open two windows of the test app.
2. Use dock preview/focus.
3. Open the drawer and launch another test app.
4. In Hybrid open music controls.

**Expected result:** Correct windows focus; drawer launches; tasks remain reachable beside activity.

**Failure examples:** Wrong window, stuck drawer or activity removes dock access.

**Evidence:** Recording including the app titles. Save in `review/cp-06-dock/evidence/run-01/owner/` with test ID `M02`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M03 — Transition and desktop input

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Switch modes repeatedly.
2. Cancel/reverse mid-transition using the supplied action.
3. Click and type in another app.
4. Try reserve/overlay and fullscreen.

**Expected result:** Modes settle predictably; no invisible window blocks input or wrong-screen reflow.

**Failure examples:** Click blocker, duplicate surface or stuck in-between shape.

**Evidence:** Whole-screen recording including a failed click/type. Save in `review/cp-06-dock/evidence/run-01/owner/` with test ID `M03`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M04 — Motion and scale

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Try normal shorter transition.
2. Try optional expressive transition.
3. Enable reduced motion.
4. Read long app labels at larger text/scale.

**Expected result:** Default is brief; expressive is opt-in; reduced motion removes travel; labels and focus fit.

**Failure examples:** Always-slow travel, clipped labels or motion continues when reduced.

**Evidence:** Recording and capture with text/scale setting. Save in `review/cp-06-dock/evidence/run-01/owner/` with test ID `M04`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

## If something goes wrong

Use Stop for CP-06; use Restore previous if needed. If either fails, follow [Quick recovery](../RECOVERY.md)
and tell Codex NEEDS HELP. Do not diagnose the code or run the installer yourself.

For the first test run save failures in **`review/cp-06-dock/evidence/run-01/owner/`**.
Name a screenshot **`cp-06__M01__short-problem__run-01.png`**; use the real test ID and `.webm`/`.mp4`
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
After the requested tests, tell Codex **“I approve CP-06 Gate B for version [SHA Codex supplies], run-01.
My requested tests passed.”** Name any untested case honestly; required gaps must be resolved before
approval is recorded. Or say **“Changes requested: CP-06 [test ID and problem].”**
Approval is only for the tested version. Codex records it and prepares the next eligible checkpoint;
it does not publish or replace your everyday desktop. [General testing guide](../TESTING.md).
