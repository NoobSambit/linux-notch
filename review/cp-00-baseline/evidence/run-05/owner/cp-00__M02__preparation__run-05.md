# M02 preparation — run-05

This supplements the frozen [run-05 handoff](../index.md) for its existing M02 steps.
Application revision remains **b114d5a1b8c3ed90e97b577e3424092a783e04ed**.
This records agent preparation, not an owner M02 result or Gate B decision.
Current test status is authoritative only in [progress.json](../../../../../docs/workflow/progress.json).

## Ready for the owner

The isolated test desktop is running. Open its **aquamarine** window; the native launcher
(`Buscar aplicaciones`) is already open. Two coloured dummy documents are behind it.

1. Type `vlc` into the launcher to check search and keyboard focus, then press **Esc**.
2. Right-click the small top-centre island → **Ajustes**. Check that settings opens, then **Esc**.
3. Right-click the island again. On **CP00 local sine track**, click **Pause**, then **Play**.
   Silence is expected: the local WAV plays into the isolated dummy audio sink.
4. Close the panel with **Esc**. Click `Harmless input` in the teal dummy document;
   press **Ctrl+A**, type `CP00 M02 harmless text`, then **Ctrl+C**.
   Right-click the island → **Portapapeles** and check that text appears. Close with **Esc**.
5. Right-click the island → **Todas** → **Captura**. Select **Guardar**, then **Pantalla**.
   Check that a capture confirmation/preview appears. This captures only the nested dummy desktop;
   saved files stay under the synthetic `/home/cp00/Capturas`.

Report only **M02 PASS / FAIL / NOT TESTED / NEEDS HELP**, with the step and what happened if needed.
For a problem, Codex handles diagnosis. If available, attach a screenshot of the failing test view
without personal material. M03 and M04 will be prepared separately.

Stop the isolated test when needed, from the repository directory:

```sh
python3 tools/cp00.py stop
```

If it has been stopped, ask Codex to prepare the same pinned fixtures again before M02.
The original Start/Stop/Restore actions remain in the handoff; no installer or personal restore is needed.

## Preparation and identity

Exact outputs are preserved in [start](../automated/m02-start.txt),
[demo](../automated/m02-demo.txt), [initial readback](../automated/m02-readback-initial.json),
[fixture preparation](../automated/m02-fixture-preparation.json),
[opening the launcher](../automated/m02-owner-start-view.json) and
[final readiness](../automated/m02-readiness.json).
The final readiness record contains full current server/compositor process identities, application
ID/config/PID/start ticks, source SHA, private Wayland/socket signature, session bus and namespaces.
Revalidate those handles on resume; do not act on stale PIDs.

The existing `python3 tools/cp00.py start` and `demo` were used. Both synthetic documents,
the looping `/lab/dummy.wav` track and `CP00 harmless owner-test text` clipboard were checked.
The native launcher is left open; M02's later user interaction has not been claimed.
The source checkout is clean and mounted read-only; the application process is unchanged throughout preparation.
No new runtime/helper/product code or dependencies were introduced.

Initially the private mirror `WAYLAND-1` was focused with no workspace, so the fixture process
loaded but mapped no windows (retained in the initial readback). The two attempted legacy dispatcher
forms were rejected: `hyprctl dispatch focusmonitor CP00-STABLE` exited 7 with a Lua syntax error;
`hyprctl eval 'return hl.dispatch("focusmonitor", "CP00-STABLE")'` exited 7 because it expected a dispatcher object.
The documented Lua form `hl.dispatch(hl.dsp.focus({monitor="CP00-STABLE"}))` succeeded inside the
private compositor. Only the exact verified dummy fixture was stopped/relaunched. Both dummy windows
then mapped on CP00-STABLE; no host focus/workspace was changed. This is fixture/session preparation,
not a product repair or a new performance run. API form checked against the
[official Hyprland dispatcher documentation](https://wiki.hypr.land/configuring/core/dispatchers/).

The before/after host checks match: ordinary Quickshell config
`/home/noobsambit/.config/quickshell/end4-pC/shell.qml`, ID `xzn1r8nt`, PID 1293;
notification owner `:1.14`; personal `.config/k4`, `.local/state/k4` and `.local/share/k4` absent.
Only path existence was checked. The app namespace still cannot reach host HOME, parent display,
host runtime/system bus or audio/input devices. No host clipboard was read or written.
The private prelaunch isolation probe passed through the existing guarded Start action.

The owner-testing message explicitly permits small administrative commits after the completed five
engineering commits. No new five-commit budget is being inferred. All earlier evidence, run records,
results and the pinned tested application are preserved. CP-01 and Gate B remain outside this preparation.

## Captures and recovery

Agent screenshots: [documents](../application/cp-00__M02__prepared__run-05.png),
[control panel](../application/cp-00__M02__panel__run-05.png),
[application drawer](../application/cp-00__M02__apps__run-05.png),
[ready launcher](../application/cp-00__M02__launcher-ready__run-05.png).
All four were opened and visually inspected; they contain only synthetic/public fixture content.
[Capture provenance](../automated/m02-capture-inventory.json) records SHA256, UTC time, display,
source and command. These are agent preparation images, not owner M01 or M02 submissions.

Stop remains `python3 tools/cp00.py stop`, using verified exact identities. The existing recovery
target is `ff520e33e136bbce11b7100c69888dedf42f7273` with immutable dummy-only snapshot
`scratch/backups/cp-00-baseline/original-run03-complete`. No recovery was performed in this preparation;
the [proven recovery procedure](../automated/recovery.md) and earlier logs remain unchanged.
The current selected source remains b114d5a. The ignored live logs/handles are in
`scratch/cp00/lab/`; no personal state was copied.

[Administrative verification](../automated/m02-administrative-validation.md) records workflow/history
validation, 30 workflow regressions, clean pinned-source and previous-evidence preservation checks.
