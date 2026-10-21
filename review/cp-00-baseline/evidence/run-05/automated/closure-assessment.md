# CP-00 evidence closure assessment

Tested candidate: **b114d5a1b8c3ed90e97b577e3424092a783e04ed**, evidence **run-05**.
This is an administrative evidence/applicability review under the owner's explicit closure instruction.
No product/helper code, new live scenario, new screenshot, Gate B or next checkpoint is introduced.

## Screenshot investigation

The earlier wording about missing screenshots was too broad. Two actual manual-period files exist:

| Original synthetic capture | Preserved evidence | What the actual image shows |
| --- | --- | --- |
| `captura-20261021-113602.png`, 11:36:02 UTC | [Recovered M02 original](../owner/cp-00__M02__recovered-owner-capture__run-05.png) | Both CP00 dummy documents and the exact `CP00 M02 harmless text` sample. |
| `captura-20261021-115325.png`, 11:53:25 UTC | [Previously preserved M03 original](../owner/cp-00__M03__owner-capture__run-05.png) | Whole dummy desktop during the M03 interval. |

Both images are 1280x720. They were opened with `view_image` and compared with originals by SHA256.
The M02 file had not previously been copied into Git; it is now preserved byte-for-byte. The M03
file already in Git is identical and has not been replaced. Test attribution uses visible fixture
state, original names/mtime, preparation/report times and the owner's clarification, not an invented
click transcript. Filesystem times are identified as such, not claimed as independent input-event logs.

[Search manifest](closure-screenshot-investigation.json) records scope, paths, dimensions, hashes,
duplicate matches and limits: 323 PNG candidates/182 distinct hashes across run-05, test lab and
dummy snapshots (including extensionless clipboard PNG blobs); inherited source trees excluded.
Configured host/test screenshot output folders and relevant cache/temp locations were also checked
for current-test-date candidates. No unrelated personal image was opened or copied. The four files
in synthetic Capturas include two older engineering outputs tied to run-04/run-05 command logs,
and these two later manual-period images. No additional M01 label/normal-desktop view or bar-visible
M03 owner view was recovered. Existing logs do not retain exact owner screenshot/Dock clicks.

The owner separately recalls that both images appeared correctly in the Dock. That remains an
owner observation; neither saved PNG independently shows the Dock. The capture path intentionally
hides the island (`services/Captura.qml` / `services/Island.qml` / `shell.qml`), so this absence does
not mean the files are missing or that Dock appearance failed. Two image files do not mean two monitors.

## Adequacy by required observation

| Observation | Accepted evidence and limits | Conclusion |
| --- | --- | --- |
| M01 label/source identity | The literal [M01 owner report](../owner/cp-00__M01__owner-report__run-05.md), actual labelled [candidate settings](../application/cp-00__R01__recovery-candidate-settings__run-05.png), exact source/config/ID/PID/start-time records in [R01 recovery check](recovery-check.json). The image is an agent runtime frame, not an owner M01 photo. | Adequate for the required identity observation. |
| M01 Start/Stop and unaffected normal desktop | Owner's direct report that Start/Stop worked and normal desktop stayed unaffected; R01 actual exact-instance stop kept the neighbouring test instance, host Quickshell ID/config/PID and notification owner matched before/after, personal k4 state stayed absent. Private isolation proof and subsequent guarded return/stop records corroborate the boundary. No image is falsely claimed to prove a stop or personal desktop state. | Adequate combined direct owner and independent technical proof. |
| M02 captured output/input | Recovered original visibly contains the typed M02 sample and both documents; original owner report says all five steps worked; owner clarification reports Dock appearance. The original image proves output and visible content, not a transient Dock interaction. | Adequate; original preserved and supplementary owner observation attributed accurately. |
| M03 whole-screen output and context | Recovered original has the fixed nested output's 1280x720 geometry; [M03 readiness](m03-readiness.json) documents that output/mirror arrangement. The post-test saved setting is abajo in the original M03 provenance and preserved candidate state. The PNG itself hides the island. | Adequate screenshot-output/context evidence in combination, not standalone edge proof. |
| M03 both edges and fullscreen return/input | Owner's literal [M03 PASS report](../owner/cp-00__M03__owner-report__run-05.md), actual [top](../application/cp-00__R02__surface-arriba__run-05.png) and [bottom](../application/cp-00__R02__surface-abajo__run-05.png) native frames, [fullscreen](../application/cp-00__R02__fullscreen-on__run-05.png) / [return](../application/cp-00__R02__fullscreen-return__run-05.png) frames and corresponding command/readbacks. The selected agent frames were reopened and inspected during closure; source is b114d5a per the original immutable inventory. Pixels do not prove typing, so that remains the owner's direct report. | Adequate for the required available-display matrix. |

The [owner decision](../owner/closure-owner-decisions.md) conditionally authorizes genuine reports and
existing runtime captures as substitutes after investigation and adequacy review. It is applied only
to the unrecovered M01-specific and bar-visible M03 views; the two recovered originals are kept.
For M03, the original file itself is recovered and primary; only its missing edge/transition viewpoints
are supplied by genuine existing agent frames plus the owner's report. This changes evidence format,
not required behaviour or test scope. The combined proof covers every required observation above;
there is no remaining required screenshot-format gap after this explicit CP-00/run-05 disposition.
No generated image, relabelled agent frame or retrospective reconstruction is used.

## Physical display finding and formal disposition

[Display verification](closure-display-verification.json) compares pre-M03/current host inventories:
only eDP-1 is listed physically. Run-05 commands explicitly create `CP00-2` with `output create headless`.
CP00-STABLE is the stable headless test output; WAYLAND-1 mirrors it. Existing two-output engineering
captures are virtual-display evidence. No physical dual-monitor test is established by the records.

`R02-physical-2-display` and `M03-physical-2-display` remain **NOT TESTED — ENVIRONMENT LIMITATION**.
They are nonblocking for CP-00 only, with `required: false` and the owner's quote, UTC timestamp,
source, existing specification reference, reason and hashed decision artifact. The condition is already
present in R02's “where available” wording and M03's “If a second test display exists” instruction;
no product-scope change or DECISIONS amendment is needed for this conditional baseline repetition.
Splitting these cases now is a disclosed administrative correction, not backdated execution.

The parent R02/M03 tests stay required. The real virtual two-output baseline and all other required
available-display observations are retained. No required core display/privacy/data gate is waived.
V1 core one/two-monitor verification and relevant later geometry/display/release checkpoints remain
unchanged; neither future hardware proof nor release testing is marked PASS or preapproved.

## Acceptance assessment and retained findings

| Criterion | Required evidence | Closure assessment |
| --- | --- | --- |
| AC01 — safe isolation/stop/restore | A01, R01, M01; exact native instance/host checks; owner report; candidate/original matching state and guarded stop/restore proof. | Satisfied for CP-00 with the accepted evidence format. |
| AC02 — original behaviour and limitations documented | R02, M02, M03; actual native frames/readbacks; both recovered originals; owner reports; explicit conditional physical-display disposition. | Satisfied as baseline characterization, not a claim that inherited product defects are fixed. |
| AC03 — resource/Atalaya/rights baseline | R03, M04; three startups and 24 complete fixed-display workload samples, effective Atalaya/open/closed checks, rights-gap inventory and owner recovery report. | Satisfied for a baseline/initial rights inventory; no release rights clearance implied. |

Existing warnings/defects and failed historical attempts remain visible: settings binding loops,
Game/chest state versus its separate setting, failed Qt timing instrumentation with the alternative
kernel/Wayland measurements, and the later stale private IPC socket startup failure resolved by verified
task-private housekeeping without code changes. They do not prevent the demonstrated safe, reproducible
CP-00 baseline. Their scope remains later settings/safety/compatibility work, not an unreported repair.
Other existing hardware/driver/scale/device and distribution-rights limitations remain in the immutable
baseline report and performance/rights records; this closure does not turn them into release passes.

All eight required tests remain PASS. The two new conditional physical-display cases are the only
additional NOT TESTED records and are explicitly nonblocking under the approved conditional scope.
No unresolved required FAIL, NEEDS HELP or NOT TESTED is accepted. Old histories/evidence/run indexes
are retained verbatim; current applicability reviews append separate entries rather than rewriting them.

Gate B remains null. The candidate remains unchanged at b114d5a / run-05, selected and stopped.
Closure permits preparation of the owner's approval decision only; no CP-01, product/helper patch,
push, PR, merge, publication or agent-granted approval follows.

## Closure verification

- Workflow validator with `--base-ref 570387d`: PASS after staging reviewed evidence and rendering the owner view. Initial render correctly refused untracked proof; the subsequent stale-view check was resolved by rendering after staging. No gate or code was changed.
- `python3 tools/test_workflow.py`: 30 tests PASS.
- `python3 tools/test_cp00.py`: 14 tests PASS.
- Read-only [closure audit](closure-check.py): PASS; all 290 earlier evidence files and every prior history entry retained, staged/worktree evidence hashes match, all three immutable dummy snapshots match, candidate/original checkouts clean, payloads stopped, later checkpoints unchanged. Its first draft expected a combined display-status string; corrected to the existing schema's `NOT TESTED` result plus `ENVIRONMENT LIMITATION` reason before the successful audit. This was an audit assertion correction, not a test-result or workflow-rule change.
- Exact commands, exit codes and closure audit output are preserved in [closure validation](closure-validation.json).

All CP-00 acceptance criteria are satisfied with these explicit evidence/applicability dispositions.
The only next owner decision is explicit Gate B approval of the unchanged tested revision/run.
