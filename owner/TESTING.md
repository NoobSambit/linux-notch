# Test a checkpoint

## WHAT YOU NEED TO DO NOW

Check [Progress](PROGRESS.md). Test only when it identifies a ready checkpoint and Codex has supplied
its exact run, version and tested Start/Stop/Restore actions. CP-00 prepares the initial safe setup.
Do not run the inherited installer or replace your everyday bar to test this project.

## When Codex says a version is ready

1. Open [Progress](PROGRESS.md), then that checkpoint's personal note. Check the checkpoint number,
   test run and version Codex gives you. If they do not match, say **NEEDS HELP**.
2. Use the **Start CP-NN** action Codex supplies. Codex must give tested Start, Stop and Restore previous
   actions and show a labelled test terminal. You do not need to construct commands yourself.
3. Follow only the requested tests in that note. Each says what must be running, what to do,
   what to expect, signs of failure, what to capture and how to recover.
4. Report each test ID as **PASS**, **FAIL**, **NOT TESTED** or **NEEDS HELP**. You can send a short
   message such as “CP-04 M01 PASS; M03 FAIL; M04 NOT TESTED — ENVIRONMENT LIMITATION: one monitor.”
   Codex records the results; you do not need to edit technical files.
5. Use **Stop CP-NN** when done. If needed use **Restore previous**, supplied by Codex.
6. After all requested tests, approve the specific version or ask for changes using [Feedback](FEEDBACK.md).

Codex runs engineering checks and prepares dummy data. You check things a person can see or feel:
readability, focus, pointer behavior, clipping and motion. Never use real passwords or private files.
If a test needs a second display, battery/backlight, Bluetooth device, recorder or password manager,
Codex identifies it first. Missing equipment is **NOT TESTED — ENVIRONMENT LIMITATION**, never PASS.
Codex arranges another test or explains the required decision; you do not have to diagnose it.

## Capture a failure

Save screenshots or a short recording in the active checkpoint's exact folder. For example:
`review/cp-04-surfaces/evidence/run-01/owner/cp-04__M03__fullscreen-fail__run-01.png`.
Every personal note gives its own path and filename. Keep the test ID, use the current run supplied
by Codex, and use `.webm` or `.mp4` for video. If the app is frozen, a phone photo is fine; tell Codex
where it is saved. Avoid showing private notifications, documents or clipboard contents.

If anything freezes, follow [Quick recovery](RECOVERY.md). Do not run process-wide kill commands or
change personal settings to make a test pass. Codex investigates and gives you a corrected run to retest.
