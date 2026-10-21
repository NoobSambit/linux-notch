# CP-00 evidence-closure owner decisions

Primary tested revision: `b114d5a1b8c3ed90e97b577e3424092a783e04ed`; evidence run: `run-05`.
UTC transcription/decision-record time: 2026-10-21T12:39:10Z. This is not an invented manual-test execution time.
Source: owner's message in this Codex thread beginning “Let's finish CP-00 evidence closure and prepare Gate B.”
The literal relevant words follow; the owner did not approve Gate B in this message.

## Screenshot clarification and conditional evidence authorization

> A clarification from me: I remember taking TWO screenshots during manual testing, and they appeared in the Dock correctly. Please investigate the existing captures before claiming my screenshots are missing.

> If the original owner screenshots cannot be recovered, I explicitly authorize using my written M01/M03 PASS reports together with your genuine existing runtime captures as substitutes, provided you verify and document that this evidence is adequate.

## Conditional physical-display disposition authorization

> I do not know whether physical dual-monitor testing was performed. Check the actual run records and display configuration. Do not confuse my two screenshots with two monitors. If physical dual-monitor testing was not performed, record it honestly as NOT TESTED — ENVIRONMENT LIMITATION. I approve a formal nonblocking CP-00-only disposition if this is a conditional scenario permitted by the existing specification and workflow rules. Preserve the requirement for later relevant checkpoints and release testing.

## Boundaries

> Record the decisions with the required owner provenance, UTC timestamp, specification reference and hashed supporting evidence. Preserve all existing test history.

> Do not change product code, fabricate results, start CP-01, push or merge anything.

> Do not grant Gate B on my behalf. I want to approve it explicitly and finish CP-00.

## Applicability verified before applying these decisions

Two original manual-period screenshot files were recovered/reverified. They are not absent:
`captura-20261021-113602.png` correlates to M02 (including its visible typed sample), and
`captura-20261021-115325.png` correlates to M03. Both files are preserved without editing.
Neither supplies an M01 label/normal-desktop view or a bar-visible M03 view. No such additional
original view was recovered from the searched locations/logs. The substitution authorization is
limited to those unavailable observations; it does not discard or relabel the recovered originals.
The M03 original remains primary screenshot-output evidence, with existing genuine agent frames
and the owner's report supplying its edge/fullscreen context. Adequacy is assessed per observation
in `../automated/closure-assessment.md` and the screenshot investigation manifest.

The existing CP-00 R02 contract says displays “where available”; owner M03 step 3 says “If a second
test display exists, repeat there.” Read-only historical/current inventories show one physical eDP-1;
run-05's additional independent output was explicitly created as headless CP00-2. The two recovered
PNGs are two files, not two monitors. This satisfies the owner's condition for a CP-00-only conditional
physical repetition disposition under `docs/workflow/RECORD_FORMAT.md` (Limits, corrections and stale approval).

The new `R02-physical-2-display` and `M03-physical-2-display` records isolate only that physical repetition.
They remain NOT TESTED — ENVIRONMENT LIMITATION with `required: false`, owner quote/date/source,
existing specification reference, reason and a SHA256-bound copy of this decision. R02/M03 and their
required available-display observations remain required and PASS. No FAIL or NEEDS HELP is waived.
This is a late administrative coverage correction, not a claim that the child records existed before
manual testing, and not a changed product promise. The original owner histories and frozen runs stay intact.

Specification references:

- `docs/workflow/checkpoints/cp-00-baseline.md#runtime-verification`: R02's existing “where available” scope.
- `owner/checkpoints/cp-00-baseline.md`: M03's existing conditional step 3 and original evidence instructions.
- `docs/workflow/RECORD_FORMAT.md#limits-corrections-and-stale-approval`: conditional nonblocking disposition fields.
- `docs/V1_SPEC.md#support-tiers-and-release-gates`: later core one/two-monitor release checks stay required.
- `docs/workflow/checkpoints/cp-04-surfaces.md` and `docs/workflow/checkpoints/cp-10-release.md`, where applicable:
  later geometry/display and release requirements are not amended or started by this decision.

No original owner desktop screenshot is invented. No agent image is labelled an owner capture.
No new live test, image generation, product repair, Gate B, CP-01 implementation or remote action is authorized here.
