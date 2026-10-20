# CP-04 — Four surface modes, geometry and displays

## WHAT YOU NEED TO DO NOW

Wait until Codex activates this checkpoint on [Progress](../PROGRESS.md). Do not generate files or test an unfinished version yet.

## What are we building, and why?

The surface should stay reachable when you change modes, screens or screen size. Notch, Island, Dock and Hybrid selection; top/bottom size/offset/reserve controls; monitor and fullscreen recovery.

## What must you provide?

Supply geometry/state boards and transition storyboard using CP-03’s approved look; test a second display only if available.

Yes, visual references are needed. Use [this complete brief](../../docs/workflow/checkpoints/cp-04-surfaces.visual.md). Static images go in `review/cp-04-surfaces/references/submitted/`; motion in `review/cp-04-surfaces/references/storyboards/`; extras in `review/cp-04-surfaces/references/alternatives/`. The brief lists every exact filename. Approve the selected feasible images before Codex changes the visual code.

## What will Codex do?

Implement bounded four-mode geometry and safe display/fullscreen behavior using the existing host and approved visual language. Codex handles setup, technical checks, debugging, evidence, Git commits and a safe
Start/Stop/Restore handoff. You only test after Codex supplies a ready version labelled CP-04, its version
and evidence run. Expect the visible results in the checklist below; any remaining limitation must be listed.

## Your checklist

Report each ID as **PASS / FAIL / NOT TESTED / NEEDS HELP**. Current results are on [Progress](../PROGRESS.md),
initially all NOT TESTED. You can send results in one short message; Codex records them for you.
Missing equipment/software means **NOT TESTED — ENVIRONMENT LIMITATION** with a short reason.

| Test | What to check |
| --- | --- |
| M01 | Modes and saved size |
| M02 | Reserved space |
| M03 | Fullscreen |
| M04 | Display disconnect |
| M05 | Large text and recovery |

### M01 — Modes and saved size

- **Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.
- **What to do:** 1. Select each of the four modes. 2. Try top then bottom. 3. Change size and offset within supplied limits. 4. Restart.
- **Expected result:** Chosen mode and size return; no clipping or unexplained jump; open work remains.
- **Failure examples:** Wrong mode after restart, clipped controls or lost plugin session.
- **Evidence:** Before/after whole-surface screenshots and settings value. Save in `review/cp-04-surfaces/evidence/run-01/owner/` with test ID `M01`.
- **Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M02 — Reserved space

- **Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.
- **What to do:** 1. Open a normal app window. 2. Switch reserve space on, then overlay. 3. Change between Dock and Hybrid.
- **Expected result:** App space changes only with the selected reserve choice; Hybrid parts remain reachable.
- **Failure examples:** Unwanted empty strip, hidden app controls or huge reflow.
- **Evidence:** Recording including app edges. Save in `review/cp-04-surfaces/evidence/run-01/owner/` with test ID `M02`.
- **Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M03 — Fullscreen

- **Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.
- **What to do:** 1. Put an app fullscreen on one display. 2. Try each prepared fullscreen policy. 3. Use the supplied reveal shortcut and leave fullscreen.
- **Expected result:** Only that display follows the policy; deliberate access works and the surface returns.
- **Failure examples:** Wrong monitor hides, typing is stolen or no recovery path.
- **Evidence:** Whole-screen recording naming policy and display. Save in `review/cp-04-surfaces/evidence/run-01/owner/` with test ID `M03`.
- **Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M04 — Display disconnect

- **Before starting:** A second physical/test display; Codex prepares the reversible test. Otherwise NOT TESTED — ENVIRONMENT LIMITATION.
- **What to do:** 1. Open a view on the second test display. 2. Disconnect that display as Codex instructs. 3. Use the view on the remaining display.
- **Expected result:** The active view and keyboard focus move safely; staged work remains.
- **Failure examples:** Offscreen view, duplicate expansion or lost focus.
- **Evidence:** Recording of both screens before removal and remaining screen afterward. Save in `review/cp-04-surfaces/evidence/run-01/owner/` with test ID `M04`.
- **Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M05 — Large text and recovery

- **Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.
- **What to do:** 1. Enable larger text and reduced motion. 2. Try the surface. 3. Watch Codex demonstrate invalid-size recovery using dummy settings.
- **Expected result:** No clipped labels or travel effects; a usable size returns after bad settings.
- **Failure examples:** Offscreen surface, lost settings or continued decorative motion.
- **Evidence:** Capture the size, text setting and recovery result. Save in `review/cp-04-surfaces/evidence/run-01/owner/` with test ID `M05`.
- **Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

## If something goes wrong

Use Stop for CP-04; use Restore previous if needed. If either fails, follow [Quick recovery](../RECOVERY.md)
and tell Codex NEEDS HELP. Do not diagnose the code or run the installer yourself.

For the first test run save failures in **`review/cp-04-surfaces/evidence/run-01/owner/`**.
Name a screenshot **`cp-04__M01__short-problem__run-01.png`**; use the real test ID and `.webm`/`.mp4`
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
After the requested tests, tell Codex **“I approve CP-04 Gate B for version [SHA Codex supplies], run-01.
My requested tests passed.”** Name any untested case honestly; required gaps must be resolved before
approval is recorded. Or say **“Changes requested: CP-04 [test ID and problem].”**
Approval is only for the tested version. Codex records it and prepares the next eligible checkpoint;
it does not publish or replace your everyday desktop. [General testing guide](../TESTING.md).
