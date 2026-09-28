# Research Workflow

This is the stage map for a **separate research workspace** created from `templates/workspace/`. At every stage, identify the dataset, article, task, intended output, evidence available, and decision needed. Read only the material required for that task. A protocol, data-use agreement, ethics approval, registered plan, and target-journal instructions take precedence over these defaults.

## Stage-based reading map

| Stage | Read first in the research workspace | Do not read by default |
|---|---|---|
| Workspace setup or new conversation | Root `AGENTS.md`; `README.md`; `index/workspace_memory.md` when local preferences matter; catalog/structure guide when locating files | Article folders, data, results, manuscripts, literature full texts |
| Resume interrupted work | Root `AGENTS.md`; relevant workspace or article `handoff.md`; state/plan files required by the resumed task | Unrelated outputs or old drafts |
| Question and literature | Root and relevant dataset rules; article `ARTICLE_STATE.md` and `memory.md` if an article exists | Raw data, result workbooks, unrelated papers |
| New article | Root and dataset rules; `index/workspace_structure_text.md`; only the needed files in `shared/templates/` | Another article's results or unused templates |
| Exploratory analysis | Article state, relevant decisions, approved data guide, current scripts, relevant method note | Whole manuscripts, unrelated result folders |
| Formal analysis plan | Article state/decisions, verified measures and data provenance, relevant methods | Irrelevant exploratory output |
| Formal analysis | Current `analysis_plan.md`, scripts, authorized inputs, software documentation | Manuscript drafts unless consistency checking requires them |
| Select results and figures | Plan, relevant complete outputs, selected outputs, diagnostics, journal requirements when formatting | Unrelated analyses and old manuscripts |
| Draft manuscript | State, plan, editable manuscript source, selected results/figures, verified references, journal rules | Raw data and the entire exploratory output archive |
| Respond to review | Submitted/current versions, comments, response draft, plan, related code and Git diff | Unrelated articles |
| Summarize or reuse | Final state, decisions, plan, selected results, approved manuscript and scripts | Raw records and large intermediate files |
| Audit Git or migrate | Root rules, `.gitignore`, candidate file list, diff, and file metadata; open selected files for review | Participant-level file contents and unrelated project material |

Do not ask for a dataset or article name if the task can be completed at workspace level. Missing optional files do not block a task; create them only when their purpose arises.

## 1. Establish the scientific question

- State the population, setting, time structure, constructs, outcome or comparison, and intended estimand. Decide whether the aim is descriptive, predictive, explanatory, or causal.
- Explain why the question matters beyond a technical gap. Verify relevant claims against the original literature and identify plausible competing explanations.
- Identify what the design cannot support. Cross-sectional associations alone do not establish temporal order or causality.

**Gate:** the question and design match, and the contribution is credible enough to justify analysis.

## 2. Establish governance and the minimum workspace

- Confirm data access, permitted uses, ethics, storage, dataset version, codebook, and authoritative measurement sources before opening controlled data.
- Keep original data unchanged. Write transformations, exclusions, and derived variables in reproducible scripts. Never infer scoring or coding solely from a column name.
- For a real article, use `ARTICLE_STATE.md` as a short current dashboard and `memory.md` for durable decisions. Add `analysis_plan.md` when formal analysis, a major rerun, or table/figure planning begins. Add `handoff.md` only for a task that needs handoff.
- Create `scripts/`, `results/`, `figures/`, and `manuscript/` only when needed. Keep controlled data and row-level outputs outside the workflow repository and outside Git by default.

**Gate:** provenance, permissions, units of analysis, missing codes, ranges, reverse scoring, and sample filters are documented.

## 3. Lock a defensible analysis plan

Record eligibility and exclusions, missing-data handling, variable construction, primary model and estimand, covariate rationale, uncertainty method, diagnostics, sensitivity analyses, multiplicity families, and planned outputs. Separate primary, secondary, exploratory, diagnostic, and sensitivity work. Mark whether results were already inspected. Date and justify any subsequent amendment; never relabel exploratory choices as prespecified.

**Gate:** a reviewer can tell what was chosen before looking at results and what was changed afterward.

## 4. Analyze and verify

- Generate the analysis sample, models, tables, and figures from code; avoid manual transfer of numerical values into another source of truth.
- Record software/package versions, seeds when relevant, authorized input locations, and the execution order without publishing private paths.
- Check convergence, assumptions, sparse groups, dependence or clustering, influential observations, uncertainty, and model sensitivity. Choose models by question and design, not by significance.
- Keep complete local outputs in `results/all/`, diagnostics in `results/diagnostics/`, and only verified manuscript-facing aggregates in `results/selected/`. Use parallel `figures/all/` and `figures/selected/` only when figures exist.

**Gate:** reported estimates and exclusions can be reproduced from approved inputs and scripts, or the remaining limits are stated explicitly.

## 5. Write, cite, and render

Use `manuscript/manuscript.qmd` as the default single editable source. Generate review Markdown and Word from it, then transfer accepted Word edits back to QMD. Use the optional LaTeX starter only when the journal or author requires it. Generate Excel and manuscript tables from the same model object or tidy result data. Follow `shared/journal_requirements/manuscript_format_requirements.md` only as a local default; journal instructions govern final formatting.

Trace every numerical statement to a checked output and every literature claim to a source that actually supports it. Report effect size and uncertainty, avoid causal or diagnostic claims beyond the design, and distinguish speculation from results.

**Gate:** the text, tables, figures, supplement, references, sample sizes, and code agree; rendered output is visually checked.

## 6. Review, hand off, and archive

- Use `QUALITY_CONTROL.md` to inspect design, analysis, citation support, disclosure risk, and layout before sharing.
- For revisions, preserve the submitted version, map each reviewer point to a response and change, and use Git history to inspect what changed. Git does not replace a dated analysis plan or decision log.
- For a real handoff, record current goal, completed work, unresolved decisions, authorized data location, relevant files, and next actions; never paste sensitive records into a handoff.
- Promote knowledge to `methods_library/`, `topic_library/`, or `shared/` only after the generic rule has been separated from the article and checked for applicability. Do not copy an article's numbers, ethics text, or protected source material into a template.
- Review the exact candidate files before any commit, push, remote connection, or visibility change. Private GitHub is not equivalent to approved data storage.

**Gate:** another authorized collaborator can identify the current source of truth, reproduce the approved analysis, understand amendments, and locate the limitations without receiving data through this toolkit.
