# CP-05 — Host Activity Policy and interactions

Execution contract for roadmap milestone 5. **PLANNED initially; current truth is [progress.json](../progress.json).**
No task/test/approval result is asserted by this document. [Owner note](../../../owner/checkpoints/cp-05-activities.md) · [Visual brief](cp-05-activities.visual.md).

## Objective

Extend the existing host arbitration for reliable interruption, expiry, restoration and deliberate input without a second owner.

## Prerequisites

Approved cp-04-surfaces; recorded authorization for this checkpoint.
Read the [workflow](../README.md), [safety procedure](../SAFETY.md), [verification](../VERIFICATION.md)
and relevant source before edits. All earlier required failures block dependent implementation.

## Authoritative specification references

[IMPLEMENTATION_PLAN](../../IMPLEMENTATION_PLAN.md), [V1_SPEC](../../V1_SPEC.md), [V1_EXPERIENCE](../../V1_EXPERIENCE.md), [ARCHITECTURE](../../ARCHITECTURE.md), [UX_DIRECTION](../../UX_DIRECTION.md), [DECISIONS](../../DECISIONS.md). Follow the matching milestone in IMPLEMENTATION_PLAN and relevant MUST/SHOULD clauses
in V1_SPEC; this contract does not replace those requirements. Consult inherited [API/plugins](../../k4-reference/README.md)
for touched compatibility behavior. If scope conflicts, stop that task and resolve the decision with the owner.

## In scope and affected modules

Compact/persistent/transient/user-session policy in existing arbiter; expiry/coalescing/restore; recording visibility; critical battery dismissal; hover/click/drag-intent/shortcut/ESC focus; D20 Own-only notification integration.

`shell.qml`, `api/K4/Plugin.qml`, `services/Island.qml`, `services/Notifs.qml`, Media/Audio/Indicadores/Wifi/Bt/Captura services, `widgets/*`, affected Player/Volume/Toast/Panel views.

## Out of scope

No second Activity Router, arbitrary user priority editor, camera/mic universality, media queue/lyrics or fake brightness source. Actual Shelf target waits for CP-07.

## Implementation tasks

Statuses live only in progress.json. Complete one bounded task, verify it, then record its evidence.

| ID | Work | Proof IDs |
| --- | --- | --- |
| T01 | Verify activity layouts/storyboard and CP-03/04 inheritance; lock feasible differences with owner Gate A. | R01 |
| T02 | Add deterministic eligibility/expiry/restore/coalescing and legacy priority/view compatibility tests; implement within existing host. | A01 |
| T03 | Connect actual Linux signals and recording stop affordance; Own-only notifications and conditional real backlight; implement intent/focus rules. | A02, R02, M01, M02, M03 |
| T04 | Capture interruption/hidden-expiry/critical/focus/fullscreen/display matrix in four modes and reduced motion; profile changes. | R03, M04, M05 |

## Acceptance criteria and proof mapping

| ID | Required outcome | Automated/runtime/owner proof |
| --- | --- | --- |
| AC01 | One existing host owns selection; current eligibility drives restore, hidden events expire. | A01, R02, M01 |
| AC02 | Intent and recording stop stay accessible without focus theft or stale reopen. | A02, R02, R03, M02, M03 |
| AC03 | Notification ownership and real-signal limits are honest; visuals/motion match approved sequence. | A02, R01, R03, M04, M05 |

## Technical risks

Hidden stale transient replay, focus theft from user views, recording stop hidden by another activity, timer guesses versus live source and daemon name-loss races.

## Automated verification

Run all existing commands in [VERIFICATION](../VERIFICATION.md), then the following scoped checks.
New suites below are requirements for this future checkpoint, not commands claimed to exist today.
Record exact implemented commands/results, SHA and environment in the authoritative test records.

- **A01:** Existing gates plus deterministic media→HUD→current-media restore, stopped-media no restore, hidden expiry/coalescing, dismissed-state no reopen, critical/user/persistent priority and legacy plugin mapping.
- **A02:** D20 owner/loss/restart guards, recording accessibility, hover never grabs keyboard, explicit shortcut/ESC/click-outside order and real-signal availability; no duplicate watcher.

## Runtime verification

- **R01:** Inspect approved state boards/keyframes; identify anchored regions and Gate A decision.
- **R02:** Music/volume bursts/current-source restore, recording stop behind user view, critical status dismissal, real Wi-Fi/Bluetooth/battery signals; hardware brightness only if verified.
- **R03:** Own/External real daemon matrix, open launcher while events arrive, hover versus click/shortcut/ESC, all modes/fullscreen/display rehome and reduced-motion video/frame costs.

Capture actual application states under `review/cp-05-activities/evidence/run-01/application/` for the first run;
later runs get new numbers. Keep logs/diffs/traces under `automated/` in the same run and use the
[handoff template](../TEMPLATES.md). Include tested SHA/tree, instance identity, recovery, limitations,
app-versus-reference differences where applicable and code-review findings. Pure fixtures/compilation
cannot prove runtime/focus/animation behavior.

## Owner requirements, visual references and manual tests

Supply activity states and a media → volume → media storyboard; test music, dummy notices and a short safe recording.

Gate A is mandatory before visual code changes. Inspect every actual supplied image and storyboard; do not infer approval from filenames.
Use [this checkpoint’s complete brief](cp-05-activities.visual.md) and [personal tests](../../../owner/checkpoints/cp-05-activities.md).
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
