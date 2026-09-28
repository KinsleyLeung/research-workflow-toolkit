# Quality Control

Use these checks at the scale warranted by the study. A completed checklist does not substitute for expert review or justify a model that does not match the design.

## Research question and design

- Is the question important, focused, and answerable with the available design and measurements?
- Are population, time frame, exposure or grouping, outcome, and intended estimand explicit?
- Are identification assumptions and plausible alternative explanations stated?
- Do claims stay within the observational, temporal, and measurement limits of the data?

## Data and measurement

- Is the data version authorized and recorded? Is the original preserved unchanged?
- Are filters, duplicate handling, missingness, value ranges, coding, scoring direction, reverse scoring, and scale construction documented?
- Are measures and coding verified against authoritative source materials rather than inferred from column names?
- Are individual-level data and sensitive information kept outside the shared workflow repository?

## Statistical analysis

- Was the primary analysis plan recorded before confirmatory interpretation? Are amendments dated and explained?
- Does the estimator fit the outcome scale, sampling structure, distribution, and research question?
- Are convergence, model assumptions, uncertainty, influence, class/group size, and relevant diagnostics assessed?
- Are multiple-testing families and sensitivity analyses defined by the scientific question, not selected after seeing significance?
- Are primary, secondary, exploratory, diagnostic, and sensitivity results clearly separated?
- Are substantive interpretations supported by effect sizes and uncertainty, not only P values?

## Manuscript and outputs

- Can every number in text, tables, and figures be traced to a reproducible output?
- Do manuscript sample sizes, exclusions, variables, model labels, tables, and supplements agree?
- Does each citation exist and support the exact claim attached to it?
- Has the rendered manuscript been checked for clipping, unreadable tables, broken references, and figure quality?
- Are target-journal instructions followed? They supersede local defaults and templates.

## Reproducibility and sharing

- Can scripts run from documented inputs without relying on an unrecorded absolute local path?
- Are software versions, seeds, outputs, and known limitations reported where relevant?
- Has the final Git change list been reviewed for data, results, personal paths, credentials, temporary files, and third-party material?

## Adaptable local defaults

The installable scaffold uses a single editable Quarto manuscript, tables generated from the same analysis objects as their manuscript values, and restrained noncausal language for cross-sectional findings. These are starting conventions, not universal methodological rules; use the target journal, protocol, and analysis plan where they differ. Edit `index/workspace_memory.md` in the receiving workspace to record the team's actual choices.
