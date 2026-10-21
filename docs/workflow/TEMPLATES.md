# Supporting record templates

Copy these into a run's `index.md` when real evidence exists. They are supporting provenance;
all lifecycle, task/test outcomes and approval decisions belong in progress.json.

## Runtime handoff (required before owner testing)

```text
Checkpoint / run:
Branch / tested SHA / dirty patch hash (if any):
Previous accepted SHA / matching state snapshot:
Environment: Qt, Quickshell, Hyprland, GPU, displays, scale, theme, motion, file managers
Isolation: test user/home, bus identity, Wayland socket, shared capabilities approved
Start action (exact tested command or launcher):
Stop action (exact tested command or launcher):
Restore previous action (exact tested command or launcher):
Live instance: full ID, PID, start time, config path (reverify before use)
Backup paths / checksums / restore rehearsal:
Owner checklist link / tests requested / special hardware:
Real application captures:
Reference comparison and noticeable deviations:
Review findings and resolution:
Remaining limitations / next agent action / next owner action:
```

## Evidence inventory

```text
Path | Type (owner concept / storyboard / actual app / owner failure / test log)
Creator/capture tool | UTC date | SHA256 | state/test ID | tested SHA | privacy review
For tests: command/steps, exit code, observed result, environment, limitations
For production assets: creator, source, permission/license, attribution, changes, distribution decision
```

For a required recording kept outside Git, add a tracked `recording-manifest.md` with: exact URL or
owner-approved storage location, SHA256, byte size, capture command/tool/date, tested SHA/environment,
scenario/timecodes, retrieval instructions, access requirements, and last successful retrieval/checksum
date. Include essential tracked keyframes and event/frame traces, plus exact recapture instructions.
The next agent verifies access and hash before relying on it; inaccessible required motion proof blocks
the current handoff until recovered or recaptured. Do not upload without owner permission.

## Design translation before Gate A

Prepare `references/proposed-design-rNN.md` alongside the candidate images. The owner sees a short
summary plus the exact selection. After approval copy its exact bytes to
`references/approved/rNN/design-spec.md`; record the file/hash in `reference_sets[].design_spec`
and bind its hash in Gate A. This is an implementation interpretation of the existing brief, not a
new product specification. Do not choose missing material design decisions on the owner's behalf.

```text
Checkpoint / set / source image hashes / inherited approved sets:
Source crop and coordinate scale (canvas pixels versus QML logical units; reference monitor/DPR):
Geometry table: mode/state, anchors, min/preferred/max bounds, offsets, radius, padding, clipping:
Tokens: semantic role, proposed dark/light/opaque value, existing Theme/K4.Tema property or additive role:
Typography/icons: family/fallback/license, size/weight/line-height, optical size, long-text behavior:
Components: existing QML path, state/property/signal, host or plugin owner, compatibility mapping:
Interaction table: trigger, guard, next state, focus/ESC/click-outside order, disabled/error response:
Motion table: from/to, fixed anchor, animated properties, duration/easing, interruption/reversal,
  hidden/expired behavior, reduced-motion equivalent:
Accessibility: keyboard order/names, focus, measured contrast targets, hit areas and text scaling:
Capture matrix: acceptance IDs, deterministic fixture, theme/mode/edge/scale/motion and expected outcome:
Differences from images / unresolved choices / feasibility and prior-set consistency:
```

Record numerical measurements and their rationale where the image permits them; label estimates.
Resolve ambiguous palette, dimensions, timing or behavior through the owner's Gate A selection.
Routine code structure choices within that approved interpretation do not require another permission.
Material changes require a new set/spec hash and explicit Gate A; retain superseded versions.
Generated labels and pixels never become flattened app controls.

## Owner approval record (agent transcribes; never invent)

```text
Gate A or Gate B:
Owner's exact words:
UTC date / source message, export or issue link:
Checkpoint and scope:
Gate A: reference set ID and exact paths/hashes, approved feasibility notes/deviations
Gate B: tested Git SHA and evidence run, requested owner tests and results
Unperformed cases and explicit disposition (never mark PASS):
Permission for next checkpoint (if explicitly supplied):
```

## Regression/correction record

```text
Reported test / run / owner words:
Reproduction and actual versus expected behavior:
Impact / affected acceptance IDs:
Cause / scoped fix / commits:
Regression command or runtime reproducer:
Retest run / related scenarios rerun:
Remaining failures / owner retest requested:
```
