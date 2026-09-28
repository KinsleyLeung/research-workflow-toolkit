# Repository Agent Instructions

This repository contains reusable research workflows, templates, methods notes, and lightweight examples. It is not a research-data or manuscript repository.

## Operating Rules

1. Read `README.md` and `WORKFLOW.md` first; open other materials only when relevant to the current task.
2. Keep all repository-facing instructions and reusable materials in English. Translate useful non-English source notes and remove project-specific details before migration; preserve the meaning and flag unresolved ambiguity.
3. Keep dataset- and article-specific materials out of the reusable framework. The PBICR2023 example is limited to dataset-level process guidance.
4. Do not add participant-level data, study datasets, article manuscripts, private results, full-text literature files, or other controlled materials.
5. Label internal preferences as local conventions, not universal journal or statistical requirements.
6. Before changing files, state the scope. Do not commit, push, publish, or connect a remote unless explicitly authorized.
7. Keep method notes qualified by their review status, assumptions, software versions, and evidence sources.

## Reading Order

- Framework orientation: `README.md`, then `WORKFLOW.md` and `QUALITY_CONTROL.md` as needed.
- To apply the workflow in a separate research workspace, start from `templates/workspace/README.md` and `templates/workspace/AGENTS.md`.
- For an applied dataset-level example, read `examples/PBICR2023/project_workflow.md`.
- For methods, read `methods/README.md` before using a note.

## Version-Control Boundary

Before staging or committing, inspect the candidate file list and diff for project-specific content, data, results, personal paths, secrets, and generated artifacts. Do not push or change repository visibility by default.
