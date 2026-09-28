# Research Workflow Toolkit

A lightweight, reusable framework for moving a research question through design, governed data access, analysis, manuscript drafting, review, and handoff. It contains workflow rules and templates, not study data, a completed analysis, or a universal methods handbook.

## Quick start

Requirements: Git and Python 3. Quarto is needed only when rendering a manuscript; R and method-specific software remain project dependencies.

```bash
git clone https://github.com/KinsleyLeung/research-workflow-toolkit.git
cd research-workflow-toolkit
python3 tools/workflow_toolkit.py init /path/to/new-research-workspace
```

On Windows, `py -3` may be used instead of `python3`. The target directory must be new or empty. The initializer copies the workspace scaffold, `WORKFLOW.md`, and `QUALITY_CONTROL.md`; it does not create a Git repository, project, article, dataset, or software environment.

Next:

1. Read the new workspace's `README.md` and `AGENTS.md`.
2. Review its `.gitignore` against the applicable data-use agreement.
3. Edit `index/workspace_memory.md` to record actual team preferences.
4. Create dataset and article folders only when real work begins.

For a manual installation, copy the contents of [`templates/workspace/`](templates/workspace/) plus `WORKFLOW.md` and `QUALITY_CONTROL.md` into a new directory. Do not copy this repository's top-level `AGENTS.md`; it governs maintenance of the toolkit itself.

Run the repository self-check after changes:

```bash
python3 tools/workflow_toolkit.py check
```

## What is here

| Path | Role |
|---|---|
| [`WORKFLOW.md`](WORKFLOW.md) | Stage gates and handoffs from question to archive |
| [`QUALITY_CONTROL.md`](QUALITY_CONTROL.md) | Design, data, analysis, manuscript, and sharing checks |
| [`templates/workspace/`](templates/workspace/) | Installable, project-neutral workspace scaffold |
| [`tools/workflow_toolkit.py`](tools/workflow_toolkit.py) | Cross-platform initializer and repository self-check |
| [`examples/minimal_quarto/`](examples/minimal_quarto/) | Data-free Quarto smoke test for Markdown and Word output |
| [`methods/`](methods/README.md) | One regression example showing how local method notes can accumulate |
| [`templates/regression/`](templates/regression/) | Generic Word reporting reference for the regression example |
| [`templates/overleaf_article_template/`](templates/overleaf_article_template/) | Optional LaTeX starter for journal-required use |
| [`examples/PBICR2023/`](examples/PBICR2023/) | Optional, data-free dataset-level application example |

The [workspace guide](templates/workspace/README.md) explains the installed files. The [workspace architecture map](templates/workspace/index/workspace_structure_text.md) shows how dataset sources, article folders, complete outputs, selected results, manuscripts, and reusable libraries fit together. The recipient must still supply an authorized dataset and codebook, a defensible research question, project-specific scripts and software, source literature, and current journal instructions.

## Boundaries

Keep this toolkit separate from active research repositories. Do not add participant-level data, controlled documents, article manuscripts, private results, credentials, personal absolute paths, or generated outputs. A private repository is still a sharing boundary: inspect the complete candidate file list and diff before every release or collaboration handoff.

Quarto is the default editable manuscript route in this scaffold; LaTeX is optional and journal-driven. The regression materials are examples of local working knowledge, not mandatory procedures. Adapt the structure to the study design and the team's actual habits instead of expanding the library pre-emptively.

This project is licensed under the [MIT License](LICENSE). See [CONTRIBUTING.md](CONTRIBUTING.md) for the small set of repository contribution rules and [CHANGELOG.md](CHANGELOG.md) for notable changes.
