# CP-10 — Compatibility, performance and release validation

## WHAT YOU NEED TO DO NOW

Follow the current action on [Progress](../PROGRESS.md). Use this note when Codex activates this checkpoint; test only its supplied ready version.

## What are we building, and why?

We need evidence that the whole product is safe and ready before sharing it. Release evidence, measured budgets, manual Hyprland dependency instructions and any separately reviewed fixes. No new visual direction.

## What must you provide?

No new concept images. Perform the final short daily-use checklist and decide whether the tested release candidate is acceptable. Publishing needs separate explicit permission.

**No visual reference generation required for this checkpoint.** It checks engineering/runtime behavior rather than choosing a new look. [Reference note](../../docs/workflow/checkpoints/cp-10-release.visual.md). Actual screenshots belong in evidence below.

## What will Codex do?

Check the whole candidate, measure resource use, review what can be distributed and demonstrate a safe return to the previous version. Codex handles setup, technical checks, debugging, evidence, Git commits and a safe
Start/Stop/Restore handoff. You only test after Codex supplies a ready version labelled CP-10, its version
and evidence run. Expect the visible results in the checklist below; any remaining limitation must be listed.

## Your checklist

Report each ID as **PASS / FAIL / NOT TESTED / NEEDS HELP**. Current results are on [Progress](../PROGRESS.md).
You can send results in one short message; Codex records them for you.
All `run-01` paths below are first-run examples. Use the current run and exact save folder from Codex’s handoff; never overwrite an earlier run.
Missing equipment/software means **NOT TESTED — ENVIRONMENT LIMITATION** with a short reason.

| Test | What to check |
| --- | --- |
| M01 | Daily workflow |
| M02 | Displays and fullscreen |
| M03 | Services and old tools |
| M04 | Comfort and responsiveness |
| M05 | Recovery and release decision |

### M01 — Daily workflow

**Before starting:** Candidate run/SHA and harmless music/files prepared by Codex; all prior required gates complete.

**What to do:**

1. Start candidate.
2. Play music/change volume.
3. Search/copy clipboard.
4. Stage/copy a dummy file.
5. Launch an app from Dock/Hybrid.
6. Restart.

**Expected result:** Activities restore, originals stay, tasks/settings persist and no view blocks daily work.

**Failure examples:** Data loss, stuck HUD, lost pins/settings or frozen shell.

**Evidence:** Recording naming the first failing step. Save in `review/cp-10-release/evidence/run-01/owner/` with test ID `M01`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M02 — Displays and fullscreen

**Before starting:** Second display/fractional-scale hardware when available; missing required coverage remains NOT TESTED — ENVIRONMENT LIMITATION.

**What to do:**

1. Try top/bottom and all modes.
2. Enter fullscreen and reveal.
3. If available disconnect/reconnect the preferred display.

**Expected result:** Correct display policy, no clipping, one expanded view and safe focus return.

**Failure examples:** Offscreen settings, wrong monitor hidden or duplicate expansion.

**Evidence:** Whole-screen video with monitor/scale details. Save in `review/cp-10-release/evidence/run-01/owner/` with test ID `M02`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M03 — Services and old tools

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Watch Codex demonstrate notification modes and restart safely.
2. Open supported tools you use and a supplied old plugin.
3. Review missing-dependency states.

**Expected result:** Existing daemon is respected; old plugins/tools work or honestly show missing prerequisites.

**Failure examples:** Daemon replaced, removed feature, crash or stale actions.

**Evidence:** Capture mode/tool/plugin and the failed action. Save in `review/cp-10-release/evidence/run-01/owner/` with test ID `M03`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M04 — Comfort and responsiveness

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Use the candidate for the short workload Codex prepares.
2. Try larger text and keyboard navigation.
3. Enable reduced motion.
4. Leave it idle.

**Expected result:** Readable, reachable controls and calm transitions; no obvious sustained stutter or heat increase. Codex supplies actual measurements.

**Failure examples:** Keyboard trap, unreadable text, persistent animation or sustained lag.

**Evidence:** Short recording and describe when lag/heat starts. Save in `review/cp-10-release/evidence/run-01/owner/` with test ID `M04`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M05 — Recovery and release decision

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Use Stop and Restore previous.
2. Confirm settings return.
3. Read the short list of remaining limitations and included/excluded assets.
4. Approve or request corrections for the candidate SHA.

**Expected result:** Recovery works; limitations are explicit; nothing is published just because you approve testing.

**Failure examples:** Wrong version, lost settings, unresolved core test or unclear distribution rights.

**Evidence:** Capture restore result and name any limitation you do not accept. Save in `review/cp-10-release/evidence/run-01/owner/` with test ID `M05`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

## If something goes wrong

Use Stop for CP-10; use Restore previous if needed. If either fails, follow [Quick recovery](../RECOVERY.md)
and tell Codex NEEDS HELP. Do not diagnose the code or run the installer yourself.

For the first test run save failures in **`review/cp-10-release/evidence/run-01/owner/`**.
Name a screenshot **`cp-10__M01__short-problem__run-01.png`**; use the real test ID and `.webm`/`.mp4`
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
After the requested tests, tell Codex **“I approve CP-10 Gate B for version [SHA Codex supplies], [current run].
My requested tests passed.”** Name any untested case honestly; required gaps must be resolved before
approval is recorded. Or say **“Changes requested: CP-10 [test ID and problem].”**
Approval is only for the tested version. Codex records it and prepares the next eligible checkpoint;
it does not publish or replace your everyday desktop. [General testing guide](../TESTING.md).
