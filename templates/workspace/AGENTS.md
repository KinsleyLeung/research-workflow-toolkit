# Workspace Agent Instructions

This file is for Codex and other AI agents working in this research workspace. `README.md` is for human orientation; `AGENTS.md` is the operating rulebook for the agent.

## 1. Core Principle

Keep the system light. Do not create folders, templates, state files, method notes, topic notes, or summaries until they are useful for the active work.

For every task:

1. Identify the active dataset, article, task type, and intended output.
2. Read only the files needed for that task.
3. Before creating, modifying, moving, deleting, committing, pushing, or uploading anything, report the planned file operations and wait for user approval.
4. Do not scan unrelated articles, datasets, methods, or topics.
5. Do not expose individual-level or sensitive data in chat.

## 2. Workspace Structure

Use this structure as a placement guide; do not pre-create optional directories:

* `projects/`: dataset-level projects and manuscript-specific article folders.
* `projects/<DATASET>/`: one folder per dataset-level project.
* `projects/<DATASET>/articles/`: manuscript-specific article folders within a dataset project.
* `methods_library/`: reusable statistical workflows and reporting rules.
* `topic_library/`: reusable theory, construct, and topic knowledge.
* `shared/`: shared formatting rules, journal requirements, manuscript resources, and templates.
* `index/`: workspace maps, directory snapshots, audits, and cleanup inventories.
* `handoff.md`: workspace-level task handoff when a long workspace task is paused or resumed.

`index/` is not the place for active task handoff notes.

Generic method notes are supplied in the separate workflow toolkit. Copy or link only a reviewed, relevant note into `methods_library/` when a real article needs it; a note does not replace the primary method sources or the article analysis plan.

## 3. Reading Order

For workspace-level work, read this file first.

For dataset-level work, read:

1. Root `AGENTS.md`.
2. Dataset `AGENTS.md`, when present.
3. Dataset overview or guide only when needed.

For article-level work, read:

1. Root `AGENTS.md`.
2. Dataset `AGENTS.md`, when present.
3. Article `ARTICLE_STATE.md`.
4. Article `memory.md`, when historical decisions are relevant.
5. Article `analysis_plan.md`, when formal analysis, result interpretation, or manuscript generation is involved.

Read scripts, results, figures, manuscripts, source documents, or literature only when the current task requires them.

## 4. Stage-Based Reading Map

Use the user's stated stage, active dataset, active article, task type, and intended output to decide what to read. Do not read broad folders just because they exist.

If the user says only the stage, ask or infer the active dataset/article only when needed. If the task is workspace-level, do not enter article folders.

### 4.1 Workspace Or New Conversation Startup

Use when the task is about general workflow, Git boundaries, workspace rules, or how Codex should operate.

Read:

1. Root `AGENTS.md`.
2. `index/workspace_memory.md`, when stable user preferences or workflow choices matter.
3. `index/workspace_catalog.md`, when locating workspace areas.
4. `index/workspace_structure_text.md`, only when folder placement or new structure is being discussed.

Do not read article folders, data, results, manuscripts, or literature by default.

### 4.2 Task Resume And Handoff

Use when the user says to continue, resume, pick up from last time, or return to a paused or blocked task.

Read:

1. Root `AGENTS.md`.
2. The relevant `handoff.md`.
   * For workspace-level tasks, read root `handoff.md`.
   * For article-level tasks, read the article folder's `handoff.md`.
3. The state files required by the resumed task stage, such as `ARTICLE_STATE.md`, `memory.md`, or `analysis_plan.md`.
4. Only the files named or implied by the handoff and the current user request.

If no relevant `handoff.md` exists, continue using the stage-based reading map and do not create a handoff unless the task becomes long, interrupted, blocked, cross-file, or likely to be resumed later.

When ending an unfinished long task, update the relevant `handoff.md` only after reporting the planned update and receiving approval.

### 4.3 Topic Or Idea Discussion

Use when the user is still discussing a possible research question, theory, literature logic, or article direction.

Read:

1. Root `AGENTS.md`.
2. Dataset `AGENTS.md`, when a dataset is named.
3. Article `ARTICLE_STATE.md`, only if an existing article is named.
4. Article `memory.md`, only if prior direction changes or rejected paths are relevant.
5. `topic_library/`, only when the user asks for reusable topic knowledge or a cross-article theory note.

Do not read raw data, generated results, full manuscripts, or unrelated articles by default.

### 4.4 New Article Setup

Use when creating a new article folder, state files, or initial project skeleton.

Read:

1. Root `AGENTS.md`.
2. Dataset `AGENTS.md`, when present.
3. `index/workspace_structure_text.md`.
4. Relevant templates in `shared/templates/`.
5. `index/workspace_memory.md`, when workflow preferences matter.

Create only the files needed for the current stage. For a new real article, start with `ARTICLE_STATE.md` and `memory.md` unless the user asks otherwise.

### 4.5 Exploratory Analysis

Use when running early models, checking feasibility, exploring directions, or comparing possible analytic routes.

Read:

1. Root `AGENTS.md`.
2. Dataset `AGENTS.md`, when present.
3. Article `ARTICLE_STATE.md`.
4. Article `memory.md`, when historical decisions matter.
5. Dataset overview, data guide, variable dictionary, scripts, or approved source documents only as needed.
6. Relevant method notes in `methods_library/`, only for the active method.

Do not read manuscripts, `results/selected/`, or broad `results/all/` outputs unless the exploratory task requires them.

### 4.6 Formal Analysis Plan

Use when the direction is becoming fixed, a formal rerun is planned, manuscript tables are being planned, or the user asks for `analysis_plan.md`.

Read:

1. Root `AGENTS.md`.
2. Dataset `AGENTS.md`, when present.
3. Article `ARTICLE_STATE.md`.
4. Article `memory.md`.
5. Article `analysis_plan.md`, if it already exists.
6. Dataset overview, variable dictionary, source documents, and relevant method notes only as needed.

Record whether the plan is `draft`, `locked`, `amended`, or `superseded`. Do not silently rewrite a locked plan after seeing results.

### 4.7 Formal Modeling And Result Generation

Use when executing the formal analysis plan, rerunning scripts, generating result workbooks, or creating selected aggregate outputs.

Read:

1. Root `AGENTS.md`.
2. Dataset `AGENTS.md`, when present.
3. Article `ARTICLE_STATE.md`.
4. Article `analysis_plan.md`.
5. Article `memory.md`, when prior amendments, pitfalls, or rejected models matter.
6. Active scripts and relevant method notes.
7. Data guides or source documents only as needed for variable use.

Do not read manuscript drafts unless the output must match manuscript tables or text.

### 4.8 Result Selection, Tables, And Figures

Use when deciding which outputs move from `results/all/` or `figures/all/` into manuscript-selected materials.

Read:

1. Root `AGENTS.md`.
2. Article `ARTICLE_STATE.md`.
3. Article `analysis_plan.md`.
4. Relevant parts of article `memory.md`.
5. Only the relevant result categories in `results/all/`.
6. `results/selected/` and `figures/selected/`, if they already exist.
7. `shared/journal_requirements/`, when manuscript-ready formatting is required.

Do not scan unrelated result categories or old exploratory files by default.

### 4.9 Manuscript Drafting And Word Output

Use when generating, revising, checking, or formatting a manuscript or supplement through Quarto, Markdown, or Word.

Read:

1. Root `AGENTS.md`.
2. Dataset `AGENTS.md`, when present.
3. Article `ARTICLE_STATE.md`.
4. Article `memory.md`.
5. Article `analysis_plan.md`.
6. The active `manuscript/manuscript.qmd`, when it exists.
7. `results/selected/` and `figures/selected/`.
8. `shared/journal_requirements/manuscript_format_requirements.md`.
9. The active `reference.docx`, only when generating or checking Word layout.
10. Article `references.bib`, journal `.csl`, or Zotero records, when references are involved.
11. Article `reference_audit.md`, only when claim-level citation verification or submission auditing is involved and the file exists.
12. Approved dataset-level Study design and Measures sources, when the active manuscript uses shared study information.
13. An approved generic table reference and table-formatting code, only when manuscript-ready Word tables are involved and those materials exist.

Read generated `manuscript/output/manuscript.md` when checking whole-document content or numerical consistency. Read generated `manuscript/output/manuscript.docx` only when Word rendering, Track Changes, comments, or layout must be reviewed.

Do not read raw data, cleaned data, large diagnostics, or full `results/all/` by default.

Use an Overleaf/LaTeX starter only if it has been copied from the workflow toolkit into `shared/templates/` and the target journal or user actually requires LaTeX.

### 4.10 Revision, Reviewer Response, Or Journal Resubmission

Use when handling reviewer comments, editor letters, manuscript revision, or point-by-point responses.

Read:

1. Root `AGENTS.md`.
2. Article `ARTICLE_STATE.md`.
3. Article `memory.md`.
4. Article `analysis_plan.md`.
5. Current manuscript, supplement, tables, figures, references, reviewer comments, and response drafts relevant to the revision.
6. Git history or file diffs only when the revision task requires version comparison.

Do not read unrelated articles or exploratory outputs unless a reviewer asks about those analyses.

### 4.11 Final Study Summary And Reusable Knowledge

Use when an article is stable, accepted, submitted, or ready for reusable-method/topic extraction.

Read:

1. Article `ARTICLE_STATE.md`.
2. Article `memory.md`.
3. Final or current `analysis_plan.md`.
4. Final manuscript or selected sections.
5. `results/selected/` and `figures/selected/`.
6. Relevant method/topic library files only when updating reusable knowledge.

Create or update `STUDY_SUMMARY.md` only when useful. Do not move article-specific literature into `topic_library/` unless it is reusable across articles or the user selected it as valuable.

### 4.12 Workspace Cleanup Or Migration

Use when auditing, deleting, archiving, moving, renaming, or reorganizing files.

Read:

1. Root `AGENTS.md`.
2. `index/workspace_catalog.md`.
3. `index/workspace_structure_text.md`.
4. `index/cleanup_candidates.md`, when available.
5. File lists and metadata before file contents.

Do not open individual-level data contents. Do not delete, move, rename, overwrite, or archive anything without explicit approval for that operation.

### 4.13 Git, GitHub, Or Release Boundary Review

Use when staging, committing, pushing, creating a repository, connecting a remote, or deciding what belongs on GitHub.

Read:

1. Root `AGENTS.md`.
2. `.gitignore`.
3. `index/workspace_memory.md`, when Git/GitHub preferences matter.
4. Git status and candidate file lists.
5. Candidate files by name and type before content.

Before staging or committing, report the exact candidate files or patterns and check for data-like or large files. Do not commit, push, publish, or connect a remote unless the user explicitly approves that action.

For a single article entering Git, first read the article state files and directory listing, then produce three lists for user approval:

1. Recommended for Git.
2. Keep local and exclude from Git.
3. Needs user decision.

Do not stage the whole article folder by default.

## 5. Article Workflow And State Files

A researcher may develop ideas and literature logic in conversation, then run analyses, iterate results, revise the research direction, generate a manuscript, and summarize reusable knowledge. Record decisions in files as the work matures rather than treating a conversation as the only source of truth.

For each real article, keep `ARTICLE_STATE.md` and `memory.md` separate:

* `ARTICLE_STATE.md`: current dashboard. It records the current idea, stage, direction, completed work, next actions, current blockers, important cautions, and links to key files.
* `memory.md`: chronological decision log. It records durable decisions, direction changes, model changes, result-selection decisions, rejected paths, and pitfalls.

Create or update `analysis_plan.md` when the article is ready for formal analysis, a major analysis rerun, manuscript table planning, or a fixed research direction. It should record the current analysis contract, including sample, variables, model sequence, diagnostics, sensitivity analyses, exploratory analyses, planned tables/figures, and output destinations.

Use plan status in `analysis_plan.md`:

* `draft`: still being discussed.
* `locked`: used as the current formal analysis plan.
* `amended`: changed after data or result inspection, with an amendment note.
* `superseded`: replaced by a later plan.

Do not silently rewrite a locked plan after seeing results. Record changes as amendments or in `memory.md`.

Use `handoff.md` only when a task is long, interrupted, cross-file, blocked, or likely to be resumed later. It is a task handoff, not the article's long-term memory. For article tasks, place it in the article folder; for workspace tasks, place it at the workspace root.

## 6. Analysis And Output Routing

Article-specific outputs belong in:

`projects/<DATASET>/articles/<ARTICLE>/`

Use:

* `scripts/`: article-specific analysis and manuscript-generation scripts.
* `results/all/`: complete generated outputs, exploratory outputs, diagnostics summaries, model comparisons, and machine-readable audit materials.
* `results/selected/`: manuscript-selected aggregate outputs.
* `results/diagnostics/`: assumption checks, errors, sensitivity diagnostics, and QA materials.
* `figures/all/`: complete generated figures.
* `figures/selected/`: manuscript-selected figures.
* `manuscript/manuscript.qmd`: the single editable manuscript source.
* `manuscript/references.bib`: article-specific bibliography used by Quarto/Pandoc.
* `manuscript/journal.csl`: journal citation style when an article-specific CSL file is needed.
* `manuscript/reference_audit.md`: claim-to-source audit created only when formal drafting or citation verification makes it useful.
* `manuscript/reference.docx`: article- or journal-specific Word style reference, created only when needed.
* `manuscript/output/manuscript.md`: generated review output for whole-document content and numerical checking.
* `manuscript/output/manuscript.docx`: generated Word output for visual quality control, Track Changes, coauthor review, and submission.
* `manuscript/output/supplement.docx`: generated supplement output when a supplement exists.
* `manuscript/overleaf/`: optional LaTeX/Overleaf source used only when a journal explicitly requires LaTeX or the user requests it.

In `results/all/`, organize outputs by result type rather than generating many repeated fragments. Useful categories may include descriptive statistics, sample flow, model fit, primary models, robustness checks, sensitivity analyses, subgroup analyses, interaction analyses, diagnostics, and software-exchange files. Multiple workbooks are acceptable when each has a clear purpose.

In `results/selected/`, organize tables by manuscript design. Prefer:

* one workbook for main manuscript tables, with one sheet per table;
* one workbook for supplementary tables, with one sheet per table.

Record planned main and supplementary tables in `analysis_plan.md` before treating them as manuscript-ready.

When a table is delivered both as an Excel workbook and inside `manuscript.qmd`, generate both from the same R model object or tidy result data frame. Excel workbooks are review and audit deliverables; they must not become a second numerical source, and values must not be copied manually from Excel back into the manuscript.

Use CSV only for software exchange, reproducible pipelines, Mplus/R/Python input-output, or lightweight machine-readable intermediates.

Formal manuscript figures should be exported only as:

* PDF for inspection, review, manuscript assembly, and vector-preserving submission when accepted by the journal.
* TIFF for final high-resolution journal submission.

Do not generate PNG, JPG, SVG, or multiple preview variants by default.

## 7. Manuscript Workflow

Use `manuscript.qmd` as the single source of truth for each manuscript and supplement. The default workflow is:

`R analysis -> manuscript.qmd -> manuscript/output/manuscript.md -> manuscript/output/manuscript.docx`

Rules:

* Edit `manuscript.qmd`; treat files under `manuscript/output/` as generated outputs.
* Declare the article bibliography and output formats in the QMD front matter using project-relative paths. Use `reference.docx` only when that file exists and Word styling is required.
* Use `manuscript/output/manuscript.md` for whole-document content, citation-placeholder, and numerical review. It is not the final authority for Word table appearance.
* Use `manuscript/output/manuscript.docx` for final visual quality control, Track Changes, coauthor comments, and journal submission.
* Transfer accepted Word edits back into `manuscript.qmd` before regenerating outputs. Do not maintain divergent manuscript versions manually.
* Insert R results directly into `manuscript.qmd` whenever practical. Fix model seeds, record package versions, and make the generation path reproducible.
* Use `gtsummary` for Table 1 and conventional model summaries, tidy data frames or `broom` outputs for custom models, and `flextable` for final Word table formatting.
* Use an approved, generic table reference or the target journal's instructions when available. Never use a populated study table as a reusable visual template.
* Implement reusable formatting rules in code only when required; render and visually verify them against an approved generic reference before relying on them.
* Use a `reference.docx` only for document-level Word styles such as body text, headings, captions, margins, and paragraph spacing. Table appearance remains the responsibility of `flextable` and `table_style.R`.
* Convert a stable manuscript to LaTeX only when the target journal explicitly requires it. Do not use LaTeX as the default early drafting environment.

### Reference Management

Use the article-specific `manuscript/references.bib` as the citation source of truth. It should contain the references actually cited in that manuscript, not a full Zotero library export.

Rules:

* For references already in Zotero, preserve the existing Better BibTeX citation key whenever possible.
* A reference not present in Zotero may be identified and bibliographically verified from authoritative sources such as the publisher, Crossref, PubMed, or an official institutional website, then added directly to `references.bib`. Downloading a PDF or importing the item into Zotero is not required merely to create a valid citation.
* Distinguish bibliographic verification from claim-support verification. Metadata can verify authorship, title, venue, year, DOI, and URL; it does not by itself establish that a source supports a manuscript statement.
* For theoretical claims, method assumptions, scale properties, exact numerical claims, disputed conclusions, or strong novelty statements, inspect the abstract, full text, original table, or official report as required. If only metadata has been checked, label the citation `Metadata only` rather than `Verified`.
* Do not enable Better BibTeX Keep Updated to overwrite a `references.bib` that also contains entries added outside Zotero. Automatic whole-file export is acceptable only when all entries in the project bibliography are managed in the corresponding Zotero collection; otherwise use explicit item export and reviewed merging.
* A later Zotero import is optional for long-term collection. When importing a project-only entry later, preserve and verify its project citation key to avoid duplicate keys for the same work.
* Use Quarto/Pandoc citation syntax such as `[@citekey]`. Do not leave manually typed author-year citations as the final citation mechanism.
* During drafting, standardize unresolved citations as `[CITE: concise claim or source requirement]`. Do not mix this with informal placeholders such as `[find a paper]` or final-looking author-year parentheses.
* Before submission, replace every citation placeholder and verify bibliographic accuracy, DOI/URL completeness, duplicate records, citation-key consistency, and correspondence between in-text citations and `references.bib`.
* Use the journal CSL file to render in-text citations and the bibliography. CSL does not control manuscript typography, page layout, or table formatting.
* Quarto-generated Word citations are output text rather than the manuscript's editable source. Citation changes proposed in Word must be transferred back to `manuscript.qmd` and regenerated.

Create `manuscript/reference_audit.md` when the article enters formal drafting, accumulates difficult or high-risk citations, or approaches submission. Do not create it automatically for every new idea. It should map exact manuscript locations and claims to references, citekeys, evidence checked, support level, status, and notes. Use statuses such as `Verified`, `Partial`, `Contextual`, `Metadata only`, `Unresolved`, and `Rejected`.

When a dataset maintains approved shared Study design or Measures sources, use only the material needed by the active article. Preserve approved wording unless the user asks for a change; add article-specific sample restrictions, exclusions, reliability estimates, or scoring details only where required. Treat pending material as a draft and verify wording and citation keys before manuscript use. Do not insert an entire Word source into a manuscript. Follow the target journal's heading requirements, and resolve every citation key against the active article bibliography.

## 8. Reusable Knowledge

After an article is stable or finalized, create or update a concise `STUDY_SUMMARY.md` in the article folder when useful. It may include:

* the final research question and thesis;
* small aggregate results suitable for sharing;
* final manuscript table and figure map;
* major limitations and interpretation boundaries;
* reusable methods, theory, writing, formatting, or workflow lessons;
* pitfalls to avoid in similar future studies.

Route reusable knowledge carefully:

* `methods_library/`: reusable statistical execution and reporting rules.
* `topic_library/`: reusable theory, construct definitions, topic logic, and user-selected valuable literature notes.
* `shared/`: manuscript formatting rules, workflow conventions, templates, journal requirements, and cross-project practical notes.

Do not create a new library category, such as a point library or literature library, unless repeated use shows that `methods_library/`, `topic_library/`, and `shared/` are not enough.

## 9. Git And GitHub Boundaries

Local Git records file changes. It does not replace `memory.md`, which records why research decisions were made.

GitHub Issues can help manage revision tasks, reviewer comments, and collaborator-facing checklists. Issues should not replace source files such as `analysis_plan.md`, scripts, `manuscript.qmd`, `.bib`, or `STUDY_SUMMARY.md`.

For a reusable workflow/template repository, include only workflow-level materials such as `README.md`, `AGENTS.md`, `.gitignore`, templates, formatting rules, and lightweight examples. Do not include research data, article-specific private results, manuscript drafts, or controlled materials.

For article repositories, include only reviewed and safe materials such as:

* `ARTICLE_STATE.md`
* `memory.md`
* `analysis_plan.md`
* final or approved `.R` analysis scripts
* scripts that generate final selected tables, figures, or manuscript outputs
* `manuscript.qmd` and supplement QMD sources
* `.bib` files
* journal `.csl` files
* `reference_audit.md`, when it contains reviewed claim-to-source decisions
* small aggregate `STUDY_SUMMARY.md`
* small non-sensitive configuration files
* Mplus `.inp` syntax files, when they do not contain data

For article repositories, prefer files that explain and reproduce the final or current approved article version. Do not commit every exploratory script merely because it exists.

Before an article enters Git, classify its files into:

* Recommended for Git: `ARTICLE_STATE.md`, `memory.md`, `analysis_plan.md`, final or approved scripts, `manuscript.qmd`, supplement QMD sources, article `.bib`, journal `.csl`, reviewed `reference_audit.md`, small configuration files, and `STUDY_SUMMARY.md`.
* Keep local and exclude from Git: data, full result workbooks, generated `manuscript/output/`, generated Word/PDF/TIFF outputs, logs, caches, diagnostics, Mplus outputs, literature PDFs, and large intermediate objects.
* Needs user decision: exploratory scripts that may contain useful logic, small aggregate result summaries, selected table workbooks, selected figure PDFs, journal-specific `reference.docx` or LaTeX template files, and collaborator-facing materials.

Prefer one private repository per manuscript when the article becomes active enough for version control, especially for submission, revision, or collaboration. Keep the reusable workflow/template repository separate from concrete article repositories.

Suggested article repository naming pattern:

* `<dataset>-<article-slug>`

For article repositories, useful Git milestones include:

* initial article scaffold;
* locked `analysis_plan.md`;
* primary analysis script runs successfully;
* selected tables and figures are defined;
* first complete `manuscript.qmd` draft;
* first visually checked `manuscript.docx`;
* submission version;
* revision response version;
* accepted or final archive version.

Do not commit or upload:

* raw data, cleaned data, individual-level data, or uncertain data exports;
* `.xlsx`, `.csv`, `.sav`, `.rds`, `.RData`, `.dat`, `.gh5`, or large model objects unless explicitly reviewed and approved;
* Word manuscripts, PDFs, TIFFs, rendered previews, caches, logs, backup folders, zip packages, or literature PDF libraries by default;
* all historical exploratory scripts by default;
* generated `results/all/`, diagnostics, or Mplus output folders by default.

Before the first commit, run a dry status review and check for data-like or large files. Do not commit, push, publish, or connect a remote unless the user explicitly requests it.

## 10. Safety And Integrity

Do not invent data, variables, results, citations, coefficients, confidence intervals, P values, sample sizes, ethics details, funding details, or author contributions.

Preserve the distinction between primary, exploratory, diagnostic, and sensitivity analyses. Do not present exploratory findings as prespecified analyses.

Do not infer causality from cross-sectional associations unless the study design supports it.

Do not delete, move, rename, or overwrite files without explicit approval for that operation.

When source files conflict, report the conflict before choosing one.
