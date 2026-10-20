# Supply visual references

## WHAT YOU NEED TO DO NOW

Nothing to generate yet. The first visual brief is [CP-03](../docs/workflow/checkpoints/cp-03-design-system.visual.md),
after the safe setup, safety checks and file-drag test are approved. Use the active checkpoint link
on [Progress](PROGRESS.md) when Codex requests images.

## Save and submit

1. Open that checkpoint's visual brief. Give your external image tool its **purpose, image table,
   shared style, motion instructions and constraints**. Attach earlier approved images named by Codex
   so the style stays consistent. Generate exactly the mandatory images; optional alternatives can wait.
2. Save static references as PNG (best for UI), JPEG or WebP. The brief gives exact `.png` names.
   If you use another format, keep the same name and change the extension to `.jpg` or `.webp`;
   tell Codex. Do not just rename a file's extension.
3. For CP-03, save the static boards in
   `review/cp-03-design-system/references/submitted/` and its motion board in
   `review/cp-03-design-system/references/storyboards/`. Every later brief gives its own exact paths.
4. Use descriptive filenames from the table, for example
   `cp-03__surface-family__dark__r01.png`. `r01` means first revision. Do not use `image1.png`.
5. Save extra unfinished choices in that checkpoint's `references/alternatives/` folder.
   Give each a new revision such as `r02`; do not overwrite the old file.
6. Add a short preference in `references/NOTES.md`, or simply tell Codex which files you prefer.
7. Send the exact “References ready” message at the end of the checkpoint brief.
8. Codex checks the files exist, opens every image, identifies missing/contradictory details and shows
   you a feasible selection. File presence alone is not approval. Do not start app testing yet.
9. After reviewing that selection, say: **“I approve Gate A for CP-03, set r01, as listed by Codex,
   including the listed feasibility notes.”** Use the actual checkpoint and set. Codex records your words
   and preserves the exact approved files. Only then can visual coding start.

## Motion and revisions

A storyboard is a labelled image with before/middle/after frames. The brief lists exact frame states,
anchors and movement. Individual keyframes may use suffixes `__frame-01`, `__frame-02`, etc. before
the extension. Optional short video goes in `references/storyboards/` with the same descriptive name
and `.webm` or `.mp4`; Codex keeps large video local and records its location. A still image does not
prove animation works; Codex later supplies real app video.

For a revision use `r02`, then `r03`. Put new alternatives in `references/alternatives/`; put the
proposed replacement boards in `references/submitted/` and motion in `references/storyboards/`.
Tell Codex what changed and which set you prefer. Codex asks you to approve the new exact set; your
previous approved set stays in `references/approved/r01/`, with its approval history preserved.
Never edit `references/approved/` yourself. Material changes need a new approval before coding continues.

Aim for images under 2 MB each. Keep large originals/video locally; Codex can prepare small review copies
without changing your originals. Only selected lightweight references need to enter Git. Do not place
concepts in `core/`, `plugins/`, `api/` or existing `screenshots/`. References do not automatically become
art used by the app, and they do not automatically grant rights to redistribute any depicted artwork.
