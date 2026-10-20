# CP-01 — Regression and safety gates

Execution contract for roadmap milestone 1. **PLANNED initially; current truth is [progress.json](../progress.json).**
No task/test/approval result is asserted by this document. [Owner note](../../../owner/checkpoints/cp-01-safety.md) · [Visual brief](cp-01-safety.visual.md).

## Objective

Add focused safety/compatibility regression coverage and targeted safe-default corrections on the characterized k4 foundation.

## Prerequisites

Approved cp-00-baseline; recorded authorization for this checkpoint.
Read the [workflow](../README.md), [safety procedure](../SAFETY.md), [verification](../VERIFICATION.md)
and relevant source before edits. All earlier required failures block dependent implementation.

## Authoritative specification references

[IMPLEMENTATION_PLAN](../../IMPLEMENTATION_PLAN.md), [V1_SPEC](../../V1_SPEC.md), [ARCHITECTURE](../../ARCHITECTURE.md), [DECISIONS](../../DECISIONS.md), [K4_MIGRATION_PLAN](../../K4_MIGRATION_PLAN.md), [DEPENDENCIES](../../DEPENDENCIES.md). Follow the matching milestone in IMPLEMENTATION_PLAN and relevant MUST/SHOULD clauses
in V1_SPEC; this contract does not replace those requirements. Consult inherited [API/plugins](../../k4-reference/README.md)
for touched compatibility behavior. If scope conflicts, stop that task and resolve the decision with the owner.

## In scope and affected modules

Focused settings/migration/activity/parser/IPC/plugin fixtures; D20 notification first-run and conflict safety; D24 fresh Atalaya off versus migrated effective state; disclosed/controllable known network paths; installer restart scoping where justified.

`services/Settings.qml`, `services/PluginManager.qml`, `services/Notifs.qml`, `shell.qml`, `instalar`, `tools/prueba_*`, `.github/workflows/validar.yml`, `api/K4/*` and `ejemplos/*`.

## Out of scope

No surface redesign, Shelf integration, replacement Activity Router, broad installer/packaging rewrite or removal of inherited modules. Any new substantial UI needs its own approved brief before visual work.

## Implementation tasks

Statuses live only in progress.json. Complete one bounded task, verify it, then record its evidence.

| ID | Work | Proof IDs |
| --- | --- | --- |
| T01 | Characterize settings, parser, existing activity and IPC/plugin lifecycle contracts; add targeted regression fixtures and CI invocation for those seams. | A01, R01 |
| T02 | Implement/test D20 fresh owned/unowned selection, saved intent, migration, restart, loss/race/conflict fallback and safe Notifs facade. | A02, R02, M01 |
| T03 | Implement/test fresh versus migrated Atalaya effective-state preservation and safe invalid/truncated settings fallback. | A03, M02 |
| T04 | Scope installer restarts to intended instance; check disclosure/control and offline cases for known network features; review compatibility and recovery. | A04, R03, M03, M04 |

## Acceptance criteria and proof mapping

| ID | Required outcome | Automated/runtime/owner proof |
| --- | --- | --- |
| AC01 | Focused regressions run in CI without weakening inherited gates. | A01, A02, A03, A04 |
| AC02 | D20 never steals ownership; user intent and facade compatibility survive conflicts/restarts. | A02, R02, M01 |
| AC03 | Fresh Atalaya is off, inherited effective state preserved; settings/IPC recover without loss. | A03, R01, M02 |
| AC04 | Scoped restart/offline controls and recovery work without collateral effects. | A04, R03, M03, M04 |

## Technical risks

Misclassifying an inherited catalog default as a fresh install, saved intent versus effective fallback, notification owner races, unsandboxed external plugins and tests that mock away real process effects.

## Automated verification

Run all existing commands in [VERIFICATION](../VERIFICATION.md), then the following scoped checks.
New suites below are requirements for this future checkpoint, not commands claimed to exist today.
Record exact implemented commands/results, SHA and environment in the authoritative test records.

- **A01:** Existing gates plus new focused settings/activity/backend-payload/IPC and plugin-lifecycle fixtures; missing plugin and failed/reloaded/disabled samples included.
- **A02:** D20 matrix: fresh occupied/unowned bus, saved Own/External, migrated no-choice, unknown owner, name loss/race, restart and explicit change; assert no daemon takeover.
- **A03:** D24 explicit on/off and inherited default migration, fresh off; malformed/truncated JSON recovery and stable IDs/aliases.
- **A04:** Installer process-scope fixture with unrelated Quickshell sentinel; offline/opt-in network behavior and safe unavailable dependencies.

## Runtime verification

- **R01:** Load/reload/disable/error test examples and verify IPC settings aliases; disabled plugins are uninstantiated.
- **R02:** Exercise D20 against a real test-bus daemon, including restart and intentional switching after owner control; External shows unavailable history/actions.
- **R03:** Demonstrate safe restart leaves unrelated test sentinel and real session untouched; inspect actual settings, network toggles and rollback.

Capture actual application states under `review/cp-01-safety/evidence/run-01/application/` for the first run;
later runs get new numbers. Keep logs/diffs/traces under `automated/` in the same run and use the
[handoff template](../TEMPLATES.md). Include tested SHA/tree, instance identity, recovery, limitations,
app-versus-reference differences where applicable and code-review findings. Pure fixtures/compilation
cannot prove runtime/focus/animation behavior.

## Owner requirements, visual references and manual tests

No images. Allow a short test of fresh and copied settings in the isolated session; Codex handles setup.

**No visual reference generation required for this checkpoint.** It validates engineering/runtime behavior rather than selecting a new appearance.
Use [this checkpoint’s complete brief](cp-01-safety.visual.md) and [personal tests](../../../owner/checkpoints/cp-01-safety.md).
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
