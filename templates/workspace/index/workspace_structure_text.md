# Research Workspace Structure

This is a placement guide, not a request to create an empty tree. The installable scaffold contains the root rules, `index/`, and `shared/`; create `projects/`, `methods_library/`, or `topic_library/` only when they have real content.

```text
<WORKSPACE>/
  README.md
  AGENTS.md
  WORKFLOW.md
  QUALITY_CONTROL.md
  .gitignore
  index/
    workspace_catalog.md
    workspace_structure_text.md
    workspace_memory.md
  shared/
    journal_requirements/manuscript_format_requirements.md
    templates/ARTICLE_STATE_template.md
    templates/memory_template.md
    templates/analysis_plan_template.md
    templates/handoff_template.md
    templates/dataset_README_template.md
    templates/dataset_AGENTS_template.md
  projects/<DATASET>/                 # create after access is approved
    README.md                          # dataset governance and source pointers
    AGENTS.md                          # only if dataset-specific rules are needed
    articles/<ARTICLE>/                # create for a real article
      ARTICLE_STATE.md                 # current dashboard
      memory.md                        # dated decisions and rejected paths
      analysis_plan.md                 # when formal analysis is ready
      handoff.md                       # only for an interrupted task
      scripts/                          # create when analysis starts
      results/all/                     # full local outputs
      results/selected/                # verified manuscript-facing aggregates
      results/diagnostics/             # checks and errors
      figures/all/                     # generated figures, when any
      figures/selected/                # selected figures, when any
      manuscript/manuscript.qmd        # start when drafting begins
      manuscript/references.bib        # cited references only
      manuscript/output/               # generated review copies
      STUDY_SUMMARY.md                 # only when a useful final summary exists
  methods_library/                    # add reusable methods after review
  topic_library/                      # add cross-article knowledge when useful
  handoff.md                          # optional workspace-level task handoff
```

The article's `ARTICLE_STATE.md` answers **where are we now?** `memory.md` answers **why did we make or abandon these choices?** `analysis_plan.md` is the current formal analysis contract. Git history records file changes, not reasoning or data authorization.

Read state before historical decisions, and read the plan before formal modeling or manuscript generation. Do not scan `results/all/`, data, full-text papers, or other articles unless the active task requires them.
