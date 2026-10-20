# Verification and evidence

## Existing automated gates

Run from repository root, capture stdout/stderr, exit code and versions in each evidence run.
These are the commands in current `.github/workflows/validar.yml`; do not substitute one aggregate
green result for acceptance-specific evidence.

```sh
python3 tools/plugins.py
python3 tools/api.py
python3 tools/guia.py
python3 tools/layouts.py
python3 tools/prueba_editar.py
python3 tools/prueba_plugins.py
python3 tools/prueba_rutas.py
python3 tools/prueba_texto.py
python3 tools/workflow.py
git diff --check
```

`prueba_editar` uses installed ffmpeg/ffprobe for real media probes; if missing, record NOT TESTED
and the dependency, not PASS. `guia.py` may skip QML example checks without qmllint. Preserve that
limitation in evidence. None of these runs the full Hyprland shell. The current CI publication job
does not approve checkpoints. Workflow setup adds no runtime tests or dependency installations.

CP-01 will add focused pure-policy, migration, parser, IPC and plugin-lifecycle fixtures, using
available Qt Quick Test/JS/Python tools at the relevant seam. Every later contract specifies its
additional scenarios; record the actual command once implemented. Do not claim a planned suite exists.
Run matching-version QML checks with the real `api/` import path. Do not suppress new warnings to pass.

## Runtime and visual gates

Use [safe runtime](SAFETY.md). Each visual handoff must include actual collapsed/expanded app captures,
dark/light, keyboard focus, representative content and empty/error states, relevant display sizes/scales,
and reduced motion. Use deterministic dummy data, fixed fonts/scale/wallpaper/window bounds and explicit
state labels; document unavoidable differences. Scrub personal material before committing evidence.

Compare approved **concepts** to actual app captures side by side: geometry, hierarchy, spacing, text,
material, icons, state and motion. Record each noticeable difference and reason. Concept art is guidance,
not a pixel-perfect baseline or licensed runtime asset. Material deviations reopen Gate A.

After Gate B the approved real-app captures become the visual regression baseline. For later changes,
repeat matched state captures and create difference images using existing installed tools when available;
record masks/tolerance and why dynamic regions are excluded. Review differences manually; do not increase
tolerance or replace a baseline simply to hide a regression. Record expected accepted differences against
the exact Gate B SHA. If pixel diff tools are unavailable, provide side-by-side captures and record that
automated pixel comparison is NOT TESTED. Static property tests still cover geometry/state bounds.

Motion/input require recordings and actual interaction: before/middle/after, anchored and moving regions,
interruption/return, focus and frame traces. A storyboard is intended motion, never proof of motion.
Measure idle/media/dock/transition CPU/RSS/GPU/frame timing against CP-00 under matching conditions.
Record sample duration, workload, hardware and tool; establish budgets from measured evidence rather
than invented universal limits. Hidden/disabled effects must stop. Accessibility proof covers focus order,
accessible names, keyboard actions, non-color cues, contrast over varied backgrounds and enlarged/long text.

## Evidence and outcomes

`review/<checkpoint>/evidence/<run>/application/` holds real screenshots/recordings;
`owner/` within that run holds owner submissions; `automated/` holds logs/traces/diff images.
Use run names `run-01`, `run-02`, never overwrite previous runs. Filenames:
`cp-04__M02__fullscreen__run-01.png`, `cp-05__R01__volume-restore__run-01.webm`.
Record provenance/type in the run index. Runtime handoff, logs and comparison use [templates](TEMPLATES.md).

In progress.json append test records with `id`, `kind` (automated/runtime/owner), `result`, date,
command/steps, tested SHA/tree, environment and evidence. Keep failures when a later run passes.
Only the latest applicable result counts for readiness; an old passing run cannot clear a new failure.
All acceptance IDs must map to a test/evidence record before handoff. Unavailable hardware is
NOT TESTED — ENVIRONMENT LIMITATION, not a hidden skip. For required gates arrange another test
environment; a materially changed release promise requires an explicit DECISIONS entry.

Review gate: inspect full diff for scope, compatibility, privacy, data safety, unexplained media and
test weakening. Record findings and resolutions before owner review. An agent review is technical
evidence, never owner approval. On owner failure reproduce the reported scenario, add a focused regression
where useful, fix the smallest cause, rerun affected checks and previously passed dependent flows, and
request retest of the changed run. Keep unresolved failures visible and dependencies closed.
