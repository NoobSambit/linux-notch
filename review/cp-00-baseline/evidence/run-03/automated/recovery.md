# CP-00 recovery engineering rehearsal

The installed CLI is Quickshell 0.2.1. Runtime controls inspect full instance ID, exact config path,
PID, process start ticks, executable, arguments, PID namespace, Wayland socket, nested Hyprland
signature, session-bus endpoint and source SHA before acting. Stop uses `quickshell kill --id FULL_ID`
only after that match; pidfd guards the verified fallback. The old ID being absent never selects a
replacement. Sandbox teardown signals only its separately verified payload; host processes are untouched.

`python3 tools/test_cp00.py`: 14 safety regressions pass. Live recovery-rehearsal.json records original
stop while /lab/neighbor.qml remained running; repeated stop leaves it intact. That neighbor ended
only with its own test sandbox teardown. Tests include foreign config, substring ID, PID reuse,
changed bus/executable, missing previous-revision ID, corrupt snapshot, symlinks and traversal.

Complete snapshot: scratch/backups/cp-00-baseline/original-run03-complete (mode 0700, ignored).
Original source: ff520e33e136bbce11b7100c69888dedf42f7273. The retained manifest records all files and
checksums for settings, plugins.json/catalog, per-plugin dummy state, actual harmless clipboard
text/index and a Shelf dummy reference. No personal store is involved. Source export files are
checked against Git blob IDs and SHA256 before launch. Backups are immutable named directories;
restoration verifies hashes and source/store compatibility before replacing allowlisted dummy paths.
The pre-restore current state is separately retained, then restored bytes are checked before start.

The direct rehearsal mutated plugin dummy state and deleted the Shelf dummy reference, restored
both exactly, reopened actual settings/launcher and stopped safely. Initial settings capture was
taken before Loader rendering; a settled capture was then opened and confirmed visually. The final
cross-revision rehearsal started clean pinned b2e7122, stopped its /candidate instance, selected the
original ff520e3 export and restored the matching complete snapshot. See candidate-start,
cross-revision-restore and final-stop transcripts. Both test payloads are stopped after this run.

Tested copyable actions (repository root):

```sh
python3 tools/cp00.py start
python3 tools/cp00.py stop
python3 tools/cp00.py restore
```

Start prints a CP-00/source label. Restore previous switches only the test source and dummy stores;
no real desktop config, system dependency, installer, notification daemon or personal data is changed.
These actions have been exercised; final owner readiness still requires T03/T04 and clean-revision
verification. Do not ask the owner to run tests until progress.json says AWAITING OWNER TEST.

Tooling failures retained from exploration: pre-ready compositor probe correctly refused to launch;
readiness now waits for a working private output. Quickshell list --json emits the exact human sentence
`No running instances.` when empty; the parser now accepts only that known case, retaining errors for
other malformed output. IPC show takes no positional target on this release; readiness uses show and
checks target k4. The first cross-source restore refused a stale absent candidate handle; absence is
now checked before config/session matching, and both a regression and a live cross-source rerun pass.
These were CP-00 tooling defects, not repaired inherited k4 behavior.
