# CP-07 — Local Shelf implementation

Execution contract for roadmap milestone 7. **PLANNED initially; current truth is [progress.json](../progress.json).**
No task/test/approval result is asserted by this document. [Owner note](../../../owner/checkpoints/cp-07-shelf.md) · [Visual brief](cp-07-shelf.visual.md).

## Objective

Build the local staging Shelf only after the positive CP-02 proof, using safe references/copy semantics and existing host/shared components.

## Prerequisites

Approved cp-06-dock; recorded authorization for this checkpoint.  Positive CP-02 DnD evidence revalidated on current versions; CP-03–05 design/geometry/activity approvals remain applicable.
Read the [workflow](../README.md), [safety procedure](../SAFETY.md), [verification](../VERIFICATION.md)
and relevant source before edits. All earlier required failures block dependent implementation.

## Authoritative specification references

[IMPLEMENTATION_PLAN](../../IMPLEMENTATION_PLAN.md), [V1_SPEC](../../V1_SPEC.md), [V1_EXPERIENCE](../../V1_EXPERIENCE.md), [UX_DIRECTION](../../UX_DIRECTION.md), [ARCHITECTURE](../../ARCHITECTURE.md), [DECISIONS](../../DECISIONS.md), [PORTABILITY](../../PORTABILITY.md). Follow the matching milestone in IMPLEMENTATION_PLAN and relevant MUST/SHOULD clauses
in V1_SPEC; this contract does not replace those requirements. Consult inherited [API/plugins](../../k4-reference/README.md)
for touched compatibility behavior. If scope conflicts, stop that task and resolve the decision with the owner.

## In scope and affected modules

Local file/folder/multi-item URI staging; copy-default drag-out; open/reveal/copy-path/remove/clear and optional pin; keyboard route; atomic metadata/retention/missing paths; small action availability contract.

New small Shelf module/local metadata store, host/settings integration and reusable actions from `services/Archivos.qml`; existing plugin lifecycle.

## Out of scope

No product work without positive CP-02 gate; no Basket/shake, cloud/upload, conversion/OCR suite, duplicate originals by default, silent move or file-manager replacement.

## Implementation tasks

Statuses live only in progress.json. Complete one bounded task, verify it, then record its evidence.

| ID | Work | Proof IDs |
| --- | --- | --- |
| T01 | Revalidate CP-02 matrix on current runtime; verify Shelf references against feasible semantics; record Gate A. | A01, R01 |
| T02 | Implement atomic local reference metadata, validation/retention/pin and small safe action handlers; preserve originals. | A01 |
| T03 | Integrate visible drag target/cards/keyboard entry with one host and shared design; add copy-default in/out and clear/missing feedback. | R02, M01, M02, M03 |
| T04 | Test crash/restart/cancel/unavailable sources and monitor/fullscreen/reduced motion; inspect network/local data and compare actual evidence. | A02, R03, M04, M05 |

## Acceptance criteria and proof mapping

| ID | Required outcome | Automated/runtime/owner proof |
| --- | --- | --- |
| AC01 | Shelf uses tested local-reference/copy semantics without altering originals. | A01, R01, R02, M01, M02 |
| AC02 | All core actions have keyboard access and truthful availability/missing states. | A01, R02, R03, M03, M04 |
| AC03 | Restart/retention/local privacy and approved motion/visual states work. | A01, A02, R03, M04, M05 |

## Technical risks

Source deletion or implicit Move, untrusted URI/path execution, symlink/missing permissions, stale metadata after crashes, excessive retention and apparent production rights from concept images.

## Automated verification

Run all existing commands in [VERIFICATION](../VERIFICATION.md), then the following scoped checks.
New suites below are requirements for this future checkpoint, not commands claimed to exist today.
Record exact implemented commands/results, SHA and environment in the authoritative test records.

- **A01:** Existing gates plus URI/security/file/folder/multiple/duplicate/path quoting, missing/unreadable/symlink cases, atomic writes, interrupted/corrupt store, pin/retention and action availability; original hashes unchanged.
- **A02:** Shelf actions create no network request themselves; store/metadata remain local, remove/clear do not unlink originals; disabled Shelf has no watcher work.

## Runtime verification

- **R01:** Positive CP-02 recheck with current versions; inspect owner references and Gate A.
- **R02:** Two proven file-manager flows drag in/out, copy/move negotiation, approach/cancel/collapse; open/reveal/copy path/remove/clear and keyboard equivalents.
- **R03:** Restart retention/pin, source deleted/moved/permission denied, interrupted copy/cancel, unsupported source, fullscreen/display rehome/scale/reduced-motion and original integrity.

Capture actual application states under `review/cp-07-shelf/evidence/run-01/application/` for the first run;
later runs get new numbers. Keep logs/diffs/traces under `automated/` in the same run and use the
[handoff template](../TEMPLATES.md). Include tested SHA/tree, instance identity, recovery, limitations,
app-versus-reference differences where applicable and code-review findings. Pure fixtures/compilation
cannot prove runtime/focus/animation behavior.

## Owner requirements, visual references and manual tests

Generate Shelf states and approach/open/collapse storyboard; use only dummy files during tests.

Gate A is mandatory before visual code changes. Inspect every actual supplied image and storyboard; do not infer approval from filenames.
Use [this checkpoint’s complete brief](cp-07-shelf.visual.md) and [personal tests](../../../owner/checkpoints/cp-07-shelf.md).
Owner test IDs M01–M05 complement the proof table; Codex prepares data/tools and handles diagnosis.
Special hardware/software is declared in each test; missing capability stays NOT TESTED — ENVIRONMENT LIMITATION.

## Completion and approval gates

1. Confirm prerequisites/authorization and exact owner Gate A reference set before implementing.
2. Finish scoped tasks with passing affected automation/runtime evidence and reviewed diff; keep failures/history.
3. Provide tested Start/Stop/Restore, real evidence, version/run and concise owner checklist; update owner notes
   if labels differ. Set AWAITING OWNER TEST only when required engineering gates are met.
4. Owner performs M tests and explicitly grants Gate B for that SHA/run. Unresolved failures block approval;
   untested cases remain untested, with the workflow’s explicit limitation rules. Never self-approve.
5. Record decision/provenance/results in progress.json, preserve last-good revision and regenerate owner progress.
   Prepare next eligible checkpoint inputs only. No live installation, push or publication implied.
