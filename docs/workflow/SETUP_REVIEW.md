# Workflow setup review — 2026-10-20

Historical setup-agent report for `3610e20`. Its claims are not independent acceptance.
See the [engineering audit](ENGINEERING_AUDIT.md) for reproduced checker weaknesses and subsequent
validation. Current execution/approval state is solely [progress.json](progress.json).

This reviews the **workflow setup**, not CP-00 or any product implementation. All eleven checkpoints
remain PLANNED; tasks PENDING, tests NOT TESTED, authorizations/approvals empty, active checkpoint null.
Owner approval of this workflow and explicit CP-00 authorization are the next actions.

## Requirement-level audit

| Requested deliverable | Current evidence |
| --- | --- |
| Inspect authoritative project and research established practice | RESEARCH documents source/CI findings and primary-source practices; product documents remain authoritative and unchanged. |
| Separate agent and owner experiences | AGENTS and docs/workflow provide engineering execution; owner/ has start/progress/reference/test/feedback/recovery guides and eleven personal notes. Root README and docs index link both. |
| Organized visual storage | review/ policy and real checkpoint save folders separate submitted alternatives, motion, approved immutable sets, actual app captures, owner failures and logs. Existing module assets remain production paths. |
| Exact names, formats, revisions, submission and inspection | Seven .visual.md briefs list three mandatory static boards plus one storyboard each, exact filenames/canvases, paths and owner message. PNG/JPEG/WebP supported; optional video/local-large-media policy explicit. |
| Owner-selected feasible visual direction | Explicit Gate A, agent must open actual readable files, check scope/feasibility/inheritance, record owner words and exact hashes; no reference set or approval fabricated. |
| Distinct before/after approval | Lifecycle requires Gate A before visual code; Gate B after actual app proof/manual tests on exact SHA/run. Generated imagery never substitutes for runtime evidence. |
| Every checkpoint executable | Eleven contracts map to roadmap 0–10, four bounded tasks each, dependencies/spec/source scope/exclusions/risks, acceptance proof IDs, automated/runtime checks and completion gates. |
| Owner personal notes and manual testing | Eleven notes answer the owner questions, including WHAT YOU NEED TO DO NOW and checkpoint-specific tests with before/steps/expected/failures/evidence/recovery. Statuses and short bug template are explicit. |
| Important scenarios | Core display/fullscreen/hotplug/text/focus/motion, D20 ownership/migration, D24 Atalaya, file/folder/multi/copy/cancel/missing/keyboard, clipboard privacy, settings persistence, plugin/inherited checks and recovery map to relevant checkpoints. Hardware limits remain NOT TESTED. |
| One status record and resume | progress.json owns all task/test/reference/gate/run/next-action state; tools/workflow.py renders the owner view and checks consistency. No chat dependency or competing editable tracker. |
| Safe recovery/minimal owner engineering | SAFETY documents HOME/bus/clipboard isolation limits, exact-instance stop, backups/last-good restore and permission boundaries. CP-00 prepares tested actions; setup does not pretend those helpers exist. |
| No unauthorized product work | Diff is restricted to docs/owner/review placeholders, AGENTS, gitignore and a standard-library documentation/status helper; no QML/runtime/installer/desktop changes, generated final art or dependency installs. |
| Git budget | Dedicated local docs/notchbar-workflow branch; delivery budget is 12 commits, within requested minimum 10 and maximum 15. No push authorized. |

## Validation evidence

Setup verification runs from the repository root. Current inherited commands all exit 0:

| Command | Observed result |
| --- | --- |
| `python3 tools/plugins.py` | 31 built-in plugins verified. |
| `python3 tools/api.py` | 146 QML files reviewed; no API boundary violations. |
| `python3 tools/guia.py` | 5 inherited documentation files checked. |
| `python3 tools/layouts.py` | 275 QML files checked. |
| `python3 tools/prueba_editar.py` | 141 tests pass. |
| `python3 tools/prueba_plugins.py` | 63 tests pass; expected negative-case messages appear. |
| `python3 tools/prueba_rutas.py` | Local path/network/timeout checks pass. |
| `python3 tools/prueba_texto.py` | 11 text sinks checked. |

Final workflow validation additionally checks the eleven records, task/proof IDs, six manual-test fields,
28 mandatory reference filename/path declarations, relative links, gate prerequisites and generated owner
view. Git ignore probes check selected-versus-submitted media and private/video policy; diff review checks
that runtime and approved specifications are unchanged. `git diff --check` must pass before final commit.
The helper's negative checks use in-memory altered copies and cannot mutate real approval state.

Observed additional results: workflow validator PASS; seven negative checks correctly reject visual
implementation before Gate A/dependencies, PASS without history, DONE without evidence, self-approval,
missing approved images, dependency bypass and path escape. Eight Git tracking probes PASS. The initial
record contains 44 pending tasks, 106 NOT TESTED checks (50 owner tests), 28 requested reference slots,
zero runs/reference sets/approvals and no active checkpoint. A malformed numbered CP-00 instruction found
during review was corrected; numbered-step validation now guards against an empty checklist step.

These commands prove documentation structure and inherited regressions for this planning change.
They do not prove live Hyprland isolation, visual quality or any future checkpoint. No product was
launched. First runtime/evidence/owner tests will occur only after CP-00 authorization.
