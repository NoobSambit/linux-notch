# Problems, revisions and approval

Copy this small report into a message to Codex:

```text
Checkpoint / run:
Test:
Result: PASS / FAIL / NOT TESTED / NEEDS HELP
What happened:
What should have happened:
Screenshot/video: project path
Can you reproduce it? Yes / No / Sometimes
```

Codex will investigate. You do not need to explain the code. Evidence belongs in
`review/<checkpoint>/evidence/<run>/owner/`; your personal note gives the exact path.
For a visual revision say which approved image or app state should change and what you prefer.
New concept alternatives go in `references/alternatives/`, never over an approved file.

**Gate A — choose the look before coding:** after Codex lists the exact selected images and feasible
differences, say “I approve Gate A for CP-03, set r01, as listed, including the feasibility notes.”
Use the actual checkpoint/set. “Images are ready” or “I prefer this” is a submission/preference,
not permission to start visual coding.

**Gate B — approve the actual tested app:** after Codex supplies the real app and you perform the
requested checklist, say “I approve CP-03 Gate B for version [the SHA Codex gives me], run-01.
My requested tests passed.” State any untested case and its reason instead of claiming it passed.
Codex checks that remaining required gaps are resolved before recording the checkpoint approved.
For a nonvisual checkpoint use the same Gate B wording; there is no Gate A image decision.

You may also say “Changes requested: CP-03 M02 failed; please fix and send a new run.” A failed test
returns to correction and retest. Old failures remain in the history; they are not erased.
Approval covers that exact version/run, not later untested changes. Your next-checkpoint permission
can be included explicitly, for example “Prepare and carry out CP-01 after this approval.” Later visual
work still waits for its own Gate A selection. Publishing, installing over your everyday desktop and
changing desktop services each need separate explicit permission.
