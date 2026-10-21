# Return to the tested candidate after M04

Primary tested revision remains **b114d5a1b8c3ed90e97b577e3424092a783e04ed**, run-05.
After the owner's M04 reply, the temporary original ff520e3 recovery copy was stopped and the candidate
was restored with its matching saved dummy state. The candidate was checked, then both private payloads
were stopped. Next Start selects b114d5a. This is agent technical proof, not a new owner approval.

## Actions and results

1. [Before record](m04-return-before.json): exact live original full ID/config/PID/start ticks,
   ff520e3 source and private context reverified. Host Quickshell, notification owner and personal
   k4 path-existence values recorded read-only.
2. [Original app stop](m04-return-original-app-stop.json): guarded full-instance stop, exit 0.
   [Original backup](m04-return-original-backup.json): while stopped, preserved all 12 post-M04
   original dummy-store files under `scratch/backups/cp-00-baseline/owner-after-m04-20261021-121127/`.
   Manifest revision is ff520e3; snapshot bytes and live stopped-store hashes matched exactly.
3. [Original session stop](m04-return-original-session-stop.txt): both exact private payloads stopped,
   exit 0. No stale private command sockets remained; no socket cleanup was needed during this return.
4. Candidate snapshot `owner-before-m04-20261021-120008` reverified against all 15 file hashes and
   its full b114d5a manifest revision. Source pinned to b114d5a while stopped, existing prepare and
   server/compositor start actions succeeded. No product/helper source changed.
5. [Private isolation probe](m04-return-candidate-isolation.json): exit 0, with no app running.
   [Candidate restore](m04-return-candidate-restore.json): existing runtime helper restored the
   matching candidate snapshot, verified exact prelaunch store hashes, retained a supplemental
   before-restore copy, and launched `/candidate/shell.qml`, exit 0.
6. [Settings verification](m04-return-candidate-settings.json): full b114d5a source/config/instance
   identity and restored `posicionBarra=abajo` checked; settings opened and rendered.
   [Launcher verification](m04-return-candidate-launcher.json): native launcher reopened and rendered.
   Agent did not claim to repeat the owner's keyboard actions.
7. [Live verification](m04-return-candidate-verification.json): full instance/config/PID/start ticks,
   private bus/socket/signature, compositor/server identities and output geometry recorded. Host
   HOME, parent display, host runtime/system bus and audio/input devices remain absent in the app context.
8. [Final Stop](m04-return-final-stop.txt): guarded app, compositor and server stop, exit 0.
   [Final state](m04-return-final-state.json): both recorded payloads absent, no stale private command
   sockets, selected revision b114d5a, saved edge abajo; host invariants match the before record.

The original `original-run03-complete` snapshot, the pre-M04 candidate snapshot and the post-M04
original snapshot all retain matching manifests and file hashes. Running the candidate briefly changed
only `.local/state/k4/partida.json` relative to its saved snapshot after launch; no claim that live game
state remains byte-identical is made. The strict prelaunch restore comparison passed and the immutable
candidate snapshot is unchanged. All other candidate saved store bytes still match.

## Actual captures and limitations

[Returned candidate settings](../application/cp-00__M04__return-candidate-settings__run-05.png) show
the b114d5a label and bottom island. [Returned launcher](../application/cp-00__M04__return-candidate-launcher__run-05.png)
shows its native view at the bottom edge. Both were opened and visually inspected. They are agent
return evidence, not retrospective owner M01/M03 images. [Capture provenance](m04-return-capture-inventory.json)
records timestamps, exact capture commands, source and SHA256.

All previous runs, results, images, failure logs and preparation records remain unchanged. The earlier
M04 stale-socket startup failure remains documented in its preparation; this successful return does
not erase it. No host desktop capture, clipboard read, config/service change or personal restore occurred.
Only synthetic allowlisted stores were restored. No dependencies, product changes, CP-01 or remote actions.

M01's owner image and a bar-visible M03 owner image remain unsupplied; physical dual-display is untested.
These limitations remain visible in progress and are not waived by this return. Gate B remains null;
the owner must make a separate explicit decision for CP-00 / b114d5a / run-05.

## Administrative verification

- `python3 tools/workflow.py --render`: exit 0; generated owner progress updated.
- `python3 tools/workflow.py --base-ref 0ba49ef`: exit 0; structural/history validation passes.
- `python3 tools/test_workflow.py`: exit 0; all 30 tests pass (5.945 seconds).
- `git diff --cached --check`: exit 0.
- Read-only assertions against 0ba49ef: exit 0; all prior evidence bytes, runs/tasks/authorization,
  preparation records and existing test histories retained; M01–M03 and later checkpoints unchanged.
  Both pinned source checkouts are clean; all three immutable snapshots match their manifests; new
  working/index evidence hashes and both screenshot hashes agree. Actual candidate source selection
  and stopped payloads reverified. Only administrative review/owner/progress paths changed.
  All four owner reports are PASS; status remains AWAITING OWNER TEST and Gate B null.
