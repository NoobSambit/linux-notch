# Documentation map

The product files at this directory's root remain the authoritative research, architecture and v1 direction.
Product implementation still requires approval. The new execution workflow organizes future work without
changing those specifications or starting a product checkpoint.

- **Project owner:** [Start here](../owner/README.md), [current progress](../owner/PROGRESS.md),
  [visual references](../owner/VISUAL_REFERENCES.md), [testing](../owner/TESTING.md),
  [recovery](../owner/RECOVERY.md) and [checkpoint notes](../owner/checkpoints/).
- **Coding agents:** [workflow](workflow/README.md), [checkpoint contracts and visual briefs](workflow/checkpoints/),
  [authoritative progress record](workflow/progress.json), [verification](workflow/VERIFICATION.md),
  [safety](workflow/SAFETY.md), [record templates](workflow/TEMPLATES.md) and [setup review](workflow/SETUP_REVIEW.md).
- **Review files:** [storage and Git policy](../review/README.md); conceptual images stay separate from runtime assets.

- [k4 source audit](RESEARCH_K4.md), [Droppy research](RESEARCH_DROPPY.md), and [feature matrix](FEATURE_MATRIX.md) provide the evidence.
- [V1 experience](V1_EXPERIENCE.md), [v1 specification](V1_SPEC.md), [UX direction](UX_DIRECTION.md), and [decision log](DECISIONS.md) define the proposal.
- [Architecture](ARCHITECTURE.md), [migration plan](K4_MIGRATION_PLAN.md), [portability](PORTABILITY.md), [dependencies](DEPENDENCIES.md), and [implementation plan](IMPLEMENTATION_PLAN.md) describe the possible path after approval.
- [Selective upstream sync](UPSTREAM_SYNC.md) records the fork base and import policy. [Asset/data/IP release audit](ASSET_LICENSE_AUDIT.md) tracks provenance and distribution gates.

The [k4 reference documentation](k4-reference/) contains the inherited API, plugin, game, and other guides for the code currently in this repository. Keep using those guides when working with existing k4 behavior; moving them here does not deprecate the APIs or change the product.
