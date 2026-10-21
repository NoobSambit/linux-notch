# CP-00 technical review

Full changes reviewed from merged main 6478e25: CP-00 tooling/evidence, authoritative progress/generated
owner view, owner instructions, CI control-regression step and synthetic workflow-test fixture correction.

485 inherited runtime/helper/dependency/license paths have identical Git mode/type/blob IDs to ff520e3.
No product QML/theme/API/manifest/settings/IPC/installer/architecture behavior changed. Review media is not
imported at runtime. No Notchbar feature or CP-01 implementation is included.

Safety: separate namespaces and no host endpoints; parent connection only in compositor; read-only
independent checkouts with no remote/alternates/shared object hardlinks. Exact ID/config/PID/start/session/source
and pidfd checks guard stop; immutable dummy backups verify scope/checksums and retain pre-restore state.

Failures retained: Qt timing logger crash; invalid parent-occlusion measurements, corrected using fixed headless
display; earlier dummy/CLI harness errors. No gate, test or failure was waived or disabled.

Workflow tests previously copied live progress into a temporary repo lacking its history: nine failed on
current_task/SHAs. Only the temporary fixture is now reset to PLANNED; all 30 original positive/negative
assertions remain and pass. Validation logic is unchanged; the generated owner overview now says None for an empty remaining-task list. Failure, exact patch and rerun are durable. This bookkeeping
correction follows the clean application SHA and changes no runtime behavior.

Captures contain synthetic data only. No host desktop/clipboard/credentials/personal store committed.
No dependency/autostart/live config/personal restore/push/merge/release/Gate B occurred.
Technical review supports owner testing; it cannot grant owner approval or waive physical/device limits.
