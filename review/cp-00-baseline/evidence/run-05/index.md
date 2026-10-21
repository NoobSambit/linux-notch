# CP-00 owner-testing handoff — run-05

Primary clean tested revision: **b114d5a1b8c3ed90e97b577e3424092a783e04ed**.
Branch checkpoint/cp-00-baseline. Original recovery:
ff520e33e136bbce11b7100c69888dedf42f7273.

Engineering is ready for M01–M04. Gate B is not recorded. Stop at CP-00.
The final evidence commit also corrects a synthetic workflow-test fixture; runtime behavior is unchanged.

## Environment

Arch 7.2.8; Qt 6.11.2; Quickshell 0.2.1/7511545; Hyprland 0.56.2;
i7-13700HX / Intel UHD 770 rendering. Synthetic C.UTF-8/UTC session; inherited dark theme and no personal wallpaper. CP00-STABLE is a private headless
1280x720/60 Hz/scale 1 output, mirrored into the nested aquamarine window.
The small Hyprland debug-start banner is expected in this isolated debugging session.
A second virtual output was tested; a second physical display was unavailable.

Independent bubblewrap mount/user/PID/IPC/network contexts, synthetic /home/cp00,
private no-activation bus/runtime/clipboard/capture and read-only independent Git checkouts.
Only render nodes and the compositor's single parent display connection are shared.
The app cannot reach host HOME, parent socket, host compositor IPC/bus, system bus,
network, audio/input/camera/DRM-card devices or credentials. Audio uses silent VLC adummy.

## Your actions

From /home/noobsambit/Documents/k4-main:

    python3 tools/cp00.py start
    python3 tools/cp00.py stop
    python3 tools/cp00.py restore

Start prints the CP-00/source label and opens the nested test desktop; next Start selects b114d5a.
Keep that labelled terminal available. Stop checks full instance ID/config/PID/start time/session.
Restore previous closes the candidate and launches original ff520e3 with its matching
original-run03-complete dummy snapshot, retaining current dummy state and verifying checksums.
It never restores personal data. After checking recovery, ask Codex to return to the candidate.

Follow [M01–M04](../../../../owner/checkpoints/cp-00-baseline.md):

1. **M01:** Start, check the label, Stop, then use an everyday app on your normal desktop.
2. **M02:** Start and run demo below. Try launcher/settings, media pause/resume, clipboard and screenshot.
3. **M03:** Settings → Island: try top/bottom. Optional helpers below affect only dummy windows/displays.
4. **M04:** Ask Codex to demonstrate Restore previous; check the restored launcher/settings.

    python3 tools/cp00.py demo
    python3 tools/cp00.py fullscreen true
    python3 tools/cp00.py fullscreen false
    python3 tools/cp00.py view-second
    python3 tools/cp00.py view-first

Demo supplies two dummy documents, local music and harmless text. It is intentionally silent.
All actions were rehearsed. For problems give test ID and what happened; Codex handles diagnosis.
Report PASS / FAIL / NOT TESTED / NEEDS HELP. Physical/device cases remain honestly untested.

After your requested tests, explicitly approve Gate B for the primary SHA above and run-05,
or request changes. Until then M01–M04 remain NOT TESTED and CP-00 is not APPROVED.

## Evidence and recovery

- [Gates](automated/gates.json): inherited checks, real local qmllint/ffmpeg, 30 workflow and 14 control regressions.
- [Scenario observations](automated/baseline-report.md), [capture inventory](automated/capture-inventory.json).
- [Resource baseline](automated/performance-summary.md): 3 startup and 24 ten-second samples.
- [Recovery](automated/recovery.md), [source integrity](automated/source-integrity.json),
  [diff review](automated/diff-review.md), [completion audit](automated/completion-audit.md).
- [Rights inventory](automated/asset-inventory.json): 157 hashed paths; no rights clearance implied.

Exact commands/return values are in commands.json and run05-copyable-*.txt. Historical full IDs,
PID/start ticks, bus/socket/config/source live in recovery-check.json and restored-previous-handle.json.
**All test payloads are stopped.** Start produces fresh guarded identities.

Ignored immutable snapshots remain under scratch/backups/cp-00-baseline/. The original dummy-only
snapshot is also reconstructible from run-04/automated/recovery-fixture.json. No personal store was copied.
Captures are actual original k4; no visual references or concepts are required/generated.
Qt profiling/viewport failures and the initial workflow-fixture failure remain retained.
No live configuration, dependency installation, personal restore, push or publication occurred.
