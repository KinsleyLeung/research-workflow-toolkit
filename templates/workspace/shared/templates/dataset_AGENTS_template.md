# <DATASET>: Dataset Agent Instructions

Use this file at `projects/<DATASET>/AGENTS.md` **only when dataset-specific rules are needed**. The workspace root `AGENTS.md` still applies. Replace prompts with verified project rules; do not paste controlled data into this template.

## Access and protected material

- Approved data source and access route:
- Storage boundary and authorized collaborators:
- Files or output types that must stay local or within approved institutional storage:
- Prohibited uploads, exports, and row-level disclosures:

Do not assume that a private repository is an approved data location. Do not print participant-level records into a chat, log, manuscript, or handoff.

## Source authority

1. Approved protocol/study-design source:
2. Approved measure documentation and status index:
3. Original questionnaire/codebook for item wording, scoring, missing codes, and skip logic:
4. Analysis-facing data guide for column names and stable coding notes:
5. Article-specific analysis outputs for sample counts, reliability, and model-specific details:

An existing document is not automatically approved. Resolve conflicts with the designated project lead. Preserve approved shared wording unless its status or the article-specific need requires revision. Use only the measures relevant to the active article, and verify citation keys in that article's bibliography.

## Where work belongs

Keep dataset-wide design, measurement sources, and governance pointers at dataset level. Put each article's `ARTICLE_STATE.md`, `memory.md`, `analysis_plan.md`, scripts, results, figures, and manuscript under `articles/<ARTICLE>/`. Do not place one article's coefficients, decisions, or selected outputs in the dataset root as if they were shared facts.

## Git and sharing

Review the candidate file list and its contents before versioning or sharing. Only approved, non-sensitive logic and small reviewed summaries may be considered. Data, individual-level exports, controlled source documents, generated model output, and manuscript packages remain outside Git unless the data-use agreement and project lead explicitly allow a specific exception.
