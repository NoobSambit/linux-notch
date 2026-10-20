# Workflow design basis

Inspected 2026-10-20 at source baseline `ff520e3`. These are chosen practices, not a tooling mandate.

## Repository findings

Inspected the complete tracked path inventory, all eleven requested planning documents, the experience,
feature/research documents, source boundaries, launcher/installer and current tests/CI. The QML host is
`shell.qml`; `services/Island.qml` publishes geometry, `PluginManager` owns lifecycle, `Dual` implements
the dock, `core/Theme.qml` owns theme values, and `api/K4` is the compatibility surface. Built-in plugins,
examples, Python helpers, translations and `qmldir` files already form a useful modular structure.
No root AGENTS or execution tracker existed. Keep these runtime boundaries.

`.github/workflows/validar.yml` runs the existing validators and four `prueba_*` suites; it does not run
the Hyprland product or prove visual behavior. `publicar.yml` handles third-party plugin publication,
not checkpoint acceptance. Preserve both. `tools/guia.py` checks selected inherited docs, not this entire
workflow, so it cannot be presented as proof of the new links/contracts. `arrancar` prepares QML imports
and logs; it does not isolate state. Settings, Paths and PluginManager use HOME-based k4 paths; notification
startup is eager, and `instalar` has process-wide Quickshell termination. No launch/install was performed
for workflow setup. Local CLI help confirms Quickshell 0.2.1 supports explicit `-p`, `kill --id`, `ipc --id`
and `list --all --json`; future agents must recheck their installed version.

## Practices adopted and adaptations

| Practice / primary source | Application here |
| --- | --- |
| [OpenAI harness engineering](https://openai.com/index/harness-engineering/) describes repository knowledge and a short agent map. | Small AGENTS, durable checkpoint contracts, one status record and a resume routine. No dependence on chat memory. |
| [GitHub Spec Kit](https://github.com/github/spec-kit/blob/main/docs/index.md) carries intent through plan, tasks and convergence. | Existing approved specs stay authoritative; task/acceptance IDs link to them. Adopt the practice without installing the toolkit or generating competing specs. |
| [Google small changes guidance](https://google.github.io/eng-practices/review/developer/small-cls.html) recommends self-contained reviewable changes. | A handful of tasks per checkpoint, purpose-based commits, diff review and a recoverable last-good revision. |
| [Continuous integration by Martin Fowler](https://martinfowler.com/articles/continuousIntegration.html) emphasizes frequent integration and automated feedback. | Keep inherited gates, add targeted seam regressions during CP-01 and later work, retest integration after each bounded checkpoint. Owner gates remain separate from automated checks. |
| [Qt Quick Test](https://doc.qt.io/qt-6/qtquicktest-index.html) provides QML TestCase/SignalSpy patterns. | Use the installed matching Qt capabilities for policy/component tests when justified; do not introduce a C++ harness or dependency merely for setup. Python fixtures already fit helper/parser seams. |
| [Qt visual verification guidance](https://doc.qt.io/squish/how-to-create-and-use-verification-points.html) combines geometry/content and rendered comparisons. | Stable captures, known environment, property checks and screenshot differences; video/runtime checks for motion/focus. No Squish purchase/dependency is required. |
| [Design Tokens Community Group](https://www.designtokens.org/tr/2025.10/format/) formalizes named design decisions. | Gate A handoff describes semantic roles and a shared vocabulary; implementation extends existing Theme rather than adding an exchange pipeline. This community report is not a W3C Standard. |
| [GOV.UK contribution criteria](https://design-system.service.gov.uk/community/contribution-criteria/) checks usability, consistency and versatility. | One inherited visual grammar; later briefs reuse approved choices and test real content/accessibility rather than proliferating styles. |
| [Quickshell configuration guide](https://quickshell.org/docs/v0.1.0/guide/introduction/) explains explicit config paths and live reload. | A pinned test checkout/path and exact instance identity are part of handoff; copying QML alone is not desktop-service isolation. |

## Rejected overhead

No new issue tracker, background agent daemon, LFS, design tool subscription or external asset service.
No automatic screenshot rebaselining or automatic approval. Native Qt/Wayland evidence is the target;
a browser rendering of a design cannot establish QML behavior. Lightweight JSON/Markdown plus the existing
Python installation are sufficient for eleven checkpoints. Additional tools require a measured need.
