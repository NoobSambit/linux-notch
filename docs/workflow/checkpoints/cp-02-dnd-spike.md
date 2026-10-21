# CP-02 — Isolated Shelf drag-and-drop feasibility

Execution contract for roadmap milestone 2. **PLANNED initially; current truth is [progress.json](../progress.json).**
No task/test/approval result is asserted by this document. [Owner note](../../../owner/checkpoints/cp-02-dnd-spike.md) · [Visual brief](cp-02-dnd-spike.visual.md).

## Objective

Prove the real cross-application Wayland file-transfer promise before design or product integration depends on Shelf.

## Prerequisites

Approved cp-01-safety; recorded authorization for this checkpoint.
Read the [workflow](../README.md), [safety procedure](../SAFETY.md), [verification](../VERIFICATION.md)
and relevant source before edits. All earlier required failures block dependent implementation.

## Authoritative specification references

[IMPLEMENTATION_PLAN](../../IMPLEMENTATION_PLAN.md), [V1_SPEC](../../V1_SPEC.md), [DECISIONS](../../DECISIONS.md), [PORTABILITY](../../PORTABILITY.md), [DEPENDENCIES](../../DEPENDENCIES.md). Follow the matching milestone in IMPLEMENTATION_PLAN and relevant MUST/SHOULD clauses
in V1_SPEC; this contract does not replace those requirements. Consult inherited [API/plugins](../../k4-reference/README.md)
for touched compatibility behavior. If scope conflicts, stop that task and resolve the decision with the owner.

## In scope and affected modules

Throwaway layer-shell target/source; text/uri-list files, folders, multiple items, copy/move negotiation, drag-out, cancellation, missing source, keyboard fallback and same/multi-monitor matrix.

Disposable spike under ignored `scratch/`; inspect Qt Drag/DropArea and Quickshell PanelWindow on the installed versions. No edits to product modules.
Before handoff, preserve the minimal spike source (plain `.qml`/`.py`/script text), fixture generator,
exact launch command and version/MIME/action matrix under this checkpoint's tracked
`review/.../evidence/<run>/automated/spike/`. Execute only a disposable copy after isolation checks.
Verify another checkout can recreate the dummy files and run the same probe; ignored scratch content
must never be the only implementation of the experiment needed again at CP-07.

## Out of scope

No Shelf store, final design, Basket/global drag detection, fullscreen catcher, pointer polling, product integration or silent change to Shelf scope.

## Implementation tasks

Statuses live only in progress.json. Complete one bounded task, verify it, then record its evidence.

| ID | Work | Proof IDs |
| --- | --- | --- |
| T01 | Record Qt/Quickshell/Hyprland/file-manager versions and prepare dummy original hashes plus test destination. | A01 |
| T02 | Build a disposable source/target with event logging outside product modules; test URI parsing and negotiation without changing originals. | A01, R01, M01 |
| T03 | Exercise drag-in/out/copy/move refusal/cancel/missing source/keyboard using at least two available common file managers and a destination app. | R01, R02, M01, M02, M03 |
| T04 | Run screen crossing where practical and write exact GO or RESCOPE conclusion, limitations and recoverable spike evidence. | R03, M04 |

## Acceptance criteria and proof mapping

| ID | Required outcome | Automated/runtime/owner proof |
| --- | --- | --- |
| AC01 | Two file managers and another receiving app prove inbound/outbound local URI semantics. | A01, R01, M01 |
| AC02 | No original loss; cancellation/missing files and keyboard fallback are safe. | A01, R02, M02, M03 |
| AC03 | Feasibility decision and environment gaps are explicit; failed promise returns to owner product review before CP-03. | R03, M04 |

## Technical risks

Qt drag-source support on layer-shell, negotiated Move causing deletion, URL decoding/injection, common file-manager incompatibility and absent second app/display. Two-app proof is mandatory; unavailable apps leave the gate open.

## Automated verification

Run all existing commands in [VERIFICATION](../VERIFICATION.md), then the following scoped checks.
New suites below are requirements for this future checkpoint, not commands claimed to exist today.
Record exact implemented commands/results, SHA and environment in the authoritative test records.

- **A01:** Dummy-file hashes before/after, URI parsing cases (spaces/unicode/multiple lines/nonlocal/unsupported), copy-only action checks and cancellation logs; no network URI execution.

## Runtime verification

- **R01:** Version/MIME/action matrix for at least two common available file managers: file/folder/multiple files into layer-shell and drag-out to another app.
- **R02:** Requested copy/move, default copy, reject unsafe move, cancel before/after approach, missing source and equivalent keyboard route; originals remain intact.
- **R03:** Same-screen plus available cross-screen/fractional-scale cases; record exact go/rescope conclusion, not an assumed successful Shelf.

Capture actual application states under `review/cp-02-dnd-spike/evidence/run-01/application/` for the first run;
later runs get new numbers. Keep logs/diffs/traces under `automated/` in the same run and use the
[handoff template](../TEMPLATES.md). Include tested SHA/tree, instance identity, recovery, limitations,
app-versus-reference differences where applicable and code-review findings. Pure fixtures/compilation
cannot prove runtime/focus/animation behavior.

## Owner requirements, visual references and manual tests

No concept images. Use two available common file managers in the test session; Codex checks versions and prepares harmless files. Missing apps are recorded, not installed silently.

**No visual reference generation required for this checkpoint.** It validates engineering/runtime behavior rather than selecting a new appearance.
Use [this checkpoint’s complete brief](cp-02-dnd-spike.visual.md) and [personal tests](../../../owner/checkpoints/cp-02-dnd-spike.md).
Owner test IDs M01–M04 complement the proof table; Codex prepares data/tools and handles diagnosis.
Special hardware/software is declared in each test; missing capability stays NOT TESTED — ENVIRONMENT LIMITATION.

## Completion and approval gates

1. Confirm prerequisites/authorization (Gate A is not applicable) before implementing.
2. Finish scoped tasks with passing affected automation/runtime evidence and reviewed diff; keep failures/history.
3. Provide tested Start/Stop/Restore, real evidence, version/run and concise owner checklist; update owner notes
   if labels differ. Set AWAITING OWNER TEST only when required engineering gates are met.
4. Owner performs M tests and explicitly grants Gate B for that SHA/run. Unresolved failures block approval;
   untested cases remain untested, with the workflow’s explicit limitation rules. Never self-approve.
5. Record decision/provenance/results in progress.json, preserve last-good revision and regenerate owner progress.
   Prepare next eligible checkpoint inputs only. No live installation, push or publication implied.
