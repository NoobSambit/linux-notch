# CP-00 — Safe environment and original k4 baseline

Execution contract for roadmap milestone 0. **PLANNED initially; current truth is [progress.json](../progress.json).**
No task/test/approval result is asserted by this document. [Owner note](../../../owner/checkpoints/cp-00-baseline.md) · [Visual brief](cp-00-baseline.visual.md).

## Objective

Establish a reproducible, isolated original-k4 baseline and a rehearsed recovery path before changing product behavior.

## Prerequisites

Explicit workflow and CP-00 authorization from owner; no implementation authority is recorded yet.
Read the [workflow](../README.md), [safety procedure](../SAFETY.md), [verification](../VERIFICATION.md)
and relevant source before edits. All earlier required failures block dependent implementation.

## Authoritative specification references

[IMPLEMENTATION_PLAN](../../IMPLEMENTATION_PLAN.md), [V1_SPEC](../../V1_SPEC.md), [K4_MIGRATION_PLAN](../../K4_MIGRATION_PLAN.md), [DEPENDENCIES](../../DEPENDENCIES.md), [ASSET_LICENSE_AUDIT](../../ASSET_LICENSE_AUDIT.md), [UPSTREAM_SYNC](../../UPSTREAM_SYNC.md). Follow the matching milestone in IMPLEMENTATION_PLAN and relevant MUST/SHOULD clauses
in V1_SPEC; this contract does not replace those requirements. Consult inherited [API/plugins](../../k4-reference/README.md)
for touched compatibility behavior. If scope conflicts, stop that task and resolve the decision with the owner.

## In scope and affected modules

Inventory installed capabilities; prepare disposable code/state and isolated Hyprland/session services; capture current modes, inherited features and resource use; start rights inventory. Do not patch product behavior.

`arrancar`, `instalar` (inspection only), `shell.qml`, `api/K4/Paths.qml`, `services/Settings.qml`, `services/PluginManager.qml`, `services/Notifs.qml`, existing `screenshots/` and plugin examples.

## Out of scope

No Notchbar features, theme changes, baseline bug repairs, installer execution, package installation, autostart edits or personal config migration.

## Implementation tasks

Statuses live only in progress.json. Complete one bounded task, verify it, then record its evidence.

| ID | Work | Proof IDs |
| --- | --- | --- |
| T01 | Inventory source baseline, versions, devices, state paths, daemon ownership and dependencies; identify isolation hazards from source. | A01 |
| T02 | Prepare and prove separate test code/home/bus/Wayland context; supply guarded Start/Stop/Restore actions and rehearse dummy-state backup/restore. | R01, M01 |
| T03 | Capture original surface/dock top/bottom and compatibility-only sides, fullscreen and available displays; smoke media, clipboard, capture and plugin samples. | R02, M02, M03 |
| T04 | Measure idle/startup/media/dock and Atalaya effective enabled/closed costs; inventory provenance gaps and prepare baseline handoff. | R03, M04 |

## Acceptance criteria and proof mapping

| ID | Required outcome | Automated/runtime/owner proof |
| --- | --- | --- |
| AC01 | Isolation and exact-instance stop/restore work; personal state and daemon remain intact. | A01, R01, M01 |
| AC02 | Original behavior and known defects are documented, including unsupported hardware and optional dependencies. | R02, M02, M03 |
| AC03 | Reproducible resource baseline, Atalaya state and initial rights gaps exist. | R03, M04 |

## Technical risks

Hardcoded HOME state, session D-Bus/clipboard leakage, global installer kills, optional dependencies, unlicensed inherited media, and missing second display. A source audit is not live proof.

## Automated verification

Run all existing commands in [VERIFICATION](../VERIFICATION.md), then the following scoped checks.
New suites below are requirements for this future checkpoint, not commands claimed to exist today.
Record exact implemented commands/results, SHA and environment in the authoritative test records.

- **A01:** Run existing gates and read-only capability/path audit; record missing tools and skipped qmllint separately.

## Runtime verification

- **R01:** Prove isolated paths/services, exact-instance termination, backup and previous-version restore using dummy state; host services unchanged.
- **R02:** Record original top/bottom/dock, experimental sides, fullscreen, one/two displays where available, media/clipboard/capture and examples hola/piezas/efectos/snake.
- **R03:** Measure startup/idle/active resources with workload/duration/hardware; record Atalaya saved override versus inherited catalog effective state and closed-state GPU activity.

Capture actual application states under `review/cp-00-baseline/evidence/run-01/application/` for the first run;
later runs get new numbers. Keep logs/diffs/traces under `automated/` in the same run and use the
[handoff template](../TEMPLATES.md). Include tested SHA/tree, instance identity, recovery, limitations,
app-versus-reference differences where applicable and code-review findings. Pure fixtures/compilation
cannot prove runtime/focus/animation behavior.

## Owner requirements, visual references and manual tests

Explicitly approve this workflow and authorize CP-00 only. Codex will check available test-session options and ask only if a real session action is needed.

**No visual reference generation required for this checkpoint.** It validates engineering/runtime behavior rather than selecting a new appearance.
Use [this checkpoint’s complete brief](cp-00-baseline.visual.md) and [personal tests](../../../owner/checkpoints/cp-00-baseline.md).
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
