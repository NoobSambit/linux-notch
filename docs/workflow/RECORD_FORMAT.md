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
| `tasks` | Stable T IDs, PENDING / IN PROGRESS / DONE; attach hashed evidence objects before DONE. One IN PROGRESS task matches `current_task`. |
| `tests` | Stable A/R/M IDs, kind, latest result/reason and append-only `history`. Never overwrite a failure to hide it. |
| `reference_requirements` | Mandatory semantic slots and recommended first-revision filenames/folders from the visual brief. |
| `reference_sets` | Set IDs r01/r02 etc., exact selected files, original source paths, SHA256 and actual image-inspection findings. Keep superseded sets and their approval records. |
| `gate_a` | Current explicit owner decision: `owner_quote`, UTC `date`, `source`, `set_id`, `design_spec_sha256`; null until approved. Archive the exact old decision before replacement. |
| `runs` | Run ID, tested revision/tree, environment, evidence inventory/handoff, comparisons, code-review findings and unresolved limitations. |
| `latest_run` | ID of the exact current handoff run, e.g. run-02; never silently point to an older passing run. |
| `gate_b` | Owner words/date/source, `revision` and `run`; null until the actual tested app is approved. |
| Continuity fields | Branch, `last_good_sha`, `current_task`, `next_agent_action`, `next_owner_action`, blocker; runtime identity lives in the linked handoff. |

`schema_version` is 1. `workflow_status` is `AWAITING WORKFLOW APPROVAL`, `IN PROGRESS`, or
`CHECKPOINTS APPROVED`. CP-00 authorization includes the explicit workflow decision. Only one
checkpoint may be active; `active_checkpoint` matches its lifecycle, and `next_checkpoint` identifies
the first checkpoint not APPROVED (including the active one). Nonvisual checkpoints skip reference states.
Record the exact branch `checkpoint/<checkpoint-id>` and a full, locally available `last_good_sha`
before activation. `blocked_reason` prevents readiness/approval and dependent work.

Each test-history entry needs `result`, UTC `date`, `revision`, `environment`, `evidence` and `run`, plus
the exact command/exit code for automation or steps/observed result for runtime/owner tests. Evidence
paths must be real and readable; media needs capture provenance. Latest result/reason summarize the
last applicable history entry. A fresh code/environment change invalidates affected prior results;
set them NOT TESTED with reason until rerun, retaining their history.

Dates use ISO 8601 with UTC, e.g. `2026-10-20T12:00:00Z`. `revision` is a full Git commit SHA;
`environment` is a nonempty snapshot description (versions, hardware/display/scale and isolation ID).
Every history entry's revision/environment and optional patch must match its declared run.
All current results other than NOT TESTED must belong to `latest_run`, the last appended run.
Recheck each gate for a new handoff; do not copy an old PASS or invent a rerun. Any reuse requires
an actual applicability review recorded as the current check, including its original proof and limits.
Tests of runtime behavior affected by code/environment changes require a real rerun.

Evidence is a list of objects: `{"path": "review/.../proof.md", "sha256": "<64 hex digits>"}`.
This applies to task evidence and history entries. Store sanitized readable files in Git, stage their
exact bytes before validation, then commit them before handoff. The checker verifies working-tree and
index bytes. `.gitkeep`, private material and missing local-only media cannot satisfy a proof entry.
Refer to large recordings through a tracked retrieval manifest as described in [review policy](../../review/README.md).

A run is appended with this shape (illustrative placeholders, never real approval):

```json
{
  "id": "run-01",
  "date": "2026-10-20T12:00:00Z",
  "revision": "<full tested commit SHA>",
  "environment": "<versions, hardware, displays, scale, isolation>",
  "handoff": {"path": "review/<checkpoint>/evidence/run-01/index.md", "sha256": "<hash>"},
  "review": {"path": "review/<checkpoint>/evidence/run-01/automated/diff-review.md", "sha256": "<hash>"},
  "recovery": {"path": "review/<checkpoint>/evidence/run-01/automated/recovery.md", "sha256": "<hash>"}
}
```

The three documents are mandatory at AWAITING OWNER TEST/APPROVED and contain the corresponding
[template](TEMPLATES.md) details, including observed Start/Stop/Restore outcomes. A visual run also has
`reference_set` and a hashed `comparison` document. Exploratory runs may omit handoff documents and
record `patch` as a hashed patch artifact (including new files), but owner testing uses a clean commit.
Collect provisional files in a new run directory, then append the finalized run and its test histories
together. Freeze each run record once appended; add owner results as test-history entries and separate files,
without rewriting the run index. Use a new run for changed code, environment or handoff instructions.
Archive old test runs even when failed. A hash proves file identity, not the truth of its contents.

For each selected reference-set file record `requirement` (the original recommended slot filename),
`path` (the actual immutable approved file), `source_path` and `sha256`. A revised file may use r02 or
jpg/webp while its requirement slot stays stable. The set's `inspection` records date, tool used to
decode/open every image, completeness/feasibility checks and agreed differences. The helper only checks
headers/hashes; an agent must actually view the images. Each selected set also has a hashed `design_spec`
artifact using the [design translation template](TEMPLATES.md#design-translation-before-gate-a).
Its hash is bound to Gate A; later sets retain earlier lineage without overwriting files.
At REFERENCES SUBMITTED, `submission` inventories every mandatory slot using
`requirement`, `path`, `sha256`; track reviewed candidate copies explicitly because their folders are
ignored by default. At AWAITING VISUAL APPROVAL, `proposed_design_spec` names the hashed interpretation
shown to the owner. No need to copy to approved until the owner decides. Then preserve originals,
copy the exact selected bytes and design interpretation, and record Gate A.
If originals exceed the media limit, prepare lightweight candidates and have the owner approve those
exact copies before recording their hashes; do not compress an already approved set in place.

## Limits, corrections and stale approval

Split mixed required/conditional hardware cases into child test IDs, e.g. R03-2-display, before testing, so a passing
single-display check does not hide an unperformed two-display scenario. Document extra cases in the
contract/owner note as appropriate (same `- **R03-2-display:**` or `### M03-2-display — ...` format).
Keep the parent required; it only passes when all its named required scenarios pass. Do not mark an
entire multi-scenario test optional because one child is conditional. Keep the missing case `NOT TESTED` with reason
`NOT TESTED — ENVIRONMENT LIMITATION: ...`.

All declared cases are required by default. Only an existing spec-conditional case, or an explicit
owner-approved product scope change recorded in DECISIONS, may be treated as nonblocking. Record
`required: false` and `disposition` with owner_quote/date/source/spec_reference/reason and a hashed
`evidence` object containing the decision. `spec_reference` is a repository-relative spec/DECISIONS
path plus optional heading. It still stays
NOT TESTED; FAIL and NEEDS HELP cannot be waived by this mechanism. Required core display/privacy/data
gates need actual proof in another environment. A convenience skip is not a scope decision.

If the owner requests changes, append `{"gate": "gate_b", "decision": <exact old object>,
"date": <UTC>, "reason": <why>}` to `approval_history`, clear current Gate B, return to
IMPLEMENTING and append a new run after correction. Reopen Gate A for material visual changes and
archive its old decision with `gate: "gate_a"`; return to AWAITING REFERENCES for new materials.
Retain all old sets, invalidate results, and record the reapproval blocker. Unchanged completed tasks
may remain DONE as historical work while that blocker and approval history are present; reset tasks
requiring new implementation to PENDING. Revalidate approved downstream checkpoints affected by a regression: archive their
Gate B, clear it, return those records to PLANNED with `blocked_reason`, set test results NOT TESTED with
invalidation reasons and preserve their completed tasks/evidence as historical work. Only such suspended
records may retain DONE tasks in PLANNED. No IN PROGRESS task remains in a suspended record.
Resume them in order after prerequisites are approved again. Keep affected dependents closed until retested.
Update active/next to the earliest correction. Do not leave a stale APPROVED claim.

When every checkpoint is approved, active/next may both be null. This does not authorize publication.
The helper validates structural consistency, not truth of owner words, adequacy of a scope decision or
actual runtime behavior; those require the agent's source/evidence review and explicit owner decisions.
