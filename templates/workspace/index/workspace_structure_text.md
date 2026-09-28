# Research Workspace Architecture

This is the canonical placement map for a receiving research workspace. It describes responsibilities and information flow; it is not a request to create every folder in advance. Create a path only when active work needs it.

## 1. Workspace Areas

```text
<WORKSPACE>/
├── README.md                         # human orientation
├── AGENTS.md                         # AI operating and safety rules
├── WORKFLOW.md                       # stage sequence and review gates
├── QUALITY_CONTROL.md                # design, analysis, writing, and sharing checks
├── index/                            # maps, conventions, audits, cleanup inventories
├── shared/                           # cross-project formats, templates, and resources
├── projects/                         # dataset projects and their articles
├── methods_library/                  # reviewed methods reusable across articles
├── topic_library/                    # reusable theory, constructs, and literature logic
└── handoff.md                        # optional workspace-level task handoff
```

| Area | Use it for | Create or read it when |
|---|---|---|
| `projects/` | Dataset governance, shared sources, and article-specific work | A real dataset or article is active |
| `methods_library/` | Qualified statistical procedures, code patterns, reporting rules, and recurring pitfalls | A method has become reusable after real use and review |
| `topic_library/` | Cross-article theory, construct definitions, topic logic, and selected literature notes | Knowledge is useful beyond one article |
| `shared/` | Dataset-independent templates, formatting guidance, journal resources, and common assets | Several projects may use the same resource |
| `index/` | Navigation, structure, stable local conventions, audits, and cleanup inventories | Locating, designing, auditing, or reorganizing the workspace |
| `handoff.md` | A concise resume point for an interrupted workspace task | Work is long, blocked, cross-person, or likely to resume later |

`index/` is not an output folder or a task diary. `shared/` is not a miscellaneous dumping area. Article-specific decisions and results stay with the article.

## 2. Dataset Project

Use one dataset-level project when several articles share data governance, study design, questionnaire sources, measures, or stable coding definitions.

```text
projects/<DATASET>/
├── README.md                         # governance, provenance, and source pointers
├── AGENTS.md                         # optional dataset-specific rules
├── dataset_overview.md               # reusable design and population overview, when useful
├── data_guide.md                     # variable names, coding, modules, and stable definitions
├── source_documents/                 # authoritative design, measure, and questionnaire sources
│   ├── Study_design/                 # approved reusable study-design text
│   ├── Measures/
│   │   ├── README.md                 # measure-library rules
│   │   ├── measures_index.md         # snippet navigation and approval status
│   │   └── <measure>.md              # one reviewed measure snippet per file
│   ├── questionnaire_or_codebook/    # original wording, scoring, missing codes, skip logic
│   └── related/                      # protocols, registrations, and supporting sources
└── articles/<ARTICLE>/               # one article's state, analysis, outputs, and manuscript
```

Names under `source_documents/` may vary by dataset. Preserve a clear source-authority order in the dataset `AGENTS.md`; an existing file is not automatically an approved source.

### Source lookup flow

For study design or measure text:

```text
active article and analysis_plan.md
-> data guide identifies the variable, construct, and questionnaire module
-> source index identifies the approved reusable text
-> approved Markdown snippet is reused without silent paraphrase
-> original questionnaire or codebook is consulted only when verification is needed
-> citation keys are resolved in the article references.bib
-> article-specific sample, scoring, or reliability details are added in manuscript.qmd
```

Use only sources and measures required by the active article. Do not copy the full source library into every manuscript.

## 3. Article Project

```text
projects/<DATASET>/articles/<ARTICLE>/
├── ARTICLE_STATE.md                  # current question, stage, blockers, and next actions
├── memory.md                         # dated decisions, amendments, rejected paths, and pitfalls
├── analysis_plan.md                  # current formal analysis and output contract
├── handoff.md                        # optional interrupted-task handoff
├── data/                             # optional local-only article inputs or software exchange
├── scripts/                          # analysis and output-generation code
├── results/
│   ├── all/                          # complete, exploratory, candidate, and machine-readable outputs
│   ├── diagnostics/                  # assumptions, convergence, sensitivity, errors, and QA
│   └── selected/                     # verified aggregates selected for the current manuscript
├── figures/
│   ├── all/                          # all generated figures
│   └── selected/                     # figures selected for the current manuscript
├── manuscript/
│   ├── manuscript.qmd                # single editable manuscript source
│   ├── supplement.qmd                # create only when a supplement exists
│   ├── references.bib                # references cited by this article
│   ├── journal.csl                   # create when an article-specific style is needed
│   ├── reference.docx                # create when Word styles are needed
│   ├── reference_audit.md            # create for formal or high-risk citation review
│   ├── output/                       # generated Markdown, Word, and submission copies
│   └── overleaf/                     # optional late-stage or journal-required LaTeX source
└── STUDY_SUMMARY.md                  # optional final aggregate summary and reusable lessons
```

The state files have distinct jobs: `ARTICLE_STATE.md` answers **where are we now?**; `memory.md` answers **why did we make or abandon these choices?**; `analysis_plan.md` states **what analysis and manuscript outputs are currently authorized?**; Git records **what changed in files?**

The optional `data/` directory is controlled local storage, not a sharing location. Do not put row-level data, software exchange data, model objects, or generated outputs in Git by default.

## 4. Result Promotion

Use a one-way evidence path:

```text
approved inputs
-> scripts
-> results/all + results/diagnostics
-> scientific and technical review
-> analysis_plan amendment when the design changes
-> results/selected + figures/selected
-> manuscript.qmd
-> manuscript/output
-> STUDY_SUMMARY.md and reusable libraries, when justified
```

`results/all/` may contain descriptive statistics, sample flow, candidate models, primary models, model fit, robustness checks, sensitivity analyses, subgroup analyses, interactions, and software-exchange outputs. Organize it by result type or analysis purpose instead of creating many duplicate fragments.

`results/selected/` is not a significant-results folder. It contains only checked, aggregate outputs adopted by the current manuscript design. A result enters `selected/` only after it is consistent with the current `analysis_plan.md`; changes made after inspecting results must be recorded as an amendment. Manuscript drafting reads `selected/` by default and does not search `all/` for a preferable result.

Create only the paths required by the current stage. Read state before history, the analysis plan before formal modeling, and selected outputs before manuscript drafting. Do not scan raw data, full `results/all/`, source archives, literature libraries, or other articles unless the active task requires them.
