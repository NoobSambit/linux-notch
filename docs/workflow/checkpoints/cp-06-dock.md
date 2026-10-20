# CP-06 — Dock and Hybrid polish

Execution contract for roadmap milestone 6. **PLANNED initially; current truth is [progress.json](../progress.json).**
No task/test/approval result is asserted by this document. [Owner note](../../../owner/checkpoints/cp-06-dock.md) · [Visual brief](cp-06-dock.visual.md).

## Objective

Polish existing Dual dock/Hybrid behavior with approved shared visuals, stable task state and shorter default motion.

## Prerequisites

Approved cp-05-activities; recorded authorization for this checkpoint.
Read the [workflow](../README.md), [safety procedure](../SAFETY.md), [verification](../VERIFICATION.md)
and relevant source before edits. All earlier required failures block dependent implementation.

## Authoritative specification references

[IMPLEMENTATION_PLAN](../../IMPLEMENTATION_PLAN.md), [V1_SPEC](../../V1_SPEC.md), [UX_DIRECTION](../../UX_DIRECTION.md), [ARCHITECTURE](../../ARCHITECTURE.md), [K4_MIGRATION_PLAN](../../K4_MIGRATION_PLAN.md). Follow the matching milestone in IMPLEMENTATION_PLAN and relevant MUST/SHOULD clauses
in V1_SPEC; this contract does not replace those requirements. Consult inherited [API/plugins](../../k4-reference/README.md)
for touched compatibility behavior. If scope conflicts, stop that task and resolve the decision with the owner.

## In scope and affected modules

Reuse Dual state, task/pin order and previews; focus/drawer/drag interactions; reserve reflow and Hybrid activity reachability; shorter default transition/reduced-motion with opt-in expressive travel.

`plugins/Dual/DualPlugin.qml`, `Muelle.qml`, `Escena.qml`, `Caida.qml`, `Gota.qml`, host and settings; repeated Hyprland focus/window seams.

## Out of scope

No replacement dock, new window manager, fullscreen input catcher without proof, independent activity owner or new app store.

## Implementation tasks

Statuses live only in progress.json. Complete one bounded task, verify it, then record its evidence.

| ID | Work | Proof IDs |
| --- | --- | --- |
| T01 | Verify dock references and continuity with CP-03/04/05; record Gate A and intended default/optional motion. | R01 |
| T02 | Separate only necessary dock state and transition coupling; preserve pins/order/window activation and compatible IPC. | A01 |
| T03 | Apply shared tokens/states to drawer/previews/task feedback and Hybrid; implement short/default/reduced-motion transitions. | R02, M01, M02 |
| T04 | Check reflow, rapid transitions/cancel, display/fullscreen and resource/input traces; compare real implementation. | R03, M03, M04 |

## Acceptance criteria and proof mapping

| ID | Required outcome | Automated/runtime/owner proof |
| --- | --- | --- |
| AC01 | Existing pins, order and window actions survive restart/mode switches. | A01, R02, M01, M02 |
| AC02 | Hybrid keeps tasks and activity reachable; transitions never block input. | R02, R03, M02, M03 |
| AC03 | Approved hierarchy, reduced motion and measured hidden/transition costs satisfy handoff. | R01, R03, M04 |

## Technical risks

Transition windows intercepting input, stale Hyprland client identity/focus, polling while hidden and pins disappearing on mode changes.

## Automated verification

Run all existing commands in [VERIFICATION](../VERIFICATION.md), then the following scoped checks.
New suites below are requirements for this future checkpoint, not commands claimed to exist today.
Record exact implemented commands/results, SHA and environment in the authoritative test records.

- **A01:** Existing gates plus pin/order persistence, app/window identity/parser/IPC, disabled-dock watcher behavior and rapid mode-change/cancel state transitions.

## Runtime verification

- **R01:** Read dock boards/storyboard and exact CP-03 lineage; owner Gate A.
- **R02:** Pin/unpin/reorder by pointer and keyboard route; multiple-window focus/previews/drawer and Hybrid simultaneous activity.
- **R03:** Top/bottom reserve/overlay/fullscreen/hotplug/scale; repeated/aborted mode transitions; no invisible input catcher; reduced motion and CPU/GPU/frame/hidden polling traces.

Capture actual application states under `review/cp-06-dock/evidence/run-01/application/` for the first run;
later runs get new numbers. Keep logs/diffs/traces under `automated/` in the same run and use the
[handoff template](../TEMPLATES.md). Include tested SHA/tree, instance identity, recovery, limitations,
app-versus-reference differences where applicable and code-review findings. Pure fixtures/compilation
cannot prove runtime/focus/animation behavior.

## Owner requirements, visual references and manual tests

Supply dock/task states and mode-transition storyboard derived from previous approved visuals.

Gate A is mandatory before visual code changes. Inspect every actual supplied image and storyboard; do not infer approval from filenames.
Use [this checkpoint’s complete brief](cp-06-dock.visual.md) and [personal tests](../../../owner/checkpoints/cp-06-dock.md).
Owner test IDs M01–M04 complement the proof table; Codex prepares data/tools and handles diagnosis.
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
