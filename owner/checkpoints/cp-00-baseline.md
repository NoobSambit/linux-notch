# CP-00 — Safe environment and original k4 baseline

## WHAT YOU NEED TO DO NOW

First approve the workflow and authorize CP-00 only, using the message in [Start here](../README.md). No test copy is ready yet.

## What are we building, and why?

We need to know what already works and be able to stop a failed test without disturbing your desktop. Only a separate test setup, baseline captures and recovery instructions. Your everyday desktop is not replaced.

## What must you provide?

Explicitly approve this workflow and authorize CP-00 only. Codex will check available test-session options and ask only if a real session action is needed.

**No visual reference generation required for this checkpoint.** It checks engineering/runtime behavior rather than choosing a new look. [Reference note](../../docs/workflow/checkpoints/cp-00-baseline.visual.md). Actual screenshots belong in evidence below.

## What will Codex do?

Establish a reproducible, isolated original-k4 baseline and a rehearsed recovery path before changing product behavior. Codex handles setup, technical checks, debugging, evidence, Git commits and a safe
Start/Stop/Restore handoff. You only test after Codex supplies a ready version labelled CP-00, its version
and evidence run. Expect the visible results in the checklist below; any remaining limitation must be listed.

## Your checklist

Report each ID as **PASS / FAIL / NOT TESTED / NEEDS HELP**. Current results are on [Progress](../PROGRESS.md),
initially all NOT TESTED. You can send results in one short message; Codex records them for you.
Missing equipment/software means **NOT TESTED — ENVIRONMENT LIMITATION** with a short reason.

| Test | What to check |
| --- | --- |
| M01 | Start and stop safely |
| M02 | Original everyday paths |
| M03 | Screen and fullscreen baseline |
| M04 | Recovery rehearsal |

### M01 — Start and stop safely

- **Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.
- **What to do:** 1. Use Start CP-00 supplied by Codex. 2. Check the test label. 3. Use Stop CP-00. 4. Open an everyday app on your usual desktop.
- **Expected result:** Only the test version closes; your usual desktop and notification app still work.
- **Failure examples:** Both bars stop, personal settings change, or the desktop stops responding.
- **Evidence:** Photo or screenshot of the label and affected desktop; tell Codex which action failed. Save in `review/cp-00-baseline/evidence/run-01/owner/` with test ID `M01`.
- **Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M02 — Original everyday paths

- **Before starting:** Test session, dummy music/text and a safe capture target prepared by Codex.
- **What to do:** 1. Open the test launcher and settings. 2. Play a dummy/local music track. 3. Copy harmless text and open clipboard. 4. Try the supplied small capture sample.
- **Expected result:** Codex records what currently works and any existing failures; no redesign is expected.
- **Failure examples:** Missing entry point, frozen view, lost keyboard focus or capture does not finish.
- **Evidence:** Capture the failing view and the step; avoid real clipboard secrets. Save in `review/cp-00-baseline/evidence/run-01/owner/` with test ID `M02`.
- **Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M03 — Screen and fullscreen baseline

- **Before starting:** Codex has prepared reversible placement choices; a second display is needed only for that part.
- **What to do:** 1. In the test desktop try top and bottom. 2. Open an app fullscreen, then leave fullscreen. 3. If a second test display exists, repeat there.
- **Expected result:** Current behavior is captured; known problems and unavailable display cases are recorded honestly.
- **Failure examples:** Surface stays offscreen, blocks typing or never returns.
- **Evidence:** One whole-screen capture with monitor arrangement and chosen edge. Save in `review/cp-00-baseline/evidence/run-01/owner/` with test ID `M03`.
- **Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M04 — Recovery rehearsal

- **Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.
- **What to do:** 1. Ask Codex to demonstrate Restore previous. 2. Open settings and launcher in the restored test copy.
- **Expected result:** The original captured version returns with its matching dummy settings.
- **Failure examples:** Only the broken candidate launches, or settings vanish.
- **Evidence:** Record what reopened and which setting differs. Save in `review/cp-00-baseline/evidence/run-01/owner/` with test ID `M04`.
- **Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

## If something goes wrong

Use Stop for CP-00; use Restore previous if needed. If either fails, follow [Quick recovery](../RECOVERY.md)
and tell Codex NEEDS HELP. Do not diagnose the code or run the installer yourself.

For the first test run save failures in **`review/cp-00-baseline/evidence/run-01/owner/`**.
Name a screenshot **`cp-00__M01__short-problem__run-01.png`**; use the real test ID and `.webm`/`.mp4`
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
After the requested tests, tell Codex **“I approve CP-00 Gate B for version [SHA Codex supplies], run-01.
My requested tests passed.”** Name any untested case honestly; required gaps must be resolved before
approval is recorded. Or say **“Changes requested: CP-00 [test ID and problem].”**
Approval is only for the tested version. Codex records it and prepares the next eligible checkpoint;
it does not publish or replace your everyday desktop. [General testing guide](../TESTING.md).
