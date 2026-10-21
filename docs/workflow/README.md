# Checkpoint execution workflow

Workflow setup does not authorize product work. Current state is in [progress.json](progress.json).
Owner entry point: [Start here](../../owner/README.md).

## Organization and authority

The approved [roadmap](../IMPLEMENTATION_PLAN.md) has eleven milestones. CP-00 through CP-10
map one-to-one to them, preserving the early isolated Shelf spike and early design system.
Each contract has a task list and acceptance-to-proof table; each has a separate plain-language
owner note and a visual brief. No new PRD or parallel product specification is introduced.

| Location | Responsibility |
| --- | --- |
| `AGENTS.md` | Short entry point and permanent guardrails. |
| `docs/workflow/checkpoints/` | Engineering execution contracts and creative briefs. |
| `docs/workflow/progress.json` | Single execution record: tasks, tests, references, decisions, blockers, next actions. |
| `owner/` | Simple guides and individual checkpoint instructions. `PROGRESS.md` is a generated view. |
| `review/<checkpoint>/` | Owner reference submissions, immutable selected sets, actual app captures and test evidence. |
| Existing `core/`, `widgets/`, `plugins/`, `api/` | Runtime code/assets; references never belong here. |
| `scratch/` (ignored) | Disposable runtime worktrees, fixtures and private backups; never the only copy of approved evidence. |

Why: a short agent map survives context loss; owners can stay in one folder; review media cannot be
mistaken for application resources; one JSON record prevents diverging progress tables. A small Python
standard-library helper validates links/records and generates the overview. No project manager service,
Spec Kit installation, Git LFS, token pipeline, CMake rewrite or new test framework is required.
See the source-grounded [design rationale](RESEARCH.md) and [setup review](SETUP_REVIEW.md).
The independent [engineering audit](ENGINEERING_AUDIT.md) records subsequently reproduced gaps and fixes.

## Lifecycle and permissions

Nonvisual: `PLANNED → READY TO IMPLEMENT → IMPLEMENTING → TESTING → AWAITING OWNER TEST → APPROVED`.
Visual: `PLANNED → AWAITING REFERENCES → REFERENCES SUBMITTED → AWAITING VISUAL APPROVAL →
READY TO IMPLEMENT → IMPLEMENTING → TESTING → AWAITING OWNER TEST → APPROVED`.

| Transition | Required evidence / actor |
| --- | --- |
| Leave PLANNED | All dependencies APPROVED; implementation authority recorded. CP-00 needs explicit workflow/baseline authorization. Later checkpoints use the next-checkpoint authorization recorded at prior handoff, or request it if absent. |
| REFERENCES SUBMITTED | Agent inventories real files and can decode/open them. Missing/corrupt files keep the gate closed. |
| AWAITING VISUAL APPROVAL | Agent has reviewed scope, feasibility, prior design inheritance and contradictions; owner receives exact proposed set and deviations. |
| READY TO IMPLEMENT | Gate A owner quote/date and exact file hashes recorded for visual work; nonvisual briefs state no generation required. |
| TESTING | Scoped tasks implemented; diff reviewed; commands and runtime revision recorded. |
| AWAITING OWNER TEST | Required automated/runtime checks pass; real evidence and reference comparison ready; short launch/stop/recovery handoff proven. |
| APPROVED | Owner explicitly approves the tested SHA and evidence run (Gate B); required scenarios passed, with any allowed limitation explicitly decided. Agent only records the decision. |

On failures return to `IMPLEMENTING` for a scoped correction, retaining failed results and adding a
new run; move through TESTING and owner retest again. A material visual correction reopens Gate A
before coding. Keep the previous approved set in history. Blockers use `blocked_reason` without
inventing another lifecycle; no dependent implementation starts while blocked or unapproved.

Statuses for every test: `PASS`, `FAIL`, `NOT TESTED`, `NEEDS HELP`. A missing hardware case is
`NOT TESTED` with reason **NOT TESTED — ENVIRONMENT LIMITATION**. It remains visible. A core release
gate cannot be waived by the agent; arrange another environment or obtain an explicit product scope
decision in DECISIONS before dependent/release approval. Conditional brightness/file-MIME cases can
be deferred only under the existing specification, with reason and owner acknowledgment.

## One checkpoint, end to end

1. Read progress, contract, affected spec sections and current code; reconcile drift before edits.
2. Validate dependencies and authorization. Open `checkpoint/<checkpoint-id>` from the prior
   checkpoint branch tip that contains its recorded approval, retaining its tested commit as
   `last_good_sha`. CP-00 starts from the reviewed workflow branch; its recovery target is `baseline_sha`.
3. For a visual checkpoint, activate its brief; owner submits references, agent inspects, owner grants
   Gate A. Record exact selected revision/hashes. No visual implementation before that point.
4. Implement one task at a time. Add meaningful regression coverage at risky seams; preserve old APIs.
   Do not run product services on the owner's session until [isolation](SAFETY.md) is proven.
5. Run [verification](VERIFICATION.md), review the diff, capture app evidence and known differences.
   Fix/retest failures; never edit a baseline solely to make a comparison green.
6. Fill the runtime handoff using [templates](TEMPLATES.md). Update owner notes if labels changed.
   Present a short description, exact tested revision and the owner's relevant tests.
7. Owner tests and approves or requests correction. Record the literal decision; commit the record.
   Preserve an approved Git SHA (optional local annotated `accepted/cp-NN` tag after approval).
8. Set active checkpoint to null, identify next eligible checkpoint and request only its missing
   owner inputs. Do not merge/push/release or change the live desktop without authorization.

## Continuity and Git discipline

`progress.json` contains a record per checkpoint. Task/test IDs are stable in the engineering and
owner documents; records refer to those IDs rather than duplicating checklists. For each test run append
command/scenario, result, UTC date, tested Git SHA plus dirty-tree patch hash if needed, environment,
evidence path and limitation. Never overwrite failure history. `latest_run` points to the handoff run.
`reference_sets` retains every selected/superseded set. `gate_a` and `gate_b` store owner quote, date,
chat/export or issue provenance, approved revision/run, and scope; an agent paraphrase is insufficient.
Owner messages can be copied by Codex into this record; owners need not edit JSON.
See [record fields and limitation handling](RECORD_FORMAT.md) for exact update conventions, subcases,
superseded reference approvals and invalidating downstream acceptance after a regression.

Before context loss record `next_agent_action`, `next_owner_action`, `blocked_reason`, branch,
last-good SHA, current task and runtime handoff/evidence paths. On resume inspect actual Git/files,
reverify recorded runtime handles, rerun stale checks if code/environment changed, and proceed from the
first incomplete eligible task. Do not trust a stale PID, chat claim or previous green test.
Keep small commits with checkpoint/task IDs and purpose, e.g. `cp-04: bound surface geometry`.
Never amend approved commits, reset the owner's tree or combine unrelated work.

Run `python3 tools/workflow.py --render` after progress changes, then `python3 tools/workflow.py`
and `git diff --check`. The helper catches structural drift; human review still checks engineering
scope, creative detail and scenario coverage. Only the approved product documents may change product
intent, through a recorded owner decision.

The existing CI also runs `python3 tools/test_workflow.py` and
`python3 tools/workflow.py --base-ref <PR-base-or-previous-push-SHA>`. Locally compare with the
previous recorded checkpoint/workflow commit before handoff. This rejects erased histories and
altered approved sets/runs; standalone validation cannot detect deletion from a previous version.
`--render` validates first and never repairs status or grants approval.

Commit product changes before the owner test, launch a clean pinned checkout of that full SHA,
and keep later evidence/progress commits separate. The tested commit excludes its later approval
record; this avoids a self-referential commit hash. A product change invalidates the current handoff.
Preserve the tested commit in branch ancestry, and do not rewrite accepted history.
If a PR is separately authorized, use the previous checkpoint branch as base until it is merged,
link the tested SHA/run, include verification and limitations, and compare the complete diff.
PR review, CI, Gate B, merge permission and publication permission are separate decisions.
This workflow review does not authorize creating a remote PR, pushing or merging.
