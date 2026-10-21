# CP-01 — Regression and safety gates

## WHAT YOU NEED TO DO NOW

Follow the current action on [Progress](../PROGRESS.md). Use this note when Codex activates this checkpoint; test only its supplied ready version.

## What are we building, and why?

Updates should preserve your settings and leave other desktop services alone. Safer startup/default handling and repeatable engineering checks; no new appearance is being designed.

## What must you provide?

No images. Allow a short test of fresh and copied settings in the isolated session; Codex handles setup.

**No visual reference generation required for this checkpoint.** It checks engineering/runtime behavior rather than choosing a new look. [Reference note](../../docs/workflow/checkpoints/cp-01-safety.visual.md). Actual screenshots belong in evidence below.

## What will Codex do?

Check updates against saved examples, fix unsafe startup choices and show that your settings and other desktop apps stay intact. Codex handles setup, technical checks, debugging, evidence, Git commits and a safe
Start/Stop/Restore handoff. You only test after Codex supplies a ready version labelled CP-01, its version
and evidence run. Expect the visible results in the checklist below; any remaining limitation must be listed.

## Your checklist

Report each ID as **PASS / FAIL / NOT TESTED / NEEDS HELP**. Current results are on [Progress](../PROGRESS.md).
You can send results in one short message; Codex records them for you.
All `run-01` paths below are first-run examples. Use the current run and exact save folder from Codex’s handoff; never overwrite an earlier run.
Missing equipment/software means **NOT TESTED — ENVIRONMENT LIMITATION** with a short reason.

| Test | What to check |
| --- | --- |
| M01 | Notifications coexist |
| M02 | Settings survive |
| M03 | Safe update and missing services |
| M04 | Return to last good |

### M01 — Notifications coexist

**Before starting:** Codex has prepared a separate notification test session and sample; no change to your everyday daemon.

**What to do:**

1. Leave the existing test notification app running.
2. Start a fresh test copy.
3. Send the harmless sample notification Codex prepared.
4. Restart the test copy.

**Expected result:** The existing notification app stays in control; Notchbar explains notification history is unavailable. Codex separately demonstrates Own when the test bus is free.

**Failure examples:** Other daemon stops, duplicate notices appear, or Notchbar claims to show its history.

**Evidence:** Screenshot of the notice and unavailable message. Save in `review/cp-01-safety/evidence/run-01/owner/` with test ID `M01`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M02 — Settings survive

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. In copied settings change one harmless option.
2. Restart.
3. Compare the chosen value and plugin enabled state.
4. Look at Codex’s fresh-copy comparison.

**Expected result:** Your copied settings survive; the fresh copy has Atalaya off and migrated copies retain their previous effective state.

**Failure examples:** Settings reset, plugin choice changes or two copies unexpectedly share settings.

**Evidence:** Before/after settings captures. Save in `review/cp-01-safety/evidence/run-01/owner/` with test ID `M02`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M03 — Safe update and missing services

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Watch Codex run the isolated restart demonstration.
2. Open a feature whose optional tool is missing.
3. Check a network feature with access disabled.

**Expected result:** Only the intended copy restarts; unavailable/offline features explain their state without freezing.

**Failure examples:** Unrelated copy closes or a missing tool breaks the whole surface.

**Evidence:** Short recording of the restart or unavailable screen. Save in `review/cp-01-safety/evidence/run-01/owner/` with test ID `M03`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M04 — Return to last good

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Use Stop.
2. Use Restore previous.
3. Open settings again.

**Expected result:** Previous version and matching settings return.

**Failure examples:** Personal desktop closes or previous settings are lost.

**Evidence:** Record which copy closed and the changed value. Save in `review/cp-01-safety/evidence/run-01/owner/` with test ID `M04`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

## If something goes wrong

Use Stop for CP-01; use Restore previous if needed. If either fails, follow [Quick recovery](../RECOVERY.md)
and tell Codex NEEDS HELP. Do not diagnose the code or run the installer yourself.

For the first test run save failures in **`review/cp-01-safety/evidence/run-01/owner/`**.
Name a screenshot **`cp-01__M01__short-problem__run-01.png`**; use the real test ID and `.webm`/`.mp4`
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
After the requested tests, tell Codex **“I approve CP-01 Gate B for version [SHA Codex supplies], [current run].
My requested tests passed.”** Name any untested case honestly; required gaps must be resolved before
approval is recorded. Or say **“Changes requested: CP-01 [test ID and problem].”**
Approval is only for the tested version. Codex records it and prepares the next eligible checkpoint;
it does not publish or replace your everyday desktop. [General testing guide](../TESTING.md).
