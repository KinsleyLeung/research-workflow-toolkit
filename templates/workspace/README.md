# Research Workspace

This directory is the installable, project-neutral workspace scaffold. Normally install it with `python3 tools/workflow_toolkit.py init <target>` from the toolkit repository. For a manual installation, copy **its contents** into a new research directory and also copy the toolkit's `WORKFLOW.md` and `QUALITY_CONTROL.md`. Do not work inside the template directory. The new workspace is separate from the workflow toolkit and may contain governed projects; the toolkit itself must not.

## First setup

1. Review this file, `AGENTS.md`, `index/workspace_structure_text.md`, and `.gitignore`. Edit `index/workspace_memory.md` to reflect the receiving team's real preferences; its defaults are examples, not universal rules.
2. Confirm approved data storage, who may access it, and whether any Git repository is appropriate. `.gitignore` reduces accidental staging but is not a security control: inspect every candidate file before sharing.
3. When an authorized dataset is available, create `projects/<DATASET>/README.md` from `shared/templates/dataset_README_template.md`, retaining only non-sensitive governance and provenance pointers. Add a dataset-specific `AGENTS.md` from `dataset_AGENTS_template.md` only if it needs rules beyond the workspace file. Keep the source codebook, questionnaire, data, and consent/ethics records in approved storage.
4. When an article becomes active, create `projects/<DATASET>/articles/<ARTICLE>/`. Copy `shared/templates/ARTICLE_STATE_template.md` and `memory_template.md` there as `ARTICLE_STATE.md` and `memory.md`. Fill in only verified facts. Add `analysis_plan.md` from the template when primary analysis or a major rerun is ready; add `handoff.md` from its template only for a real handoff.
5. Put scripts and generated outputs in article-specific folders as needed. For formal drafting, start one `manuscript/manuscript.qmd`; keep its references in `manuscript/references.bib`. The optional LaTeX starter lives in the **toolkit** at `templates/overleaf_article_template/`, not in this scaffold.

No dataset, article, empty `projects/` directory, or example data is installed by default. A colleague with a different dataset must use their own dataset name, measures, design, approved sources, and analysis plan. Any examples in the separate toolkit are optional and are not prerequisites.

This scaffold does not install R, Quarto, Mplus, packages, citations, data, or analysis scripts. Confirm the software environment needed by the chosen project and method, and record versions and run order in the article plan or scripts.

## What the files do

| File or directory | Role |
|---|---|
| `AGENTS.md` | Stage-based operating and safety rules for an AI collaborator |
| `index/workspace_catalog.md` | Quick navigation and reading map |
| `index/workspace_structure_text.md` | Directory placement and when to create files |
| `index/workspace_memory.md` | Editable local conventions and stable preferences |
| `shared/templates/` | Dataset guidance, article state, durable decisions, formal plan, and optional handoff templates |
| `shared/journal_requirements/manuscript_format_requirements.md` | Manuscript defaults requiring journal-specific review |
| `.gitignore` | Conservative local version-control exclusions |
| `WORKFLOW.md`, `QUALITY_CONTROL.md` | Copy from toolkit root; full stage map and review gates |

## A minimal first article

After creating `projects/STUDY_A/articles/QUESTION_1/`, an early article needs only `ARTICLE_STATE.md` and `memory.md`. Its dataset `README.md` should point to the authorized data guide; do not reproduce protected variables or records in this generic scaffold. At formal analysis, document the sample, variables, estimand, models, diagnostics, and amendments in `analysis_plan.md`. Generate `scripts/` and `results/` only when analysis starts. Draft and render the manuscript only after selected results have been verified.

The `index/` files are **navigation and conventions**, not task handoffs. Put a workspace-level `handoff.md` at the workspace root and an article-level handoff in the article folder when needed.
