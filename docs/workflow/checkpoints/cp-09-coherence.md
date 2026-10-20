# CP-09 — Broader product and settings coherence

Execution contract for roadmap milestone 9. **PLANNED initially; current truth is [progress.json](../progress.json).**
No task/test/approval result is asserted by this document. [Owner note](../../../owner/checkpoints/cp-09-coherence.md) · [Visual brief](cp-09-coherence.visual.md).

## Objective

Apply the accepted shared system to remaining core entry points/settings while preserving stable data/IPC and inherited functionality.

## Prerequisites

Approved cp-08-clipboard; recorded authorization for this checkpoint.
Read the [workflow](../README.md), [safety procedure](../SAFETY.md), [verification](../VERIFICATION.md)
and relevant source before edits. All earlier required failures block dependent implementation.

## Authoritative specification references

[IMPLEMENTATION_PLAN](../../IMPLEMENTATION_PLAN.md), [V1_SPEC](../../V1_SPEC.md), [V1_EXPERIENCE](../../V1_EXPERIENCE.md), [UX_DIRECTION](../../UX_DIRECTION.md), [ARCHITECTURE](../../ARCHITECTURE.md), [K4_MIGRATION_PLAN](../../K4_MIGRATION_PLAN.md), [DECISIONS](../../DECISIONS.md). Follow the matching milestone in IMPLEMENTATION_PLAN and relevant MUST/SHOULD clauses
in V1_SPEC; this contract does not replace those requirements. Consult inherited [API/plugins](../../k4-reference/README.md)
for touched compatibility behavior. If scope conflicts, stop that task and resolve the decision with the owner.

## In scope and affected modules

User-intent grouping/search/aliases without duplicate values; previews/recovery; launcher/control center/Own notification center/capture entry polish; network/unsandboxed plugin disclosure; optional simple capture→Shelf only if proven.

`services/Settings.qml`, `plugins/Settings/*`, Launcher/Apps/Panel/Toast/Captura entry views, privacy/plugin settings and touched shared widgets/translations.

## Out of scope

No redesign of deep editor/game/SSH tools, renaming persisted keys or IPC, new conversion/cloud/plugin store, silent module removal or unconditional capture expansion.

## Implementation tasks

Statuses live only in progress.json. Complete one bounded task, verify it, then record its evidence.

| ID | Work | Proof IDs |
| --- | --- | --- |
| T01 | Verify coherent screen references and previous design inheritance; approve feasible new states through Gate A. | R01 |
| T02 | Regroup existing settings/search/navigation with stable keys/aliases and migration/preview/recovery tests; preserve localization. | A01 |
| T03 | Apply shared entry-point states/privacy/dependency/plugin disclosure; optionally connect capture file to Shelf only through existing safe output. | A02, R02, M01, M02, M03 |
| T04 | Smoke core/supported/changed optional modules, focus/contrast/scale/reduced motion and actual setting persistence; compare references. | R03, M04, M05 |

## Acceptance criteria and proof mapping

| ID | Required outcome | Automated/runtime/owner proof |
| --- | --- | --- |
| AC01 | Settings are findable, one value per option; old IDs/aliases and saved data survive. | A01, R02, M01 |
| AC02 | Core entries share design and honest privacy/dependency/notification states. | A02, R02, M02, M03 |
| AC03 | Supported inherited tools remain available with no caused regression; readability/recovery are demonstrated. | R03, M04, M05 |

## Technical risks

Same setting stored twice, broken localized search/old aliases, incidental redesign or removal of inherited tools, unsupported notification mirror, credential/network disclosure drift.

## Automated verification

Run all existing commands in [VERIFICATION](../VERIFICATION.md), then the following scoped checks.
New suites below are requirements for this future checkpoint, not commands claimed to exist today.
Record exact implemented commands/results, SHA and environment in the authoritative test records.

- **A01:** Existing gates plus stable setting IDs/IPC aliases, old/new grouping search and localized labels, saved values, malformed settings recovery and preview synchronization.
- **A02:** Missing optional dependency paths, network-toggle behavior, plugin security wording/disabled lifecycle, Own/External availability and conditional capture-path validation.

## Runtime verification

- **R01:** Inspect selected settings/entry boards against all earlier approved sets and record Gate A.
- **R02:** Keyboard settings/search/preview/save/restart/recovery, launcher/controls, Own center versus External unavailable and capture entry/cancel; optional capture→Shelf preserves destination.
- **R03:** Tier-based smoke: editor/capture, Files, terminal/SSH if installed, wallpaper/theme/display tools in isolation, windows/workspaces, agents/session/plugin discovery; optional modules changed by this checkpoint; focus/contrast/text/motion.

Capture actual application states under `review/cp-09-coherence/evidence/run-01/application/` for the first run;
later runs get new numbers. Keep logs/diffs/traces under `automated/` in the same run and use the
[handoff template](../TEMPLATES.md). Include tested SHA/tree, instance identity, recovery, limitations,
app-versus-reference differences where applicable and code-review findings. Pure fixtures/compilation
cannot prove runtime/focus/animation behavior.

## Owner requirements, visual references and manual tests

Supply settings and core-entry boards based on earlier approved references. Test normal navigation and a short inherited-tool smoke tour prepared by Codex.

Gate A is mandatory before visual code changes. Inspect every actual supplied image and storyboard; do not infer approval from filenames.
Use [this checkpoint’s complete brief](cp-09-coherence.visual.md) and [personal tests](../../../owner/checkpoints/cp-09-coherence.md).
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
