# Progress record conventions

`progress.json` is the only editable progress authority. Owner pages, checkpoint contracts and evidence
indexes must not maintain independent status tables. Codex edits the record and runs
`python3 tools/workflow.py --render`, then `python3 tools/workflow.py`. Owner messages are transcribed
by Codex, so the owner never needs to edit JSON.

## Updating a checkpoint

| Field | What to record |
| --- | --- |
| `status` | Lifecycle in README; all initially PLANNED. `blocked_reason` holds a concrete blocker without adding a second lifecycle. |
| `authorization` | Owner quote, UTC date, source and scope. No implementation before this and approved dependencies. |
| `tasks` | Stable T IDs, PENDING / IN PROGRESS / DONE; attach real evidence paths before DONE. |
| `tests` | Stable A/R/M IDs, kind, latest result/reason and append-only `history`. Never overwrite a failure to hide it. |
| `reference_requirements` | Mandatory semantic slots and recommended first-revision filenames/folders from the visual brief. |
| `reference_sets` | Set IDs r01/r02 etc., exact selected files, original source paths, SHA256 and actual image-inspection findings. Keep superseded sets and their approval records. |
| `gate_a` | Current explicit owner decision: `owner_quote`, `date`, `source`, `set_id`; null until approved. Preserve old decision with its superseded set before replacement. |
| `runs` | Run ID, tested revision/tree, environment, evidence inventory/handoff, comparisons, code-review findings and unresolved limitations. |
| `latest_run` | ID of the exact current handoff run, e.g. run-02; never silently point to an older passing run. |
| `gate_b` | Owner words/date/source, `revision` and `run`; null until the actual tested app is approved. |
| Continuity fields | Branch, `last_good_sha`, `current_task`, `next_agent_action`, `next_owner_action`, blocker; runtime identity lives in the linked handoff. |

Each test-history entry needs `result`, `date`, `revision`, `environment`, `evidence` and `run`, plus
the exact command/exit code for automation or steps/observed result for runtime/owner tests. Evidence
paths must be real and readable; media needs capture provenance. Latest result/reason summarize the
last applicable history entry. A fresh code/environment change invalidates affected prior results;
set them NOT TESTED with reason until rerun, retaining their history.

For each selected reference-set file record `requirement` (the original recommended slot filename),
`path` (the actual immutable approved file), `source_path` and `sha256`. A revised file may use r02 or
jpg/webp while its requirement slot stays stable. The set's `inspection` records date, tool used to
decode/open every image, completeness/feasibility checks and agreed differences. The helper only checks
headers/hashes; an agent must actually view the images. Submission uses candidate files; no need to copy
to approved until the owner decides. Then preserve the originals and copy the exact selected bytes.

## Limits, corrections and stale approval

Split hardware/conditional subcases into child test IDs when useful, e.g. R03-2-display, so a passing
single-display check does not hide an unperformed two-display scenario. Document extra cases in the
contract/owner note as appropriate. Keep the missing case `NOT TESTED` with reason
`NOT TESTED — ENVIRONMENT LIMITATION: ...`.

All declared cases are required by default. Only an existing spec-conditional case, or an explicit
owner-approved product scope change recorded in DECISIONS, may be treated as nonblocking. Record
`required: false` and `disposition` with owner_quote/date/source/spec_reference/reason. It still stays
NOT TESTED; FAIL and NEEDS HELP cannot be waived by this mechanism. Required core display/privacy/data
gates need actual proof in another environment. A convenience skip is not a scope decision.

If the owner requests changes, clear current Gate B into an approval-history record, return to
IMPLEMENTING and append a new run after correction. Reopen Gate A for material visual changes and
preserve the old set/decision. Revalidate already approved downstream checkpoints affected by a regression;
keep their historical acceptance but clear current approval, invalidate affected tests and close dependent
work until retested. Update top-level active/next fields accordingly. Do not leave a stale APPROVED claim.

When every checkpoint is approved, active/next may both be null. This does not authorize publication.
The helper validates structural consistency, not truth of owner words, adequacy of a scope decision or
actual runtime behavior; those require the agent's source/evidence review and explicit owner decisions.
