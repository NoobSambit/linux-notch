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
