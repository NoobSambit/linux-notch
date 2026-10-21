# CP-09 — Broader product and settings coherence

## WHAT YOU NEED TO DO NOW

Follow the current action on [Progress](../PROGRESS.md). Use this note when Codex activates this checkpoint; test only its supplied ready version.

## What are we building, and why?

Settings and everyday tools should be easy to find and feel like the same product. Settings grouped by intent; coherent launcher, controls, Own notification center and capture entry points, with honest privacy/plugin descriptions.

## What must you provide?

Supply settings and core-entry boards based on earlier approved references. Test normal navigation and a short inherited-tool smoke tour prepared by Codex.

Yes, visual references are needed. Use [this complete brief](../../docs/workflow/checkpoints/cp-09-coherence.visual.md). Static images go in `review/cp-09-coherence/references/submitted/`; motion in `review/cp-09-coherence/references/storyboards/`; extras in `review/cp-09-coherence/references/alternatives/`. The brief lists every exact filename. Approve the selected feasible images before Codex changes the visual code.

## What will Codex do?

Make settings and daily tools consistent and easy to find while preserving your saved choices and existing tools. Codex handles setup, technical checks, debugging, evidence, Git commits and a safe
Start/Stop/Restore handoff. You only test after Codex supplies a ready version labelled CP-09, its version
and evidence run. Expect the visible results in the checklist below; any remaining limitation must be listed.

## Your checklist

Report each ID as **PASS / FAIL / NOT TESTED / NEEDS HELP**. Current results are on [Progress](../PROGRESS.md).
You can send results in one short message; Codex records them for you.
All `run-01` paths below are first-run examples. Use the current run and exact save folder from Codex’s handoff; never overwrite an earlier run.
Missing equipment/software means **NOT TESTED — ENVIRONMENT LIMITATION** with a short reason.

| Test | What to check |
| --- | --- |
| M01 | Find and save settings |
| M02 | Everyday core tools |
| M03 | Capture and cancel |
| M04 | Inherited tools and missing dependencies |
| M05 | Reading and recovery |

### M01 — Find and save settings

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Search for mode, motion and clipboard options.
2. Change a harmless value.
3. Visit its other entry point.
4. Restart.

**Expected result:** Search reaches the right option; all entry points show the same saved value; previews agree.

**Failure examples:** Duplicate contradictory values, missing search result or reset after restart.

**Evidence:** Capture search term, value and restart result. Save in `review/cp-09-coherence/evidence/run-01/owner/` with test ID `M01`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M02 — Everyday core tools

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Open launcher, media, clipboard, Shelf and control center by prepared shortcuts.
2. Navigate by keyboard.
3. Open notifications in Own then External test sessions.

**Expected result:** Shared style/focus and predictable close behavior; External clearly says notification history is unavailable.

**Failure examples:** Mixed style, lost focus or fake notification history.

**Evidence:** Capture failing view and selected mode. Save in `review/cp-09-coherence/evidence/run-01/owner/` with test ID `M02`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M03 — Capture and cancel

**Before starting:** Codex prepares dummy capture content and confirms available capture tools.

**What to do:**

1. Open the capture entry.
2. Start selection then cancel.
3. Take one dummy capture.
4. If offered, send the resulting file to Shelf.

**Expected result:** Cancel returns safely; file destination remains; optional handoff references the correct saved file.

**Failure examples:** Hidden frozen selector, missing output or existing destination silently changed.

**Evidence:** Recording of selection/cancel or harmless capture path. Save in `review/cp-09-coherence/evidence/run-01/owner/` with test ID `M03`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M04 — Inherited tools and missing dependencies

**Before starting:** Codex selects installed supported-tool smoke cases; no real SSH/account credentials or session lock required without separate safe setup.

**What to do:**

1. Follow Codex’s short tool tour.
2. Open supported tools you use.
3. Inspect unavailable examples and plugin/privacy descriptions.

**Expected result:** Tools remain available; missing prerequisites say so; network controls and in-process plugin limits are understandable.

**Failure examples:** Removed tool, whole shell crash, silent network promise or claim of plugin sandboxing.

**Evidence:** Record tool name and message; avoid personal credentials. Save in `review/cp-09-coherence/evidence/run-01/owner/` with test ID `M04`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M05 — Reading and recovery

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Try larger text, keyboard focus and reduced motion in settings and core entries.
2. Use Stop and Restore previous.

**Expected result:** No clipping/trap; matching previous settings return safely.

**Failure examples:** Unreadable labels, decorative travel persists or wrong snapshot is restored.

**Evidence:** Capture failing view and restore result. Save in `review/cp-09-coherence/evidence/run-01/owner/` with test ID `M05`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

## If something goes wrong

Use Stop for CP-09; use Restore previous if needed. If either fails, follow [Quick recovery](../RECOVERY.md)
and tell Codex NEEDS HELP. Do not diagnose the code or run the installer yourself.

For the first test run save failures in **`review/cp-09-coherence/evidence/run-01/owner/`**.
Name a screenshot **`cp-09__M01__short-problem__run-01.png`**; use the real test ID and `.webm`/`.mp4`
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
After the requested tests, tell Codex **“I approve CP-09 Gate B for version [SHA Codex supplies], [current run].
My requested tests passed.”** Name any untested case honestly; required gaps must be resolved before
approval is recorded. Or say **“Changes requested: CP-09 [test ID and problem].”**
Approval is only for the tested version. Codex records it and prepares the next eligible checkpoint;
it does not publish or replace your everyday desktop. [General testing guide](../TESTING.md).
