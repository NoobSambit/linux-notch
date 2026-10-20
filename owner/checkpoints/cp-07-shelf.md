# CP-07 — Local Shelf implementation

## WHAT YOU NEED TO DO NOW

Wait until Codex activates this checkpoint on [Progress](../PROGRESS.md). Do not generate files or test an unfinished version yet.

## What are we building, and why?

Files can wait in one place while you move between apps, without moving the originals. Visible Shelf target, staged file cards, drag-out and keyboard actions, pin/retention and missing-file feedback.

## What must you provide?

Generate Shelf states and approach/open/collapse storyboard; use only dummy files during tests.

Yes, visual references are needed. Use [this complete brief](../../docs/workflow/checkpoints/cp-07-shelf.visual.md). Static images go in `review/cp-07-shelf/references/submitted/`; motion in `review/cp-07-shelf/references/storyboards/`; extras in `review/cp-07-shelf/references/alternatives/`. The brief lists every exact filename. Approve the selected feasible images before Codex changes the visual code.

## What will Codex do?

Build a local place to stage file references, prove originals stay safe and provide the same useful actions with the keyboard. Codex handles setup, technical checks, debugging, evidence, Git commits and a safe
Start/Stop/Restore handoff. You only test after Codex supplies a ready version labelled CP-07, its version
and evidence run. Expect the visible results in the checklist below; any remaining limitation must be listed.

## Your checklist

Report each ID as **PASS / FAIL / NOT TESTED / NEEDS HELP**. Current results are on [Progress](../PROGRESS.md),
initially all NOT TESTED. You can send results in one short message; Codex records them for you.
Missing equipment/software means **NOT TESTED — ENVIRONMENT LIMITATION** with a short reason.

| Test | What to check |
| --- | --- |
| M01 | Stage and copy onward |
| M02 | Cancel, remove and clear |
| M03 | Use actions without dragging |
| M04 | Restart and missing source |
| M05 | Approach and display comfort |

### M01 — Stage and copy onward

**Before starting:** Codex prepares dummy source/destination and the two CP-02-tested file managers.

**What to do:**

1. Drag a file, a folder and multiple dummy files into Shelf from the proven file managers.
2. Drag one into the destination app.
3. Check originals.

**Expected result:** Correct cards/count appear; destination gets copies; original paths remain.

**Failure examples:** Wrong count, source moved/deleted or stuck drag.

**Evidence:** Recording showing source, Shelf and destination. Save in `review/cp-07-shelf/evidence/run-01/owner/` with test ID `M01`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M02 — Cancel, remove and clear

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Start a drag then press Escape.
2. Remove one staged card.
3. Clear the remaining unpinned cards using the confirmation shown.
4. Check source folder.

**Expected result:** Cancel adds nothing; remove/clear only remove staging entries; originals stay.

**Failure examples:** Original deletion, canceled entry added or unclear destructive wording.

**Evidence:** Video of confirmation and original folder. Save in `review/cp-07-shelf/evidence/run-01/owner/` with test ID `M02`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M03 — Use actions without dragging

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Open Shelf by the supplied shortcut.
2. Add a dummy path using the keyboard route.
3. Select open, reveal and copy path.
4. Press Escape.

**Expected result:** Actions reach the right dummy file/folder; copied path is correct; focus returns safely.

**Failure examples:** Wrong file opens, path is corrupted or keyboard is trapped.

**Evidence:** Capture selected action and harmless pasted path. Save in `review/cp-07-shelf/evidence/run-01/owner/` with test ID `M03`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M04 — Restart and missing source

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Stage two items and pin one.
2. Restart.
3. Ask Codex to remove/move one dummy source or deny its access.
4. Try its action.

**Expected result:** Retention follows the documented choice; pinned state survives; missing/unreadable item explains the problem and disables unsafe actions.

**Failure examples:** Silent empty action, lost pin or source copied into hidden storage without explanation.

**Evidence:** Before/after cards and missing/unavailable message. Save in `review/cp-07-shelf/evidence/run-01/owner/` with test ID `M04`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M05 — Approach and display comfort

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Drag toward the surface then away.
2. Open/collapse Shelf normally and with reduced motion.
3. Try fullscreen/reveal and second display if available.

**Expected result:** Drop target is clear; no global overlay steals other drops; Shelf stays reachable with readable cards.

**Failure examples:** Blocked desktop drops, clipping, stuck expansion or excessive travel.

**Evidence:** Recording naming mode, display and motion setting. Save in `review/cp-07-shelf/evidence/run-01/owner/` with test ID `M05`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

## If something goes wrong

Use Stop for CP-07; use Restore previous if needed. If either fails, follow [Quick recovery](../RECOVERY.md)
and tell Codex NEEDS HELP. Do not diagnose the code or run the installer yourself.

For the first test run save failures in **`review/cp-07-shelf/evidence/run-01/owner/`**.
Name a screenshot **`cp-07__M01__short-problem__run-01.png`**; use the real test ID and `.webm`/`.mp4`
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
After the requested tests, tell Codex **“I approve CP-07 Gate B for version [SHA Codex supplies], run-01.
My requested tests passed.”** Name any untested case honestly; required gaps must be resolved before
approval is recorded. Or say **“Changes requested: CP-07 [test ID and problem].”**
Approval is only for the tested version. Codex records it and prepares the next eligible checkpoint;
it does not publish or replace your everyday desktop. [General testing guide](../TESTING.md).
