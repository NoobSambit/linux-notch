# M04 preparation — run-05 recovery rehearsal

Owner request in this thread: “what to do in the last test”. This prepares the existing M04
Restore previous test from the [frozen handoff](../index.md). Current status is authoritative only in
[progress.json](../../../../../docs/workflow/progress.json); no owner M04 result or Gate B is granted here.

Primary tested candidate remains **b114d5a1b8c3ed90e97b577e3424092a783e04ed**, unchanged.
For this recovery check only, the running test copy is the original
**ff520e33e136bbce11b7100c69888dedf42f7273**, with its matching original dummy snapshot.
This original recovery target was already part of run-05; it is not a new product revision or test run.

## Your last check

Open the nested **aquamarine** window. The restored native launcher is already open.

1. Type `vlc` to check launcher search responds, then press **Esc**.
2. Right-click the top-centre island → **Ajustes → Island**. Check settings opens normally.
   The small revision label should say **ff520e3**. The island should be back at **Arriba** (top).
   That reset from M03's bottom position is intentional: it comes from the original matching snapshot.
3. Close settings with **Esc** and check the test desktop still responds.

Report **M04 PASS / FAIL / NOT TESTED / NEEDS HELP**, with what reopened and any unexpected setting.
No restore command or code work is needed from you; Codex already demonstrated the guarded restore.
Stop the test when needed, from `/home/noobsambit/Documents/k4-main`:

```sh
python3 tools/cp00.py stop
```

After your report, Codex will return the disposable copy to the preserved b114d5a candidate and its
matching test state. Gate B remains a separate explicit decision for b114d5a / run-05. Do not approve
the temporary ff520e3 recovery copy as a replacement candidate.

## Candidate preservation and actual restore

Before preparation, both recorded test payloads were stopped. The [before record](../automated/m04-before.json)
inventories the candidate's allowlisted dummy stores and unchanged host invariants.
An immutable, correctly revision-labelled candidate snapshot is preserved at:

`scratch/backups/cp-00-baseline/owner-before-m04-20261021-120008/`

Its manifest revision is b114d5a and all **15** stored file hashes match the pre-M04 candidate inventory.
This includes the dummy settings, enabled/per-plugin state, clipboard/Shelf and k4 terminal store scope.
Only the existing synthetic HOME is involved. Screenshots outside those stores remain intact, and previous
committed evidence is unchanged. The [candidate backup output](../automated/m04-candidate-backup.json)
and [readiness record](../automated/m04-readiness.json) preserve the manifest and verification context.

The existing `python3 tools/cp00.py restore` succeeded on retry. It selected the clean original ff520e3
checkout, passed the private prelaunch isolation probe, verified all files in `original-run03-complete`,
retained another disposable before-restore copy, restored the full allowlisted store set with exact
prelaunch checksum comparison, then launched `/original/shell.qml` with a full recorded identity.
See [successful restore transcript](../automated/m04-restore-retry.txt).
The original immutable snapshot itself still matches its original manifest and hashes.

Postlaunch settings read back `posicionBarra=arriba`, `reservaIsla=reserva`, with the original shortcut IDs.
The postlaunch comparison differs from the original snapshot only at `.local/state/k4/partida.json`;
no claim of permanently immutable live game state is made. The restore helper's exact prelaunch
comparison passed before starting the app. Candidate backup bytes remain unchanged.

The agent reopened original settings and launcher and inspected both actual captures:
[restored settings](../application/cp-00__M04__restored-settings__run-05.png) and
[ready launcher](../application/cp-00__M04__restored-launcher__run-05.png).
[Capture provenance](../automated/m04-capture-inventory.json) records both source revisions, commands,
UTC times and SHA256. These are agent preparation images, not owner M04 proof.

## Retained startup failures and recovery

No product/helper source was modified to recover from these preparation failures:

- The first candidate compositor start exited 1 with a private-output readiness timeout.
  The subsequent backup precheck exited 1 because `WAYLAND_DISPLAY` was absent. A stale M03
  `.socket.sock` plus the new live command socket made the unchanged helper reject ambiguous private identity.
  No candidate snapshot had yet been created.
- The command batch incorrectly continued from that failed precheck to Stop and Restore. That Restore
  attempt also exited 1 at compositor readiness, before the store restore stage. It selected ff520e3
  but did not replace the candidate stores. Every candidate store hash was independently verified
  unchanged afterward. The failed transcript is [retained](../automated/m04-restore.txt), as is the
  [failed precheck](../automated/m04-candidate-isolation.json).
- Both exact recorded private payloads were stopped successfully. An initial host socket probe used
  an overlong AF_UNIX pathname and exited without mutation. Retrying from the task-private directory
  returned ECONNREFUSED for the stale M03 command socket. Only that verified non-listening socket was
  renamed to `.socket.sock.stale-before-m04`, preserving its node and adjacent logs.
  [Endpoint recovery proof](../automated/m04-stale-endpoint-recovery.json) records the exact private path.
  No host or unrelated socket/process was touched. This is private runtime housekeeping, not a source patch.
- Candidate source was reselected while stopped. Fresh server/compositor startup and the complete
  private isolation probe passed. The candidate snapshot was taken while no candidate app was running,
  with b114d5a metadata and all 15 original candidate hashes verified. Guarded Stop then removed the
  live private endpoints cleanly; the exact selector contained no stale command sockets before Restore.
- The second Restore succeeded as described above. Future resumes must verify the exact endpoint set;
  abrupt test-window closure can leave stale sockets. Do not choose an arbitrary socket, disable the
  identity check or silently patch the pinned helpers. Preserve and verify any task-private stale endpoint.

All nonempty M04 command outputs, failure logs, probe/backup results and readbacks are retained under
`automated/m04-*`. Text copies normalize trailing whitespace to one final newline; the originals,
including empty stdout files, remain in ignored `scratch/cp00/lab/`.

## Live identity, isolation and return to candidate

The original test app is left running. Full current application/config/ID/PID/start ticks,
server/compositor identities, private bus/socket/signature, source and namespaces live in
the readiness record. Reverify them on resume; never act on a stale PID.
The app still cannot reach host HOME, parent display, host runtime/system bus or audio/input devices.
Host Quickshell config/ID/PID, notification owner and personal k4 path-existence checks match before/after.
No personal configuration/state, host daemon, monitor mode or clipboard was restored or changed.

After the owner M04 report, the agent's return procedure is:

1. Guarded Stop of this original test session; verify both payloads absent and private command sockets unambiguous.
2. Pin full b114d5a while stopped. Use existing prepare/server-start/compositor-start and the private prelaunch probe.
3. Invoke `/lab/runtime_control.py restore owner-before-m04-20261021-120008` through the existing private
   command socket. Its b114d5a manifest and file hashes must match before it replaces any allowlisted dummy store.
   The existing helper retains the original live test state separately and launches the restored candidate.
4. Verify candidate source/identity and restored bottom setting, record the actual outcome, and stop at owner
   approval handoff. This return has not yet been performed in this preparation; the owner must first check M04.

Keep all prior snapshots, including `original-run03-complete` and the new candidate snapshot.
M01's owner image and a bar-visible M03 owner image remain unsupplied; physical dual-display is still untested.
These limitations are not silently waived here. No Gate B, CP-01, push, publication, PR or merge is included.

## Administrative verification

- `python3 tools/workflow.py --render`: exit 0; generated owner view updated.
- `python3 tools/workflow.py --base-ref 5414626`: exit 0; structural/history validation passes.
- `python3 tools/test_workflow.py`: exit 0; all 30 tests pass (5.662 seconds).
- `python3 tools/test_cp00.py`: exit 0; all 14 safety tests pass (0.005 seconds).
- `git diff --cached --check`: exit 0.
- Read-only preservation/hash assertions against 5414626: exit 0; all prior evidence bytes,
  run/task/authorization records and test results/histories unchanged; later checkpoints unchanged;
  M03 preparation archived exactly. Both pinned checkouts remain clean; candidate/original snapshot
  bytes match their manifests; new working/index proof hashes and both image hashes agree.
  Changed paths are administrative review/owner/progress only. M04 remains NOT TESTED and Gate B null.
  These checks do not erase the retained real startup failures or grant an owner result.
