# PBICR2023 Dataset-Level Workflow Example

This example shows how to apply the general framework to a shared dataset with multiple article teams. It describes process only. It does not include data, full variable dictionaries, questionnaire content, article manuscripts, results, or permissions to access project materials.

## 1. Access and governance

Before analysis, confirm that each collaborator has the required ethics, institutional, and data-use approval. Obtain the dataset through the authorized PBICR2023 channel. Keep the original workbook and all participant-level extracts in approved local or institutional storage. This workflow repository is not a data-distribution mechanism.

Do not commit or share raw/cleaned workbooks, row-level exports, participant identifiers, derived classifications, model objects, full result workbooks, logs, or rendered article packages. A private GitHub repository does not make controlled data safe to upload.

## 2. Read authoritative project sources

Within the authorized PBICR2023 workspace, use the following order:

1. Dataset-level `AGENTS.md` and `README.md` for data boundaries and project conventions.
2. `dataset_overview.md` for shared study context.
3. `pbicr2023_data_guide.md` to locate analysis-facing names and coding notes; treat it as a navigation guide, not a substitute for source verification.
4. Approved study-design source for common design wording.
5. Measures index and only the measure sources needed for the active article.
6. Article-specific `ARTICLE_STATE.md`, `memory.md`, and locked or current `analysis_plan.md`.

When sources conflict, stop and resolve the conflict with the project lead. Do not infer scoring, coding, ethics information, or missing-data rules from an old manuscript or column name.

## 3. Start a distinct article workspace

Keep dataset-wide guidance at the PBICR2023 project level and create a separate folder for each article. Start with a short `ARTICLE_STATE.md` and `memory.md`; add the formal analysis plan only when the research question and primary analysis are sufficiently settled. Do not copy another article's results or plan as if they were shared facts.

Each article plan should state its own question, analytic sample, variables, scoring, missingness, primary model, diagnostics, sensitivity analyses, multiplicity strategy, planned tables/figures, and interpretation boundaries.

## 4. Prepare and analyze data reproducibly

Keep source data unchanged. Use an article-specific script to apply filters, recode and score variables, document exclusions, and create a reproducible analysis dataset in approved local storage. Before fitting models, check ranges, missingness, coding direction, scale scoring, sample counts, and any clustering or survey-design features relevant to the question.

Separate exploratory work from the primary analysis. Record amendments after inspecting results. Use `results/all/` for complete local outputs, `results/selected/` for reviewed manuscript candidates, and `results/diagnostics/` for model checks, errors, and sensitivity results. Keep individual-level outputs out of the shared repository.

## 5. Draft, review, and hand off

Use one editable manuscript source per article. Generate review copies from that source and check numerical consistency, citations, tables, figures, and layout before sharing. For PBICR2023, use association language unless the approved design supports stronger claims; do not infer causality from cross-sectional analyses.

For collaborator handoff, state the current question, analysis-plan status, completed work, unresolved decisions, authorized data location, relevant scripts, and next actions. Share only aggregate outputs that have been reviewed for disclosure risk and approved for that audience.

## What this example intentionally omits

It does not reproduce the PBICR2023 dataset guide, study documents, codebooks, scale text, variable lists, references, article-specific analysis plans, scripts, manuscripts, or results. Collaborators must access those through the approved project workspace and follow the applicable data-use rules.
