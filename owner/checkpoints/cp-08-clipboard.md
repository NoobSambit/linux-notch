# CP-08 — Clipboard and file-workflow polish

## WHAT YOU NEED TO DO NOW

Wait until Codex activates this checkpoint on [Progress](../PROGRESS.md). Do not generate files or test an unfinished version yet.

## What are we building, and why?

Copied text and images should be quick to find and clear to distinguish from staged files. Readable clipboard previews, search and selection feedback, pinning and sensitive-content explanations; file offers only if proven reliable.

## What must you provide?

Supply text/image/pinned/empty/error boards in the shared style. Use harmless secret-like samples prepared by Codex, never real passwords.

Yes, visual references are needed. Use [this complete brief](../../docs/workflow/checkpoints/cp-08-clipboard.visual.md). Static images go in `review/cp-08-clipboard/references/submitted/`; motion in `review/cp-08-clipboard/references/storyboards/`; extras in `review/cp-08-clipboard/references/alternatives/`. The brief lists every exact filename. Approve the selected feasible images before Codex changes the visual code.

## What will Codex do?

Improve text and image history, search and pins, test sensitive-copy limits and add file support only if it proves reliable. Codex handles setup, technical checks, debugging, evidence, Git commits and a safe
Start/Stop/Restore handoff. You only test after Codex supplies a ready version labelled CP-08, its version
and evidence run. Expect the visible results in the checklist below; any remaining limitation must be listed.

## Your checklist

Report each ID as **PASS / FAIL / NOT TESTED / NEEDS HELP**. Current results are on [Progress](../PROGRESS.md),
initially all NOT TESTED. You can send results in one short message; Codex records them for you.
Missing equipment/software means **NOT TESTED — ENVIRONMENT LIMITATION** with a short reason.

| Test | What to check |
| --- | --- |
| M01 | Find text and images |
| M02 | Keyboard and pins |
| M03 | Honest sensitive-copy behavior |
| M04 | Files versus plain paths |
| M05 | Errors and reading comfort |

### M01 — Find text and images

**Before starting:** Dummy text/image and destination prepared in the isolated session.

**What to do:**

1. Copy harmless text, then the supplied sample image.
2. Open clipboard.
3. Search for the text.
4. Copy/paste each item into the test destination.

**Expected result:** Types are easy to distinguish; search finds the text; pasted contents match.

**Failure examples:** Wrong item/type, unreadable preview or image fails to paste.

**Evidence:** Capture the preview/search and harmless paste. Save in `review/cp-08-clipboard/evidence/run-01/owner/` with test ID `M01`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M02 — Keyboard and pins

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Open by shortcut and search without the mouse.
2. Select an item, pin it and restart.
3. Copy it, unpin it and close with Escape.

**Expected result:** Search has focus, selection is visible and pin survives; focus returns after close.

**Failure examples:** Invisible selection, lost pin or typing goes to another app.

**Evidence:** Recording with key sequence. Save in `review/cp-08-clipboard/evidence/run-01/owner/` with test ID `M02`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M03 — Honest sensitive-copy behavior

**Before starting:** Codex prepares a test password manager; if unavailable record NOT TESTED — ENVIRONMENT LIMITATION.

**What to do:**

1. Follow Codex’s test-password-manager demo using a made-up token.
2. Open history.
3. Read the sensitive-copy explanation.

**Expected result:** Supported concealed-copy cases are absent as demonstrated; wording describes tested limits, not perfect protection. Codex checks hidden storage too.

**Failure examples:** Test token appears despite an exclusion claim, or text promises all passwords are blocked.

**Evidence:** Report which dummy test failed; avoid capturing any real secret. Save in `review/cp-08-clipboard/evidence/run-01/owner/` with test ID `M03`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M04 — Files versus plain paths

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. Copy a dummy file from the proven file manager if file support was accepted.
2. Compare with copied plain path text.
3. Ask Codex to remove the dummy source and try the action.

**Expected result:** True file offer is clearly distinguished; missing source explains failure. If support was deferred, the checklist states that decision and text/image still work.

**Failure examples:** Plain text mislabelled as a file, invented action or silent failure.

**Evidence:** Capture harmless offer/type and missing-source result. Save in `review/cp-08-clipboard/evidence/run-01/owner/` with test ID `M04`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

### M05 — Errors and reading comfort

**Before starting:** The labelled test version and its Start/Stop/Restore instructions are ready.

**What to do:**

1. View empty search and prepared unavailable/broken-image example.
2. Try larger text and reduced motion.
3. Restart and inspect history.

**Expected result:** Messages explain next steps; previews fit and stored entries remain as intended.

**Failure examples:** Blank frozen panel, clipped text or lost history.

**Evidence:** Capture state, text size and result after restart. Save in `review/cp-08-clipboard/evidence/run-01/owner/` with test ID `M05`.

**Recovery:** Use Stop for this checkpoint; ask Codex to restore the previous test version.

## If something goes wrong

Use Stop for CP-08; use Restore previous if needed. If either fails, follow [Quick recovery](../RECOVERY.md)
and tell Codex NEEDS HELP. Do not diagnose the code or run the installer yourself.

For the first test run save failures in **`review/cp-08-clipboard/evidence/run-01/owner/`**.
Name a screenshot **`cp-08__M01__short-problem__run-01.png`**; use the real test ID and `.webm`/`.mp4`
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
After the requested tests, tell Codex **“I approve CP-08 Gate B for version [SHA Codex supplies], run-01.
My requested tests passed.”** Name any untested case honestly; required gaps must be resolved before
approval is recorded. Or say **“Changes requested: CP-08 [test ID and problem].”**
Approval is only for the tested version. Codex records it and prepares the next eligible checkpoint;
it does not publish or replace your everyday desktop. [General testing guide](../TESTING.md).
