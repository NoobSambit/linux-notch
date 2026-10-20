# CP-05 — Host Activity Policy and interactions

## WHAT YOU NEED TO DO NOW

Wait until Codex activates this checkpoint on [Progress](../PROGRESS.md). Do not generate files or test an unfinished version yet.

## What are we building, and why?

Brief changes such as volume should not interrupt your work or leave stale popups behind. Consistent media/HUD/recording/status behavior, hover/click/keyboard rules and honest notification modes.

## What must you provide?

Supply activity states and a media → volume → media storyboard; test music, dummy notices and a short safe recording.

Yes, visual references are needed. Use [this complete brief](../../docs/workflow/checkpoints/cp-05-activities.visual.md). Static images go in `review/cp-05-activities/references/submitted/`; motion in `review/cp-05-activities/references/storyboards/`; extras in `review/cp-05-activities/references/alternatives/`. The brief lists every exact filename. Approve the selected feasible images before Codex changes the visual code.

## What will Codex do?

Make brief indicators appear and return correctly, keep recording controls reachable and check that the surface does not steal your typing. Codex handles setup, technical checks, debugging, evidence, Git commits and a safe
Start/Stop/Restore handoff. You only test after Codex supplies a ready version labelled CP-05, its version
and evidence run. Expect the visible results in the checklist below; any remaining limitation must be listed.

## Your checklist

Report each ID as **PASS / FAIL / NOT TESTED / NEEDS HELP**. Current results are on [Progress](../PROGRESS.md),
initially all NOT TESTED. You can send results in one short message; Codex records them for you.
Missing equipment/software means **NOT TESTED — ENVIRONMENT LIMITATION** with a short reason.

| Test | What to check |
| --- | --- |
| M01 | Music and volume return |
| M02 | Keep typing and dismiss |
| M03 | Hover and recording stop |
| M04 | Notifications and real signals |
| M05 | Modes and reduced motion |

### M01 — Music and volume return

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Start the dummy music track.
2. Change volume several times.
3. Wait.
4. Repeat, then stop music while the indicator is visible.

**Expected result:** Volume updates briefly; playing music returns, stopped music does not reappear.

**Failure examples:** Stuck volume display, stale track or repeated old popups.

**Evidence:** Recording including music state and volume changes. Save in `review/cp-05-activities/evidence/run-01/owner/` with test ID `M01`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M02 — Keep typing and dismiss

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Open the launcher by its test shortcut.
2. Type a search while Codex sends routine sample events.
3. Press Escape.
4. Try click-outside with its setting on and off.

**Expected result:** Typing stays in the launcher; closing order follows the chosen setting; dismissed views do not reopen from old events.

**Failure examples:** Typing moves elsewhere, clicks are swallowed unexpectedly or a closed view returns.

**Evidence:** Recording with keys used and chosen click-outside setting. Save in `review/cp-05-activities/evidence/run-01/owner/` with test ID `M02`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M03 — Hover and recording stop

**Before starting:** Dummy capture target and recorder ready; use no personal content. Codex supplies an independent stop fallback.

**What to do:**

1. Type in another app while briefly hovering the surface.
2. Open the preview deliberately.
3. Start a short dummy recording.
4. Change volume and open another view, then stop recording.

**Expected result:** Casual hover never steals typing; preview is reachable; recording and its stop action remain reachable.

**Failure examples:** Focus is stolen, preview closes before you reach it or stop disappears.

**Evidence:** Video showing pointer and recording indicator. Save in `review/cp-05-activities/evidence/run-01/owner/` with test ID `M03`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M04 — Notifications and real signals

**Before starting:** Codex prepares both notification environments and safe test signals; no real low-battery drain or network disruption required.

**What to do:**

1. In Own mode use the supplied sample notice and action.
2. In External mode repeat.
3. Review prepared battery/network/Bluetooth samples.

**Expected result:** Own supports its notice/history/action; External clearly says unavailable and leaves the other daemon alone; unsupported signals say so.

**Failure examples:** Fake mirrored history, lost daemon, invented brightness/camera state or stuck alert.

**Evidence:** Capture the selected mode and affected message. Save in `review/cp-05-activities/evidence/run-01/owner/` with test ID `M04`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M05 — Modes and reduced motion

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Repeat a volume interruption in each mode.
2. Enable reduced motion.
3. Open/close a view and return from fullscreen.

**Expected result:** Dock keeps apps primary with activity reachable; other modes restore content calmly; reduced motion removes travel.

**Failure examples:** Lost dock tasks, wobble, flicker or stale overlay.

**Evidence:** Short recording naming mode and motion setting. Save in `review/cp-05-activities/evidence/run-01/owner/` with test ID `M05`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

## If something goes wrong

Use Stop for CP-05; use Restore previous if needed. If either fails, follow [Quick recovery](../RECOVERY.md)
and tell Codex NEEDS HELP. Do not diagnose the code or run the installer yourself.

For the first test run save failures in **`review/cp-05-activities/evidence/run-01/owner/`**.
Name a screenshot **`cp-05__M01__short-problem__run-01.png`**; use the real test ID and `.webm`/`.mp4`
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
After the requested tests, tell Codex **“I approve CP-05 Gate B for version [SHA Codex supplies], run-01.
My requested tests passed.”** Name any untested case honestly; required gaps must be resolved before
approval is recorded. Or say **“Changes requested: CP-05 [test ID and problem].”**
Approval is only for the tested version. Codex records it and prepares the next eligible checkpoint;
it does not publish or replace your everyday desktop. [General testing guide](../TESTING.md).
