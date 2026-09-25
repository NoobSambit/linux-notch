# Selective upstream k4 sync

## Baseline and remote convention

- Upstream project: [k4ditano/k4](https://github.com/k4ditano/k4).
- Fork base: [`5b1406c2267440c97c4c9986a9fa19c7424094c0`](https://github.com/k4ditano/k4/commit/5b1406c2267440c97c4c9986a9fa19c7424094c0). On 2026-09-25, the 535 paths shared by upstream at that commit and local first commit `9fba900` had identical Git blob IDs; the 11 local-only paths were the new product planning docs. This is a content-verified source baseline, even though the fork's initial import commit does not share upstream Git ancestry.
- Keep `origin` for `NoobSambit/linux-notch`; reserve the name `upstream` for `https://github.com/k4ditano/k4.git`. This document does not add or fetch a remote in the product repository.

| Tracking field | Current value | Meaning |
| --- | --- | --- |
| Last inspected upstream SHA | `5b1406c2267440c97c4c9986a9fa19c7424094c0` | Source snapshot compared on 2026-09-25. |
| Last incorporated upstream SHA | `5b1406c2267440c97c4c9986a9fa19c7424094c0` (content baseline) | No later upstream change has been imported. The local initial commit has separate ancestry. |

Record the last **inspected** upstream SHA and the last **incorporated** SHA separately. A later upstream tip is not automatically part of this product. An import note should list upstream commit(s), affected files, what was adopted or declined, adaptation needed, validation, and attribution. Compare from the recorded base or last reviewed SHA; do not infer divergence from `git merge-base` with the fork's unrelated initial commit.

## Import rule

1. Review upstream releases/commits for security fixes, Linux service fixes, compatibility improvements and useful workflows. Triage by product value and risk, not by ease of merging.
2. **Cherry-pick** a self-contained upstream change when it fits the approved behavior and affected files have little local divergence. Use `git cherry-pick -x` so the source SHA is traceable, then run affected tests and live scenarios.
3. **Manually port** the idea or fix when upstream code conflicts with the new surface, design system, Activity Policy, settings ownership or local privacy requirements. Link the upstream commit in the port's commit message/documentation, preserve required notices, and test the resulting behavior. Do not pretend the result is a verbatim cherry-pick.
4. Decline or defer changes that expand unsupported platforms/features, weaken local-first controls, or conflict with the product. Record why.

Full merges should be exceptional and justified by a reviewed batch of compatible changes. Do not make the architecture or file layout serve automatic merges. Conversely, do not casually rename/move inherited modules during early v1 work: preserve paths, public `K4` API, manifest keys, settings IDs and `k4` IPC verbs where practical. Use compatibility adapters when the product needs a new model. Break those surfaces only for a real architectural reason, with a migration and test plan.

## High-divergence review

Treat `shell.qml`, `plugins/Dual/*`, `core/Theme.qml`, `services/Settings.qml`, `plugins/Settings/*`, `services/PluginManager.qml`, `api/K4/*`, `services/Island.qml`, `services/Notifs.qml` and shared widgets as likely conflict zones. For each upstream change there, compare **behavior and invariants** rather than line count: activity ownership, geometry/focus, notification ownership, saved-state migration, plugin lifecycle, hot reload and IPC compatibility. Import small service/parser fixes independently where possible. Never replace a modified file wholesale merely to catch up.

After any import, run existing validators (`tools/plugins.py`, `tools/api.py`, `tools/guia.py`), relevant targeted tests and sample external-plugin checks. Exercise `K4.Plugin` view/priority/IPC/settings lifecycle, disabled/reload/failure behavior, and relevant Hyprland modes. Add a regression fixture when the imported change fixes a reproducible bug. Static validators do not prove rendering, focus or multi-monitor behavior.

Upstream API and guide changes belong in [`k4-reference/`](k4-reference/) when they still describe inherited code. Update links and documentation checks. Product plans in the `docs/` root change only after a separate product decision; do not let an upstream README or guide silently override them. Preserve `LICENSE`, k4ditano copyright, upstream authorship, third-party notices and any asset/data attribution separately. See the [asset release gate](ASSET_LICENSE_AUDIT.md).
