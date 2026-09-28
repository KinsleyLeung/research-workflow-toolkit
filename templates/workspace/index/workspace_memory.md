# Workspace Conventions

Edit this file during installation. It records **stable local choices**, not an activity log, a protocol, or universal standards. Article-specific decisions belong in the article `memory.md`. Delete any convention your team does not adopt.

## State and handoff

- Keep `ARTICLE_STATE.md` (current dashboard) separate from `memory.md` (dated reasoning and decisions).
- Start `analysis_plan.md` when a formal model, major rerun, or manuscript output plan is ready. Date changes made after results were inspected.
- Use `handoff.md` only for a long, interrupted, blocked, or cross-person task; place it at workspace or article level as appropriate.

## Results and manuscripts

- Store full generated results in `results/all/`, diagnostics in `results/diagnostics/`, and reviewed manuscript-facing aggregates in `results/selected/`.
- If tables are produced in a workbook and a manuscript, generate both from the same model object or tidy results. Do not manually transfer numbers between them.
- Default editable manuscript source: `manuscript.qmd`. Generate review Markdown/Word; transfer accepted Word edits back to QMD. Use LaTeX only when the journal or author requires it.
- Use `manuscript/references.bib` for cited references. Verify both bibliographic metadata and whether the source supports the exact claim; these are distinct checks.
- Default figure review/submission formats: PDF and TIFF, subject to the journal's instructions. Avoid unnecessary format variants.

## Sharing and maintenance

- Keep participant-level data, governed documents, generated outputs, and literature full texts out of the workflow toolkit and out of Git by default.
- Review candidate files and their content before committing or sharing. `.gitignore` is not a disclosure audit.
- Promote methods and topic knowledge only after removing project-specific content and documenting assumptions and scope.
- Do not create empty directories or placeholder state files before an active task needs them.

## Team-specific decisions to fill in

- Authorized storage and access process:
- Manuscript source and rendering route, if different:
- Table and figure export conventions, if different:
- Reference manager and citation-key policy, if used:
- Git hosting, visibility, and approval process:
