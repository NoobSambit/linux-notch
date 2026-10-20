# CP-10 — Compatibility, performance and release validation

Execution contract for roadmap milestone 10. **PLANNED initially; current truth is [progress.json](../progress.json).**
No task/test/approval result is asserted by this document. [Owner note](../../../owner/checkpoints/cp-10-release.md) · [Visual brief](cp-10-release.visual.md).

## Objective

Validate the assembled v1 against core/inherited support tiers, privacy, performance, compatibility and per-payload distribution rights; prepare an explicit owner release decision.

## Prerequisites

Approved cp-09-coherence; recorded authorization for this checkpoint.
Read the [workflow](../README.md), [safety procedure](../SAFETY.md), [verification](../VERIFICATION.md)
and relevant source before edits. All earlier required failures block dependent implementation.

## Authoritative specification references

[IMPLEMENTATION_PLAN](../../IMPLEMENTATION_PLAN.md), [V1_SPEC](../../V1_SPEC.md), [V1_EXPERIENCE](../../V1_EXPERIENCE.md), [ARCHITECTURE](../../ARCHITECTURE.md), [K4_MIGRATION_PLAN](../../K4_MIGRATION_PLAN.md), [UPSTREAM_SYNC](../../UPSTREAM_SYNC.md), [DEPENDENCIES](../../DEPENDENCIES.md), [PORTABILITY](../../PORTABILITY.md), [ASSET_LICENSE_AUDIT](../../ASSET_LICENSE_AUDIT.md), [DECISIONS](../../DECISIONS.md). Follow the matching milestone in IMPLEMENTATION_PLAN and relevant MUST/SHOULD clauses
in V1_SPEC; this contract does not replace those requirements. Consult inherited [API/plugins](../../k4-reference/README.md)
for touched compatibility behavior. If scope conflicts, stop that task and resolve the decision with the owner.

## In scope and affected modules

Core E2E gates, supported inherited smoke, optional enabled non-regression, plugin lifecycle/API/IPC, live notification switching, local data/privacy, reproducible CPU/RSS/GPU/frame comparisons and rights resolution; release/recovery checklist.

Whole integrated v1, sample/external plugins, installers/manual dependency documentation, asset manifests/notices and all existing CI/targeted tests.

## Out of scope

No new features/platforms, unresolved required gates waved through, automatic publishing/tagging/pushing or new style. Material visual fixes reopen the originating Gate A; runtime corrections remain scoped and retested.

## Implementation tasks

Statuses live only in progress.json. Complete one bounded task, verify it, then record its evidence.

| ID | Work | Proof IDs |
| --- | --- | --- |
| T01 | Freeze candidate SHA/environment; run existing/added suites and plugin samples/hot reload/error/disabled tests; review any upstream port provenance. | A01, R01 |
| T02 | Run full daily core scenario/display/fullscreen/accessibility/notification/privacy matrix and tiered inherited checks. | A02, R02, M01, M02, M03 |
| T03 | Measure idle/media/dock/transition/closed optional-module costs against baseline and resolve resource regressions with evidence. | R03, M04 |
| T04 | Resolve per-payload rights/notices or owner-approved release exclusion; rehearse manual install/dependency guide and rollback in isolation; request Gate B and separate publication decision. | A03, R04, M05 |

## Acceptance criteria and proof mapping

| ID | Required outcome | Automated/runtime/owner proof |
| --- | --- | --- |
| AC01 | All core gates pass on exact candidate; inherited compatibility and caused regressions resolved. | A01, A02, R01, R02, M01, M02, M03 |
| AC02 | Measured resource/accessibility/privacy behavior meets recorded product decisions. | A02, R02, R03, M04 |
| AC03 | Rights, dependencies and safe recovery have evidence; owner release acceptance is distinct from permission to publish. | A03, R04, M05 |

## Technical risks

Aggregate green gates hiding lifecycle/privacy gaps, release assets without provenance, expensive hidden watchers, unavailable hardware silently treated as passing, stale candidate after fixes and distribution without permission.

## Automated verification

Run all existing commands in [VERIFICATION](../VERIFICATION.md), then the following scoped checks.
New suites below are requirements for this future checkpoint, not commands claimed to exist today.
Record exact implemented commands/results, SHA and environment in the authoritative test records.

- **A01:** All inherited and new focused gates on exact candidate; examples hola/piezas/efectos/snake and owner-supplied external plugin when available; hot reload/failure/disabled/IPC/settings contracts.
- **A02:** Local Shelf/clipboard durable-state/privacy/secret tests, no telemetry in core, network disclosure/control, migration defaults, owner loss/race and monitor parser coverage.
- **A03:** Per-file asset/data/font/icon/shader/source notices/provenance decisions and manual logical dependency list; unresolved payload cannot enter distributable artifact.

## Runtime verification

- **R01:** Actual plugin lifecycle/IPC/legacy theme compatibility and optional external plugin supplied by owner; missing external sample explicitly recorded.
- **R02:** Complete daily core flow across modes/top/bottom, one/two displays/fractional scale/fullscreen/hotplug, accessibility/reduced motion and real Own/External switching; supported/optional tier checks.
- **R03:** Matching baseline resource workloads/duration/hardware, idle/active/closed states and severe regression resolution; accepted real-app screenshot comparisons, frame/motion traces.
- **R04:** Manual dependency/install path and missing optional tools in disposable environment; backup/stop/rollback rehearsal; verify final distributable inventory/notices without publishing.

Capture actual application states under `review/cp-10-release/evidence/run-01/application/` for the first run;
later runs get new numbers. Keep logs/diffs/traces under `automated/` in the same run and use the
[handoff template](../TEMPLATES.md). Include tested SHA/tree, instance identity, recovery, limitations,
app-versus-reference differences where applicable and code-review findings. Pure fixtures/compilation
cannot prove runtime/focus/animation behavior.

## Owner requirements, visual references and manual tests

No new concept images. Perform the final short daily-use checklist and decide whether the tested release candidate is acceptable. Publishing needs separate explicit permission.

**No visual reference generation required for this checkpoint.** It validates engineering/runtime behavior rather than selecting a new appearance.
Use [this checkpoint’s complete brief](cp-10-release.visual.md) and [personal tests](../../../owner/checkpoints/cp-10-release.md).
Owner test IDs M01–M05 complement the proof table; Codex prepares data/tools and handles diagnosis.
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
