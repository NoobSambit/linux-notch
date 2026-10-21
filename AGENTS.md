# Notchbar agent entry point

This fork's product direction is approved; **implementation is not authorized yet**.
This workflow setup does not approve or complete any product checkpoint.

## Start and resume

1. Inspect `git status --short --branch` and recent commits; preserve unrelated work.
2. Read [workflow](docs/workflow/README.md) and [progress.json](docs/workflow/progress.json).
   That JSON is the only authoritative execution/status record. The owner overview is generated.
3. Read the active/next checkpoint contract, its visual brief and owner checklist.
4. Read the relevant authoritative specifications and current source before editing.
5. Check prerequisites, owner authorization and Gate A. Resume the next incomplete task;
   do not infer approval from chat loss, file presence, a clean tree or green checks.

## Authority and architecture

- Product: [V1_SPEC](docs/V1_SPEC.md), [V1_EXPERIENCE](docs/V1_EXPERIENCE.md),
  [UX_DIRECTION](docs/UX_DIRECTION.md), [DECISIONS](docs/DECISIONS.md).
- Architecture: [ARCHITECTURE](docs/ARCHITECTURE.md), [migration](docs/K4_MIGRATION_PLAN.md),
  [roadmap](docs/IMPLEMENTATION_PLAN.md). Checkpoint contracts execute these; they do not replace them.
- Platform/dependencies/rights: [PORTABILITY](docs/PORTABILITY.md), [DEPENDENCIES](docs/DEPENDENCIES.md),
  [ASSET_LICENSE_AUDIT](docs/ASSET_LICENSE_AUDIT.md), [UPSTREAM_SYNC](docs/UPSTREAM_SYNC.md).
- Locked stack: **Qt 6 + QML + Quickshell; Wayland + Hyprland for v1**.
- Extend `shell.qml` arbitration, `services/Island.qml`, `PluginManager`, `core/Theme.qml`
  and `plugins/Dual`; no second Activity Router, theme singleton, registry or host.
- Preserve useful inherited k4 features, public `api/K4`, manifests, settings IDs and IPC.
  Use additive compatibility paths; removals need D14 evidence and owner decision.
- Top/bottom are v1 release paths; left/right remain experimental/compatibility-only.
- Follow D20 notification ownership and D24 fresh-versus-migrated Atalaya defaults exactly.
  Never mirror another daemon's history or overwrite saved intent with a temporary fallback.

## Work and evidence

- Work one eligible checkpoint on `checkpoint/cp-NN-short-name`; use small reviewable commits.
  Check off task IDs only in progress.json with actual evidence. Review the diff before handoff.
- Follow [verification](docs/workflow/VERIFICATION.md) and [safe runtime](docs/workflow/SAFETY.md).
  Never disable gates, relabel an unperformed test PASS or replace live proof with compilation.
- References live under `review/<checkpoint>/references/`. Only an owner-approved,
  hash-recorded set in progress.json satisfies **Gate A**. Actually open every selected image
  and check readability, completeness, feasibility, scope and consistency with earlier sets.
- Do not generate the owner's final references or invent the final visual direction.
  Ask for a new explicit Gate A decision for material appearance/behavior deviations.
- Capture real screenshots/video under `review/<checkpoint>/evidence/<run>/application/`.
  Compare against approved references and list differences. Generated concepts are never runtime proof.
- **Gate B** is the owner's explicit approval of the tested revision after automated/runtime checks
  and their checkpoint-specific manual tests. Agents cannot grant either gate or waive failures.
- Keep [owner notes](owner/checkpoints/) concise; update handoff instructions and regenerate
  `owner/PROGRESS.md` using `python3 tools/workflow.py --render` whenever progress changes.
- Before stopping/context loss, record task statuses, exact commands/results, failures, next agent
  action, next owner action, tested SHA/tree, runtime handle and recovery information in progress.json.
  Logs/media are supporting evidence, never a competing status tracker.

## Explicit owner decisions

Require explicit approval for starting CP-00; each visual direction; material scope/design/API
changes; live desktop config/install/autostart or session-service changes; personal state restoration;
new system dependencies; publishing/pushing/releasing; and final checkpoint approval.
Routine scoped implementation after its recorded authorization and prerequisites needs no repeated permission.
Approval of a checkpoint permits preparation of the next brief, not automatic approval of its visuals.

Never kill unrelated Quickshell processes/notification daemons, steal a D-Bus name, overwrite personal
configuration, run `instalar` as a testing shortcut, or use destructive Git recovery. A separate checkout
or XDG variables alone do not isolate inherited HOME-based state or desktop services. Stop if isolation
cannot be proven; report the missing capability with an exact next action.

## Shared toolkit

Prefer this project's instructions. Use relevant shared skills, prompts and rules from
`/home/noobsambit/.codex/everything-codex/` when helpful; do not install tools just to follow a template.
