# CP-08 — Clipboard and file-workflow polish

Execution contract for roadmap milestone 8. **PLANNED initially; current truth is [progress.json](../progress.json).**
No task/test/approval result is asserted by this document. [Owner note](../../../owner/checkpoints/cp-08-clipboard.md) · [Visual brief](cp-08-clipboard.visual.md).

## Objective

Polish existing clipboard previews/search/pin/keyboard flows and small Shelf actions without replacing the watcher/store; evaluate true file MIME safely.

## Prerequisites

Approved cp-07-shelf; recorded authorization for this checkpoint.
Read the [workflow](../README.md), [safety procedure](../SAFETY.md), [verification](../VERIFICATION.md)
and relevant source before edits. All earlier required failures block dependent implementation.

## Authoritative specification references

[IMPLEMENTATION_PLAN](../../IMPLEMENTATION_PLAN.md), [V1_SPEC](../../V1_SPEC.md), [UX_DIRECTION](../../UX_DIRECTION.md), [ARCHITECTURE](../../ARCHITECTURE.md), [PORTABILITY](../../PORTABILITY.md), [DECISIONS](../../DECISIONS.md). Follow the matching milestone in IMPLEMENTATION_PLAN and relevant MUST/SHOULD clauses
in V1_SPEC; this contract does not replace those requirements. Consult inherited [API/plugins](../../k4-reference/README.md)
for touched compatibility behavior. If scope conflicts, stop that task and resolve the decision with the owner.

## In scope and affected modules

Current text/image storage/watchers with better preview/type/search/pin/copy/keyboard behavior and measured churn; password-manager exclusion tests; separate MIME feasibility for file offers, with conditional deferral.

`services/Clipboard.qml`, `tools/portapapeles.py`, `plugins/Clipboard/*`, Shelf actions and `services/Archivos.qml` helpers.

## Out of scope

No storage rewrite without proven blocker, duplicate watcher, universal secret-exclusion guarantee, fake file labels for plain paths, rich tags/OCR/source attribution or conversion suite.

## Implementation tasks

Statuses live only in progress.json. Complete one bounded task, verify it, then record its evidence.

| ID | Work | Proof IDs |
| --- | --- | --- |
| T01 | Verify clipboard boards and retained Shelf action grammar; record Gate A and conditional file-offer scope. | R01 |
| T02 | Add watcher/store/security/MIME fixtures; test actual harmless password-manager hints and file-manager offers before choosing file support. | A01, R02 |
| T03 | Apply shared preview/search/pin/keyboard/feedback states on current storage; implement only proven file offers and small cross-workflow actions. | A02, R03, M01, M02, M03 |
| T04 | Capture missing/secret/empty/error and scale/motion states; measure writes/watchers and document conditional deferrals accurately. | R04, M04, M05 |

## Acceptance criteria and proof mapping

| ID | Required outcome | Automated/runtime/owner proof |
| --- | --- | --- |
| AC01 | Existing clipboard works with distinct usable text/image hierarchy and keyboard access. | A01, A02, R03, M01, M02 |
| AC02 | Secret promises and file-reference support match actual MIME/durable-state evidence. | A01, R02, M03, M04 |
| AC03 | Restart/error/local-data behavior and shared visual system remain coherent without duplicate watchers. | A02, R04, M05 |

## Technical risks

Secret material in logs/screenshots/disk, new duplicate watchers, write churn, file-MIME confusion and overstating password-manager protection.

## Automated verification

Run all existing commands in [VERIFICATION](../VERIFICATION.md), then the following scoped checks.
New suites below are requirements for this future checkpoint, not commands claimed to exist today.
Record exact implemented commands/results, SHA and environment in the authoritative test records.

- **A01:** Existing gates plus current text/image index/search/pin/retention/error behavior, MIME hint exclusion with disk/log checks, actual file offer versus plain path, malformed/nonlocal/missing URIs.
- **A02:** Keyboard/search/copy/pin regressions, stable store migration, no duplicate watcher, bounded write churn and no network added by clipboard/Shelf actions.

## Runtime verification

- **R01:** Inspect board and approved prior grammar; owner Gate A.
- **R02:** Actual test password managers with harmless tokens and MIME observations; verify absence from durable index/payloads/logs where exclusion is claimed. File-manager offers receive independent GO/defer decision.
- **R03:** Text/image search/pin/copy/paste/delete, keyboard focus/selection/ESC and missing file actions if supported.
- **R04:** Restart/large history/long text/image decode failure/missing dependency, empty/error and scale/contrast/reduced motion; observe watcher count and storage churn.

Capture actual application states under `review/cp-08-clipboard/evidence/run-01/application/` for the first run;
later runs get new numbers. Keep logs/diffs/traces under `automated/` in the same run and use the
[handoff template](../TEMPLATES.md). Include tested SHA/tree, instance identity, recovery, limitations,
app-versus-reference differences where applicable and code-review findings. Pure fixtures/compilation
cannot prove runtime/focus/animation behavior.

## Owner requirements, visual references and manual tests

Supply text/image/pinned/empty/error boards in the shared style. Use harmless secret-like samples prepared by Codex, never real passwords.

Gate A is mandatory before visual code changes. Inspect every actual supplied image and storyboard; do not infer approval from filenames.
Use [this checkpoint’s complete brief](cp-08-clipboard.visual.md) and [personal tests](../../../owner/checkpoints/cp-08-clipboard.md).
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
