# Original k4 resource baseline — run-05

Tested clean application checkout: b114d5a1b8c3ed90e97b577e3424092a783e04ed.

Intel i7-13700HX / Intel UHD 770 i915 render node; host also has RTX 4050, but these are Intel client counters.
Qt 6.11.2; Quickshell 0.2.1/7511545; Hyprland 0.56.2/Aquamarine 0.15.1; Arch kernel 7.2.8.
Private CP00-STABLE headless 1280x720/60 Hz/scale 1, mirrored into the parent. Native app animation enabled; compositor placement animation disabled.

Application launch + source verification + IPC readiness: 0.403 s, 0.367 s, 0.361 s (three repetitions). Excludes compositor boot and first-visible-frame latency. Each launch gets a 3-second warmup.

| Workload | CPU % of one core, mean | Maximum RSS MiB | Intel render engine %, mean | Frame callbacks/s, all surfaces |
| --- | ---: | ---: | ---: | ---: |
| idle-catalog-atalaya-on | 8.73 | 273.70 | 0.495 | 60.2 |
| idle-atalaya-off | 8.73 | 259.86 | 0.499 | 60.2 |
| idle-explicit-atalaya-on | 8.70 | 259.08 | 0.506 | 60.1 |
| media-local-playing | 9.56 | 261.80 | 0.581 | 60.2 |
| dock-settled | 8.66 | 272.28 | 0.519 | 60.2 |
| atalaya-open-two-dummy-windows | 17.83 | 276.77 | 6.026 | 120.4 |
| atalaya-closed-after-open | 8.63 | 262.75 | 0.487 | 60.2 |
| idle-untraced-control | 7.36 | 279.44 | 0.511 | not traced |

Each state: three separate 10-second samples after 3 seconds of settling. performance.json retains /proc CPU/RSS, reaped-child CPU and deduplicated DRM client fdinfo. GPU busy-time is per Quickshell client, not whole-system GPU load. External player/fixture/compositor/live-helper costs are excluded from process CPU/RSS; reaped-child CPU is separate.

Traced states use the default render loop with WAYLAND_DEBUG=client; the untraced control is an ordinary launch. Idle tracing adds about 1.4 percentage points of one core here. Reuse identical instrumentation for comparisons. No unrelated desktop process was stopped on this shared workstation.

Atalaya: absent saved override plus catalog true resolves on; explicit false resolves off; explicit true resolves on. Open reports two dummy windows/error empty; closed reports abierto=false/scale=0. Open render-engine usage averages 6.03%, returning to 0.49% after closure, near the 0.50% disabled/default baseline. This short workload does not certify all window counts/drivers.

The inherited Game/chest pill remains part of the default dummy idle workload under juegoActivo, even with its catalog plugin disabled. Its original pulse is preserved. Idle is not zero-cost.

Frame traces retain surface frame requests, matching callbacks, output events and diagnostics. Atalaya open has two active surfaces: 120 total callbacks/s is not a 120 Hz display. Callback intervals measure compositor delivery, not CPU render-stage duration or physical presentation latency. QSG_RENDER_TIMING did not complete successfully: this installed logger crashes; run-04 retains the failure. Untraced zero logged callbacks means not traced, not zero rendering.

Raw protocol files remain in ignored scratch/cp00/lab/raw-traces/run-05; each performance record binds its path/SHA256. Essential counter/callback proof is tracked. All raw-file hashes were verified readable locally before handoff.

Proposed follow-up: reuse fixed output/fixture state/warmup/three repetitions and investigate results outside the recorded workload ranges. Owner performance budgets remain a CP-03 design decision before being treated as acceptance thresholds. No universal threshold or owner tradeoff approval is invented; decisions are not deferred wholesale to CP-10.
