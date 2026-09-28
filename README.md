# Research Workflow Toolkit

An English-language, reusable framework for taking a research question through design, governed data access, analysis, manuscript drafting, review, and handoff. It is a workflow toolkit, not a dataset, a completed analysis, or a claim that any method note is ready for uncritical use.

## Start a new workspace

1. Read [the stage-based workflow](WORKFLOW.md) and [quality checks](QUALITY_CONTROL.md).
2. Copy the contents of [`templates/workspace/`](templates/workspace/) **and** this toolkit's `WORKFLOW.md` and `QUALITY_CONTROL.md` into a **new, separate** research workspace. Its `README.md`, `AGENTS.md`, `.gitignore`, `index/`, and `shared/` then form the working scaffold. Do not copy this toolkit's top-level `AGENTS.md`; it governs maintenance of the toolkit itself.
3. In the new workspace, read its `README.md` and `index/workspace_structure_text.md`. Replace the generic preferences in `index/workspace_memory.md` with your team's actual choices. Review `.gitignore` against your data-use agreement before using Git.
4. Once you have an authorized dataset, create `projects/<DATASET>/README.md` from the included dataset template, describing governance, authoritative sources, and where approved files are stored. Add a dataset `AGENTS.md` only when the dataset needs distinct rules. Keep the actual data outside this toolkit and, by default, outside Git.
5. For a real article, create `projects/<DATASET>/articles/<ARTICLE>/`; copy `shared/templates/ARTICLE_STATE_template.md` to `ARTICLE_STATE.md` and `memory_template.md` to `memory.md`. Add `analysis_plan.md` at formal analysis, and a `handoff.md` only when handoff is needed. Do not pre-create unused directories.
6. Choose only the relevant note in [`methods/`](methods/README.md), verify it against the study design and current primary sources, and record local decisions in the article analysis plan. If LaTeX is needed, the optional [Overleaf starter](templates/overleaf_article_template/) can be copied into the article manuscript folder.

The [workspace installation guide](templates/workspace/README.md) gives the file map and a concrete first-project walkthrough. The optional [PBICR2023 example](examples/PBICR2023/project_workflow.md) shows a dataset-level process only; it is not needed to use the framework.

**What the recipient must supply:** an authorized dataset and codebook, a defensible research question, project-specific analysis scripts and software environment, any required R packages/Quarto or method-specific software (for example, Mplus), source literature, and the current journal instructions. This toolkit installs none of those and does not reproduce an existing article by itself.

## What is here

| Path | Role |
|---|---|
| [`WORKFLOW.md`](WORKFLOW.md) | Stage gates, reading order, and handoff from question to archive |
| [`QUALITY_CONTROL.md`](QUALITY_CONTROL.md) | Design, data, analysis, manuscript, and sharing checks |
| [`templates/workspace/`](templates/workspace/) | Installable research-workspace scaffold and article templates |
| [`templates/overleaf_article_template/`](templates/overleaf_article_template/) | Optional, generic LaTeX starter |
| [`templates/regression/`](templates/regression/) | Generic Word reporting reference for a specific analysis family |
| [`methods/`](methods/README.md) | Qualified working notes, not validated universal SOPs |
| [`resources/`](resources/) | Optional shared visual convention |
| [`examples/PBICR2023/`](examples/PBICR2023/) | Clearly separate, data-free dataset-level application example |

## Boundaries and migration decisions

The source workspace's reusable English agent rules, article templates, methods notes, Overleaf starter, and manuscript-format guidance were migrated or adapted. Dataset/article files, populated result tables, ethics-bearing Word material, data guides, manuscripts, outputs, logs, full-text papers, and an outdated task handoff were not. The old Chinese workflow note contained a named active article and conflicting manuscript defaults, so its general stage logic was incorporated into `WORKFLOW.md` rather than copied. The current scaffold uses **Quarto as the default editable manuscript source** and LaTeX as an optional journal-driven route; this is a local convention, not a universal standard.

Keep this repository separate from active research projects. A private repository is still a sharing boundary: do not add participant-level data, controlled documents, personal paths, credentials, or unreviewed results. Review the complete file list and contents before committing, connecting a remote, or inviting collaborators. Recheck the optional named example and all third-party material before any public release. The migration changes remain local and uncommitted; no GitHub remote has been connected.
