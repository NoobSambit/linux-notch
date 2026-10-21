# M03 owner report — run-05

Tested application: `b114d5a1b8c3ed90e97b577e3424092a783e04ed`.
Source: owner's reply immediately following the supplied M03 top/bottom/fullscreen instructions.
UTC transcription time: 2026-10-21T11:56:24Z. The owner did not give a separate execution timestamp.

## Literal report

> ok everything went fine

In context, this reports successful completion of the supplied M03 steps on the available single
nested test display: top and bottom placement, fullscreen entry/exit at each edge, island return
and harmless typing. Recorded verdict: **owner-reported M03 PASS for the available single-display matrix**.
No separate per-step timings, measurements or direct agent observation of the owner's interactions are invented.

The conditional second-physical-display repetition remains **NOT TESTED — ENVIRONMENT LIMITATION**:
only eDP-1 was attached at preparation. Earlier virtual-display observations are engineering evidence,
not physical owner proof. This report is not a release waiver or Gate B approval.

## Collected image and limits

The new [nested capture](cp-00__M03__owner-capture__run-05.png) was found at
`/home/cp00/Capturas/captura-20261021-115325.png` in the synthetic HOME, after M03 preparation.
It was opened, inspected for privacy, and copied byte-for-byte; [provenance](cp-00__M03__capture-provenance__run-05.json)
records SHA256, dimensions, filesystem time, preparation context and the inference about its owner-triggered origin.
The final saved dummy settings read `posicionBarra=abajo`, `reservaIsla=reserva`.

The image contains only the dummy document and harmless text. The island is hidden, consistent with
the inherited screenshot flow (`services/Captura.qml` apartarse and `shell.qml` capture opacity).
It does not independently show the selected edge or prove the transitions/input. No bar-visible
owner image was supplied; this evidence limitation remains explicit rather than treating the image
as that proof. The owner's report supplies the interaction result; the saved setting supplies the observed final edge.

## Continuity

Both recorded test payloads were verified not live; they were not restarted or restored in this update.
The selected source remains b114d5a. All prior runs, evidence, results and M03 preparation are preserved.
M04 recovery is the remaining owner test. Prepare its disposable backup/restore demonstration separately
on the next continuation, then ask the owner to check the restored launcher and settings. The earlier M01
owner image remains outstanding. No Gate B, CP-01, product changes or remote action is included.

## Administrative verification

- `python3 tools/workflow.py --render`: exit 0; generated owner view updated.
- `python3 tools/workflow.py --base-ref 728e729`: exit 0; structural/history validation passes.
- `python3 tools/test_workflow.py`: exit 0; all 30 tests pass (5.513 seconds).
- `git diff --cached --check`: exit 0.
- Read-only Python assertions against 728e729: exit 0; all previous evidence bytes, runs, task and
  authorization records, preparation records and existing test histories retained; other tests and
  later checkpoints unchanged; new evidence working/index hashes match. The tested b114d5a checkout
  is clean. Only the M03 report/capture/provenance, progress and generated owner view changed.
  Gate B remains null. These are administrative checks, not a new owner interaction or product rerun.
