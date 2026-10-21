# CP-04 — Four surface modes, geometry and displays

Execution contract for roadmap milestone 4. **PLANNED initially; current truth is [progress.json](../progress.json).**
No task/test/approval result is asserted by this document. [Owner note](../../../owner/checkpoints/cp-04-surfaces.md) · [Visual brief](cp-04-surfaces.visual.md).

## Objective

Implement bounded four-mode geometry and safe display/fullscreen behavior using the existing host and approved visual language.

## Prerequisites

Approved cp-03-design-system; recorded authorization for this checkpoint.
Read the [workflow](../README.md), [safety procedure](../SAFETY.md), [verification](../VERIFICATION.md)
and relevant source before edits. All earlier required failures block dependent implementation.

## Authoritative specification references

[IMPLEMENTATION_PLAN](../../IMPLEMENTATION_PLAN.md), [V1_SPEC](../../V1_SPEC.md), [V1_EXPERIENCE](../../V1_EXPERIENCE.md), [UX_DIRECTION](../../UX_DIRECTION.md), [ARCHITECTURE](../../ARCHITECTURE.md), [K4_MIGRATION_PLAN](../../K4_MIGRATION_PLAN.md), [DECISIONS](../../DECISIONS.md). Follow the matching milestone in IMPLEMENTATION_PLAN and relevant MUST/SHOULD clauses
in V1_SPEC; this contract does not replace those requirements. Consult inherited [API/plugins](../../k4-reference/README.md)
for touched compatibility behavior. If scope conflicts, stop that task and resolve the decision with the owner.

## In scope and affected modules

Four modes, supported top/bottom, bounded dimensions/alignment/offset/radius, reserve/overlay, preferred/focused display, one expanded owner, hotplug rehome and bad-JSON recovery; narrow repeated Hyprland seam only where justified.

`shell.qml`, `services/Island.qml`, `services/Settings.qml`, `services/Workspaces.qml`, `plugins/Dual/*`, `plugins/Settings/PrevioIsland.qml`, `api/K4/Isla.qml`.

## Out of scope

No second host, free desktop dragging, independent per-monitor activity queues, promised side parity or unrelated compositor backend.

## Implementation tasks

Statuses live only in progress.json. Complete one bounded task, verify it, then record its evidence.

| ID | Work | Proof IDs |
| --- | --- | --- |
| T01 | Review owner geometry boards against CP-03 and feasible panel anchors; record Gate A and migration cases. | R01 |
| T02 | Add validated mode/geometry persistence with old settings/Dual mapping and last-good recovery; extract only testable needed seams. | A01 |
| T03 | Connect host/Dual/preview for modes, reserve/fullscreen/display focus and rehome; preserve plugin state and IPC. | A02, R02, M01, M02 |
| T04 | Capture scale/hotplug/fullscreen and invalid-geometry recovery matrix; compare approved direction and retest focus. | R03, M03, M04, M05 |

## Acceptance criteria and proof mapping

| ID | Required outcome | Automated/runtime/owner proof |
| --- | --- | --- |
| AC01 | Bounded controls and migration preserve saved work and public API. | A01, A02, R02, M01, M02 |
| AC02 | Only one expanded owner; display loss/fullscreen do not strand focus or hide the wrong display. | A02, R03, M03, M04 |
| AC03 | Approved shapes, reduced motion and safe invalid-geometry recovery match actual rendering. | R01, R02, R03, M05 |

## Technical risks

Exclusive-zone reflow, offscreen settings/focus, mixed scale, monitor identity drift and accidentally duplicated expanded owners.

## Automated verification

Run all existing commands in [VERIFICATION](../VERIFICATION.md), then the following scoped checks.
New suites below are requirements for this future checkpoint, not commands claimed to exist today.
Record exact implemented commands/results, SHA and environment in the authoritative test records.

- **A01:** Existing gates plus valid/range/invalid settings, old keys/Dual migration, unknown monitor, truncated JSON, last-good geometry and stable IPC IDs.
- **A02:** Recorded monitor/client payloads for focused/preferred/fullscreen policy and monitor removal; one expanded owner; mode changes preserve plugin work.

## Runtime verification

- **R01:** Inspect references and approved CP-03 lineage; record Gate A externally.
- **R02:** All four modes at top/bottom: width/height/offset/alignment/radius, reserve/overlay reflow and repeated switching with an open plugin.
- **R03:** Laptop/external/fractional scale, preferred/focused fallback, hotplug, per-display fullscreen stay/explicit-overlay/hide recovery; corrupt test settings only, not personal files.

Capture actual application states under `review/cp-04-surfaces/evidence/run-01/application/` for the first run;
later runs get new numbers. Keep logs/diffs/traces under `automated/` in the same run and use the
[handoff template](../TEMPLATES.md). Include tested SHA/tree, instance identity, recovery, limitations,
app-versus-reference differences where applicable and code-review findings. Pure fixtures/compilation
cannot prove runtime/focus/animation behavior.

## Owner requirements, visual references and manual tests

Supply geometry/state boards and transition storyboard using CP-03’s approved look; test a second display only if available.

Gate A is mandatory before visual code changes. Inspect every actual supplied image and storyboard; do not infer approval from filenames.
Use [this checkpoint’s complete brief](cp-04-surfaces.visual.md) and [personal tests](../../../owner/checkpoints/cp-04-surfaces.md).
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
