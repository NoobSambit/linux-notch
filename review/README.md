# Review material, separate from runtime resources

This tree is **not imported or packaged by the application**. It contains no approved references or
actual app evidence at setup. Empty `.gitkeep` files only preserve convenient save locations.
The existing `screenshots/` tree is inherited k4 imagery, not proof of a Notchbar checkpoint.

| Path within each checkpoint | Meaning |
| --- | --- |
| `references/submitted/` | Owner-supplied candidate static references; not approved. Visual checkpoints only. |
| `references/alternatives/` | Unfinished/alternate concepts and new revisions; not approved. |
| `references/storyboards/` | Owner motion boards/keyframes and optional local video; intended behavior. |
| `references/approved/rNN/` | Immutable exact selected files copied after explicit owner Gate A; hashes in progress.json. |
| `evidence/run-NN/application/` | Real running-app screenshots/video only; no concepts. |
| `evidence/run-NN/owner/` | Owner manual-test/failure screenshots, recordings or notes. |
| `evidence/run-NN/automated/` | Test logs, traces, property reports and comparison/diff images. |

Reference names: `cp-NN__subject-state__dark|light|both__rNN.png` (or jpg/webp). The checkpoint brief
lists exact mandatory names. Optional per-frame suffix: `__frame-01`. Evidence:
`cp-NN__M01__short-description__run-NN.png`. Preserve revision/run suffixes. Never overwrite a selected
set or older evidence run. Agent copies selected storyboards too into the corresponding approved set;
the progress record identifies exact hashes, source paths and owner decision for that set. Superseded
sets remain readable; only the recorded current approved set guides implementation.

## Git and rights policy

- Track Markdown/JSON inventories, decisions, hashes and a small useful subset of selected lightweight
  PNG/JPEG/WebP references and app baseline/failure captures. Limit individual tracked review images to
  2 MiB and a checkpoint's added review media to 20 MiB; compress review copies, retain originals locally.
- Candidate/alternative/storyboard media are ignored by default. Explicitly `git add -f` only a small
  reviewed candidate needed for discussion. Approved lightweight static/keyframe copies are trackable.
- Recordings/GIFs/archives/raw exports/temp files and `review/**/private/` are ignored. Keep videos local;
  record descriptive path, hash, date/tool/state and how to retrieve them. They are not durable Git proof.
  A checkpoint cannot depend only on a missing local video after context loss: preserve essential small
  keyframes/logs and arrange a durable owner-approved location or recapture when needed. No LFS dependency.
- Never commit personal logs, histories, credentials or private desktop captures. Ask Codex to sanitize
  evidence before adding it; raw backups live in ignored `scratch/backups/` with restricted permissions.
- Production artwork stays in the relevant existing runtime module, e.g. `plugins/<module>/assets/`,
  only after a separate asset promotion decision and provenance/license record under
  [ASSET_LICENSE_AUDIT](../docs/ASSET_LICENSE_AUDIT.md). Record creator, source/tool/material, date,
  permission/license, attribution, edits and distribution decision. A concept approval is not asset clearance.
- Future packaging must use an explicit runtime allowlist; exclude `review/`, `owner/`, workflow media
  and `scratch/`. The current installer is not changed here; do not claim packaging exclusion was tested.
  QML must never glob/import review media as production resources.

Agent: [workflow](../docs/workflow/README.md). Owner: [image guide](../owner/VISUAL_REFERENCES.md).
