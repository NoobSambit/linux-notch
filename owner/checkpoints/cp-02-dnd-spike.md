# CP-02 — Isolated Shelf drag-and-drop feasibility

## WHAT YOU NEED TO DO NOW

Wait until Codex activates this checkpoint on [Progress](../PROGRESS.md). Do not generate files or test an unfinished version yet.

## What are we building, and why?

We must prove files can enter and leave safely before building the Shelf. A disposable test target only. It will look plain and will not be added to your product.

## What must you provide?

No concept images. Use two available common file managers in the test session; Codex checks versions and prepares harmless files. Missing apps are recorded, not installed silently.

**No visual reference generation required for this checkpoint.** It checks engineering/runtime behavior rather than choosing a new look. [Reference note](../../docs/workflow/checkpoints/cp-02-dnd-spike.visual.md). Actual screenshots belong in evidence below.

## What will Codex do?

Build a plain temporary drop target and test real file transfers, then explain clearly whether the planned Shelf can work safely. Codex handles setup, technical checks, debugging, evidence, Git commits and a safe
Start/Stop/Restore handoff. You only test after Codex supplies a ready version labelled CP-02, its version
and evidence run. Expect the visible results in the checklist below; any remaining limitation must be listed.

## Your checklist

Report each ID as **PASS / FAIL / NOT TESTED / NEEDS HELP**. Current results are on [Progress](../PROGRESS.md),
initially all NOT TESTED. You can send results in one short message; Codex records them for you.
Missing equipment/software means **NOT TESTED — ENVIRONMENT LIMITATION** with a short reason.

| Test | What to check |
| --- | --- |
| M01 | Drop files in and out |
| M02 | Cancel and keep originals |
| M03 | Missing file and keyboard route |
| M04 | Screens and decision |

### M01 — Drop files in and out

**Before starting:** Two file managers, plain isolated target and dummy source/destination folders prepared by Codex.

**What to do:**

1. In the first file manager drag a dummy file, a folder, then two files onto the plain test target.
2. Drag them out into the prepared destination.
3. Repeat with the second file manager.

**Expected result:** Target accepts the correct items and destination receives copies; originals remain.

**Failure examples:** Wrong item count, lost originals, empty destination or no accepted drag.

**Evidence:** Short recording identifying the file manager and item type. Save in `review/cp-02-dnd-spike/evidence/run-01/owner/` with test ID `M01`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M02 — Cancel and keep originals

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Start a drag and press Escape before dropping.
2. Repeat with a requested move using Codex’s prepared controls.
3. Look at the original folder.

**Expected result:** Canceled items are not added; unsafe moves are refused or safely negotiated as documented copy; originals stay.

**Failure examples:** A canceled item remains or source disappears.

**Evidence:** Recording of pointer and both folders; tell Codex which modifier you pressed. Save in `review/cp-02-dnd-spike/evidence/run-01/owner/` with test ID `M02`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M03 — Missing file and keyboard route

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Ask Codex to remove a dummy source after staging.
2. Try its action.
3. Add another dummy file using only the supplied keyboard route.

**Expected result:** Missing item explains the problem; keyboard route works without dragging.

**Failure examples:** Frozen target, silent failure or keyboard cannot reach the action.

**Evidence:** Screenshot of missing-file message or keyboard focus. Save in `review/cp-02-dnd-spike/evidence/run-01/owner/` with test ID `M03`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M04 — Screens and decision

**Before starting:** Second display needed for crossing only; otherwise record NOT TESTED — ENVIRONMENT LIMITATION.

**What to do:**

1. If a second test display exists, drag between screens.
2. Review Codex’s short GO/RESCOPE report.

**Expected result:** No lost drop or stuck target; untested screens are labelled. A limitation is explained before any Shelf design begins.

**Failure examples:** Cross-screen drop loses data or report hides an untested required case.

**Evidence:** Whole-screen recording and the source/destination display names. Save in `review/cp-02-dnd-spike/evidence/run-01/owner/` with test ID `M04`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

## If something goes wrong

Use Stop for CP-02; use Restore previous if needed. If either fails, follow [Quick recovery](../RECOVERY.md)
and tell Codex NEEDS HELP. Do not diagnose the code or run the installer yourself.

For the first test run save failures in **`review/cp-02-dnd-spike/evidence/run-01/owner/`**.
Name a screenshot **`cp-02__M01__short-problem__run-01.png`**; use the real test ID and `.webm`/`.mp4`
for video. Codex supplies a new run number after fixes, so old failures are kept.

```text
Test / run:
What happened:
What should have happened:
Screenshot/video:
Can you reproduce it? Yes / No / Sometimes
```

## How to approve

There is no image-approval step here.
After the requested tests, tell Codex **“I approve CP-02 Gate B for version [SHA Codex supplies], run-01.
My requested tests passed.”** Name any untested case honestly; required gaps must be resolved before
approval is recorded. Or say **“Changes requested: CP-02 [test ID and problem].”**
Approval is only for the tested version. Codex records it and prepares the next eligible checkpoint;
it does not publish or replace your everyday desktop. [General testing guide](../TESTING.md).
