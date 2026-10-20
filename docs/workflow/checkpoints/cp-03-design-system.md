# CP-03 — Shared design system and original visual direction

Execution contract for roadmap milestone 3. **PLANNED initially; current truth is [progress.json](../progress.json).**
No task/test/approval result is asserted by this document. [Owner note](../../../owner/checkpoints/cp-03-design-system.md) · [Visual brief](cp-03-design-system.visual.md).

## Objective

Translate owner-selected original references into semantic tokens and shared QML states early, preserving public theme compatibility.

## Prerequisites

Approved cp-02-dnd-spike; recorded authorization for this checkpoint.  CP-02 must have a positive GO, or an explicit approved product rescope before proceeding; a failed spike cannot silently pass.
Read the [workflow](../README.md), [safety procedure](../SAFETY.md), [verification](../VERIFICATION.md)
and relevant source before edits. All earlier required failures block dependent implementation.

## Authoritative specification references

[IMPLEMENTATION_PLAN](../../IMPLEMENTATION_PLAN.md), [V1_SPEC](../../V1_SPEC.md), [V1_EXPERIENCE](../../V1_EXPERIENCE.md), [UX_DIRECTION](../../UX_DIRECTION.md), [ARCHITECTURE](../../ARCHITECTURE.md), [DECISIONS](../../DECISIONS.md). Follow the matching milestone in IMPLEMENTATION_PLAN and relevant MUST/SHOULD clauses
in V1_SPEC; this contract does not replace those requirements. Consult inherited [API/plugins](../../k4-reference/README.md)
for touched compatibility behavior. If scope conflicts, stop that task and resolve the decision with the owner.

## In scope and affected modules

Semantic roles, reusable states, dark/light/opaque fallback, type/icon/elevation/motion scales, core-mode examples and separate settings-navigation sample. Preserve existing theme properties.

`core/Theme.qml`, `core/Island*`, `core/SiluetaIsla.qml`, `widgets/*`, `api/K4/Tema.qml`, touched host/settings/Dual views.

## Out of scope

No independent theme singleton, final mode geometry policy, Shelf product implementation, deep module redesign, copied identity or forced external-plugin rewrite.

## Implementation tasks

Statuses live only in progress.json. Complete one bounded task, verify it, then record its evidence.

| ID | Work | Proof IDs |
| --- | --- | --- |
| T01 | Verify submitted boards and storyboard against UX scope/originality/feasibility; record owner Gate A with hashes and agreed token interpretation. | R01 |
| T02 | Extend existing Theme and shared components with semantic roles and interaction states while preserving public properties. | A01, R02 |
| T03 | Apply approved grammar to core four-mode examples, settings-navigation sample and dock primitives; add reduced-motion resolution. | A01, R02, M01, M02 |
| T04 | Capture dark/light/focus/large-text/opaque/motion examples, compare references and measure visual costs. | R03, M03, M04 |

## Acceptance criteria and proof mapping

| ID | Required outcome | Automated/runtime/owner proof |
| --- | --- | --- |
| AC01 | Owner-selected original direction is recorded before visual code changes. | R01 |
| AC02 | One shared vocabulary and legacy theme API work across touched examples. | A01, R02, M01 |
| AC03 | Legibility, focus, scale, fallback and reduced motion are visibly usable with measured cost. | R02, R03, M02, M03, M04 |

## Technical risks

Image-generation text/proportions may be impractical; transparent material may harm contrast; icon licensing and font fallback; theme changes can break legacy plugins; shader cost.

## Automated verification

Run all existing commands in [VERIFICATION](../VERIFICATION.md), then the following scoped checks.
New suites below are requirements for this future checkpoint, not commands claimed to exist today.
Record exact implemented commands/results, SHA and environment in the authoritative test records.

- **A01:** Existing gates plus semantic-token/state resolution, dark/light/reduced-motion fallback and legacy K4.Tema/sample-plugin regression checks; component geometry bounds.

## Runtime verification

- **R01:** Open each owner board/keyframe, inventory files/hashes, review feasibility and visual inheritance; Gate A is separately owner granted.
- **R02:** Rendered four-mode samples/settings/dock shared controls in dark/light, hover/pressed/focus/disabled/loading/error, long text/enlarged text and opaque fallback; keyboard and accessible-name review.
- **R03:** Real expansion/reduced-motion video, screenshots at laptop/external/fractional scale where available; compare concepts, contrast and CPU/GPU/frame costs to baseline.

Capture actual application states under `review/cp-03-design-system/evidence/run-01/application/` for the first run;
later runs get new numbers. Keep logs/diffs/traces under `automated/` in the same run and use the
[handoff template](../TEMPLATES.md). Include tested SHA/tree, instance identity, recovery, limitations,
app-versus-reference differences where applicable and code-review findings. Pure fixtures/compilation
cannot prove runtime/focus/animation behavior.

## Owner requirements, visual references and manual tests

Generate the required boards in the linked brief, choose a direction, then approve the exact feasible set. This is the first visual-generation checkpoint, after the Shelf decision.

Gate A is mandatory before visual code changes. Inspect every actual supplied image and storyboard; do not infer approval from filenames.
Use [this checkpoint’s complete brief](cp-03-design-system.visual.md) and [personal tests](../../../owner/checkpoints/cp-03-design-system.md).
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
