# Independent engineering review — workflow branch

Reviewed `docs/notchbar-workflow` at `3610e20` against `main` (`ff520e3`) on 2026-10-20.
This is a workflow engineering audit and repair report, not owner approval or a product checkpoint.
Current execution state remains exclusively in [progress.json](progress.json).

## Prioritized findings before correction

Line references in this table describe the reviewed `3610e20` version, not later edited line numbers.
The first six checker probes used isolated in-memory copies; no real authorization was fabricated.

| Priority / finding | Exact affected files and concrete evidence | Risk | Smallest practical correction |
| --- | --- | --- | --- |
| **BLOCKER B1 — unsupported handoff accepted** | `tools/workflow.py:134–187` checked presence of history strings and a run ID. A CP-00 AWAITING OWNER TEST probe passed with nonexistent task/test evidence, history referring to an unrecorded run and different revision/environment, and automated PASS with `exit_code: 1`. `runs` needed only `id`; no recovery/handoff was checked. | Untested or unrecoverable work can appear ready for owner approval. | Check full run identity, current history applicability, command exit codes, real hashed durable files, recovery/review/handoff artifacts and exact Gate B revision. Reject later product changes. |
| **BLOCKER B2 — lifecycle/task coverage bypasses** | `tools/workflow.py:83–120` accepted all tasks deleted from CP-00, unauthorized DONE work in PLANNED, active/next pointers to CP-10 while CP-00 remained planned, schema 999/status APPROVED, and nonvisual CP-00 in AWAITING REFERENCES. `:149–167` only inspected saved references while a current Gate A existed. | False progress, skipped prerequisites, lost work after resume and corrupted superseded references remain structurally green. | Bidirectional contract/task/test IDs, workflow/active/next/current-task invariants, branch/recovery identity, mandatory reference slots and retained-set validation. Preserve an explicit correction path. |
| **IMPORTANT I1 — checker not in CI and history editable** | `.github/workflows/validar.yml` contained no workflow invocation; `docs/workflow/VERIFICATION.md:5–19` nevertheless described it as a current CI command. `tools/workflow.py` compared only a single snapshot; editing/removing old failures or set hashes was undetectable. `main()` rendered before validation. | Local-only discipline fails on another agent's PR; invalid records can overwrite the owner view. | Add checker plus stdlib regression tests to the existing job, compare with PR/push base history, and validate before rendering. No new service/toolchain. |
| **IMPORTANT I2 — image-to-QML translation underspecified** | `cp-03-design-system.md:T01` asked for “agreed token interpretation,” while `RECORD_FORMAT.md:29–35` stored only images/hashes and free-form inspection. `TEMPLATES.md` had no implementable design mapping. | Different agents invent geometry/state/motion choices from the same boards and cannot identify what Gate A covered. | A short versioned design translation with source crops, logical geometry, values, existing component/property mapping, states/focus, motion and acceptance matrix, hashed into Gate A. |
| **IMPORTANT I3 — local evidence not durable** | `review/README.md:27–35` allowed a subset of selected images and local videos; checker only tested local existence. `cp-02-dnd-spike.md:23–25` put the executable spike in ignored scratch. `.gitignore` correctly ignored large/private media but no handoff checked retrieval. | Another checkout loses required references, motion proof or the spike needed again by CP-07. | Track all essential small proof with exact hashes/index bytes; retain a recording retrieval manifest and require retrieval at handoff; preserve minimal spike source/fixture recipe under review evidence. Keep large/private media ignored. |
| **IMPORTANT I4 — correction and acceptance ambiguity** | `RECORD_FORMAT.md:37–52` made subcases optional and told agents to invalidate downstream acceptance without explaining a lifecycle valid under `workflow.py:95–98`. CP-00 owner M02/M03 expected known defects to be recorded, but generic failure gates did not distinguish baseline characterization. Roadmap milestone 1 explicitly required clipboard fixtures, absent from CP-01's concrete A01 scope. CP-05 omitted specific entry/exit-delay regressions. | An agent can deadlock on an inherited defect, lose approval history, skip early clipboard safety coverage or hide missing coverage inside a broad PASS. | Define suspension/reapproval, explicit scenario splitting and baseline observation semantics; add early clipboard and hover timing cases; require bounded execution notes and measured performance acceptance. |
| **IMPORTANT I5 — stale owner navigation** | `owner/README.md`, `owner/TESTING.md`, `owner/RECOVERY.md` stated setup-time facts as permanent current instructions. Eleven personal notes hardcoded run-01 in approval wording; review READMEs asserted no tests/approvals existed forever. | Owner tests or approves the wrong run, or repeats already-granted authorization. | Route current actions through generated Progress; label first-run examples and use current-run approval wording. Retain the plain-language checklists. |
| **OPTIONAL O1 — approval commit/PR mechanics** | `docs/workflow/README.md:63–83` asked to approve a tested SHA and then commit its record, without specifying tested-code versus evidence commits or stacked PR bases. `SAFETY.md` used ambiguous `/scratch/` wording. | Agents can chase self-referential SHAs or branch from code that omits the approval record. | Explain clean pinned tested commits, later evidence commits, predecessor branch tip, separately authorized PR/merge/push, and repository-local scratch. |

## What was retained and coverage of the review objectives

The eleven milestones match the approved roadmap: baseline/safety, early isolated DnD proof, design
system, geometry, activities, Dual polish, Shelf, clipboard, coherence and release. No reorder or new
framework is justified. The source confirms the safety concerns already identified: HOME-based settings
and plugin paths, eager `NotificationServer`, clipboard watchers and installer-wide `pkill -x quickshell`.
The existing safety prohibition on launching/installing in the live session is appropriate.

| Review objective | Assessment and evidence |
| --- | --- |
| 1. Contract completeness | All eleven contracts and owner checklists inspected against V1_SPEC, IMPLEMENTATION_PLAN and architecture; task/proof mappings retained and checked in both directions. |
| 2. Hidden dependencies/order | CP-02 precedes design and Shelf, CP-07 revalidates its proof; D20/D24 safety precedes activity polish. Early clipboard characterization restored. Actual environment availability remains CP-00 work. |
| 3. Broad tasks | Four T IDs per checkpoint remain; ordered bounded execution notes identify source seams, inputs, outcomes and next steps before implementation. |
| 4. Acceptance/regressions | Required scenario coverage, conditional child cases, baseline defects, clipboard safety and hover timing clarified; no spec requirement downgraded. |
| 5. Isolation/rollback | Existing identity/backup rules retained; nested Hyprland signature, system bus, audio and portal endpoints explicitly audited. Helpers/recovery still require live CP-00 proof. |
| 6. State machine/checker | Negative reproducers plus positive lifecycle/correction fixtures cover the repaired invariants. Structural checks do not authenticate owner messages or prove behavior. |
| 7. CI | Existing Python CI job now validates records/history and runs checker tests without launching the product. |
| 8. Git/branch/PR/approval | Full available SHAs, predecessor recovery ancestry, product-versus-tested diff and archived decisions checked; owner approval and remote operations remain distinct. |
| 9. Reference lifecycle | All seven detailed briefs, 28 mandatory slots, immutable sets, candidate inventory, inspection and hash binding retained/strengthened. No final references generated. |
| 10. QML design interpretation | Required design translation maps selected art to the existing Theme, host, Dual and public compatibility paths; unresolved material decisions go to Gate A. |
| 11. Runtime/motion/visual regression | Real-app captures, recordings, matched baselines, masks/tolerance and measured frames remain required. Concepts/fixtures never substitute for runtime evidence. |
| 12. Durability | Working-tree/index hashes, tracked essentials, retrieval manifest and recoverable spike recipe address loss across machines. Remote retrieval remains a live agent check. |
| 13. Owner instruction consistency | Current actions come from Progress; static guides and first-run paths no longer claim current status. |
| 14. Nontechnical owner usability | Existing Start/Stop/Restore, short M checklists and plain approval messages preserved. Technical record/translation work remains the agent's responsibility. |
| 15. Context-loss recovery | Single status record, exact current task/run/branch, append-only evidence and explicit suspended checkpoints permit deterministic resumption. Runtime handles must be reverified. |

## Resulting validation

The two blockers and five important issues above have targeted corrections on the existing branch;
O1's documentation clarification is included. Checker/CI/test implementation is committed at
`0c666c6719c1b4beea4b4a52056f289c19d2e870`. Final validation was completed on 2026-10-21 with Python 3.14.7;
ffmpeg, ffprobe and qmllint were present. The setup report was not used as a passing test result.

| Exact command/check | Observed result |
| --- | --- |
| `python3 tools/test_workflow.py` | PASS: 30 tests, including all original bypass classes, complete synthetic progression through eleven checkpoints, corrections, visual reapproval, archived proof, missing/changed/unstaged evidence, stale revision/environment, failed command, deleted coverage, history preservation and invalid-render non-mutation. |
| `python3 tools/workflow.py --base-ref 3610e20` | PASS: current record and preserved history against reviewed head. |
| `python3 tools/workflow.py --base-ref main` | PASS: first introduction relative to main is handled. |
| `python3 tools/workflow.py --render` | PASS: generated owner view is consistent; no approval/status change. |
| `python3 tools/plugins.py` | PASS: 31 plugins verified. |
| `python3 tools/api.py` | PASS: 146 files, no API boundary violations. |
| `python3 tools/guia.py` | PASS: 5 inherited documents; qmllint available. This is not a whole-product QML test. |
| `python3 tools/layouts.py` | PASS: 275 QML files. |
| `python3 tools/prueba_editar.py` | PASS: 141 tests, installed ffmpeg/ffprobe available. |
| `python3 tools/prueba_plugins.py` | PASS: 63 tests; expected negative-case diagnostics retained. |
| `python3 tools/prueba_rutas.py` | PASS: path/network/timeout boundary checks. |
| `python3 tools/prueba_texto.py` | PASS: 11 text sinks. |
| `git diff --check` | PASS. |
| Scope and record inspection against `3610e20` | Changes confined to workflow docs, owner/review guidance, checker/tests and existing CI. All 11 checkpoints PLANNED, 44 tasks PENDING, 106 checks NOT TESTED, zero authorizations/Gate A/Gate B, no runtime handle. |

No product source, approved product specification, installer, personal configuration or dependency
was changed. `.gitignore` remains appropriate and unchanged. Local commits only; no push, merge,
release or owner approval. Hosted GitHub CI has not run for these local commits; its commands were
run locally. The checker remains a structural guard: owner identity/provenance, content adequacy,
actual image decoding, scenario completeness and remote recording retrieval still require real review.
It does not claim to authenticate approval or execute the future runtime gates.

## Live validation still required during CP-00

After explicit workflow/CP-00 authorization, establish a test account/session or equivalent proven
isolation; inventory actual versions, devices, state paths and service endpoints. Prove that the test
process and its children cannot affect personal settings, clipboard, notification ownership or host
Hyprland. Demonstrate exact-instance Start/Stop/Restore, stale-ID/PID handling, dummy backups and
matching-state rollback. Capture baseline top/bottom/compatibility sides, fullscreen/displays,
media/clipboard/capture/plugin examples, known defects and Atalaya effective state. Obtain reproducible
startup/idle/active/closed CPU/RSS/GPU/frame measurements, rights inventory and a usable owner handoff.
Record unavailable hardware and skipped capabilities honestly. No runtime proof is supplied by this review.

Later live work still needs CP-02 cross-app DnD, actual reference decoding, rendered QML/accessibility,
notification ownership races, real recording retrieval, owner M tests and Gate A/B decisions.
Neither this report nor a green workflow checker approves the workflow, starts CP-00, grants a gate,
or authorizes merge/publication.
