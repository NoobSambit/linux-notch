# M03 preparation — run-05

This prepares the existing screen/fullscreen test from the [frozen run-05 handoff](../index.md).
Application revision remains **b114d5a1b8c3ed90e97b577e3424092a783e04ed**.
Authorizing owner continuation in this thread: “proceed with m03 , or i need to test smth ???”.
Source: owner message on 2026-10-21; the UTC preparation timestamp is in the readiness record.
This is agent preparation. M03's result and Gate B remain pending in
[progress.json](../../../../../docs/workflow/progress.json).

## Your test

Open the nested **aquamarine** window. **Ajustes → Island** is already open.
Scroll down in the right-hand pane, below the large preview, to **Dónde vive la barra**.

For each position, **Arriba** (top) and **Abajo** (bottom):

1. Select the position and press **Esc** to close settings. Check the island appears on that edge.
2. From your ordinary terminal in `/home/noobsambit/Documents/k4-main`, run:

   ```sh
   python3 tools/cp00.py fullscreen true
   ```

   Look at the nested test window: the teal dummy document should fill it and the island should move out of its way.
3. Run:

   ```sh
   python3 tools/cp00.py fullscreen false
   ```

   Check that the island returns on the selected edge. Click `Harmless input` and type harmless text;
   check typing works. This fixture returns maximized after fullscreen; exact tiled bounds are not promised.

To change the edge, right-click the island wherever it is placed → **Ajustes → Island**.
After checking both positions, finish at **Abajo**, then use **Todas → Captura → Guardar → Pantalla**
as in M02. This saves one whole test-screen image with the chosen edge in the synthetic Capturas folder.
Tell Codex you took it; Codex can collect that isolated image without copying your real desktop.

Report **M03 PASS / FAIL / NOT TESTED / NEEDS HELP**, naming top/bottom and any problem.
No coding or diagnosis is required from you. If something sticks, Stop remains:

```sh
python3 tools/cp00.py stop
```

## Matrix and available displays

The owner checks are top placement/fullscreen/return/typing and bottom placement/fullscreen/return/typing
on the available single nested test display. Physical inventory currently shows only eDP-1,
1920x1080 scale 1. The stable private test output is CP00-STABLE, 1280x720@60Hz scale 1;
WAYLAND-1 is its mirror, not an independent second test display. No second output was added here.
The conditional second-physical-display repetition remains **NOT TESTED — ENVIRONMENT LIMITATION**.
Earlier virtual two-output engineering observations remain in run-05; they are not physical owner proof.
This preserves the original handoff's available-hardware boundary, without granting a release waiver.

## Preparation evidence and limits

Existing `tools/cp00.py start`, private-output focus selection and `demo` were used with the same pinned
checkout. The local fixture player was paused for this screen/fullscreen test. Settings started at
`posicionBarra=arriba`, `reservaIsla=reserva`. No runtime/helper/product source or dependencies changed.
The original Start/Stop/Restore commands and frozen run record/index remain unchanged; this supplies
the existing M03 menu labels and helper invocations, not a new software/environment test run.

Agent rehearsal ran `python3 tools/cp00.py fullscreen true` then `fullscreen false`, both exit 0.
The former produced a real 1280x720 fullscreen dummy window (mode 2). On return it was mapped and
maximized (mode 1), with the island visible. An initial ad hoc readiness assertion expected mode 0
and failed on that mode-1 readback. This was an incorrect expectation of restored tiled bounds,
not proof that fullscreen exit failed. The actual mode-1 return is retained explicitly; no product
gate, test implementation or product behavior was changed. Owner verification of both positions
and typing remains unperformed. The source checkout is clean at b114d5a.

Exact outputs: [Start](../automated/m03-start.txt), [private focus](../automated/m03-focus.txt),
[demo](../automated/m03-demo.txt), [initial readback](../automated/m03-initial-readback.json),
[fullscreen entry](../automated/m03-fullscreen-check.json),
[opening settings](../automated/m03-settings-open.txt) and
[readiness/return](../automated/m03-readiness.json).
Text stdout copies normalize their trailing whitespace to one final newline; originals remain in ignored scratch.

The [fullscreen image](../application/cp-00__M03__fullscreen__run-05.png) and
[ready settings image](../application/cp-00__M03__ready-settings__run-05.png) were opened and inspected.
They are agent preparation images, not an owner M03 submission.
[Capture provenance](../automated/m03-capture-inventory.json) records source, command, UTC time and SHA256.

Before/after host invariants match: ordinary Quickshell ID xzn1r8nt/PID 1293 and its end4-pC config,
notification owner `:1.14`, and absent personal k4 config/state/share paths. No personal contents were read.
The existing Start action's prelaunch isolation probe passed; runtime checks still find host HOME,
parent socket, host runtime/system bus and audio/input devices absent in the app namespace.
No host focus/workspace, clipboard, configuration, service or monitor mode was modified.

## Live identity and recovery

The test runtime and dummy fixture are left running. Full current application/config/instance/PID/start
ticks, server/compositor identities, source SHA, private bus/socket/signature and namespaces are in
the readiness record. Revalidate these handles on resume; never target an old PID without verification.

Guarded Stop is above. The existing recovery target remains
`ff520e33e136bbce11b7100c69888dedf42f7273` with immutable dummy-only snapshot
`scratch/backups/cp-00-baseline/original-run03-complete`; [recovery procedure](../automated/recovery.md).
No Restore was performed during this preparation. The selected source remains b114d5a.
M04 recovery and explicit Gate B approval are separate later owner actions. No CP-01 or remote action is authorized.

## Administrative verification

- `python3 tools/workflow.py --render`: exit 0; owner view regenerated.
- `python3 tools/workflow.py --base-ref 9cc50ba`: exit 0; structural/history checks pass.
- `python3 tools/test_workflow.py`: exit 0; all 30 tests pass (5.509 seconds).
- `git diff --cached --check`: exit 0.
- Read-only Python preservation/hash assertions against 9cc50ba: exit 0; all previous evidence bytes,
  run/task/authorization records and every test history unchanged; later checkpoints unchanged; M02
  preparation archived exactly; working/index preparation hashes and screenshot hashes agree.
  Only administrative review/owner/progress paths changed. The pinned checkout is clean at b114d5a.
  M03 remains NOT TESTED and Gate B null. These checks do not grant an owner result.
