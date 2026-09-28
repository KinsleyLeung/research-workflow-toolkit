# Manuscript Format Requirements

Purpose: This file records adaptable local defaults for writing, Quarto, Word output, tables, and manuscript quality control. It is not a journal policy. The study protocol and target journal's current instructions take precedence.

## 0. When to read this file

Read this file only when the task involves manuscript drafting, manuscript revision, Word document generation, final table formatting, figure/table captions, journal formatting, or manuscript quality control.

Do not read this file for ordinary data cleaning, exploratory analysis, routine statistical modeling, or intermediate result generation unless manuscript-ready output is being prepared.

For manuscript generation or revision, use this reading order:

1. Root and dataset `AGENTS.md` files.
2. Article `ARTICLE_STATE.md`.
3. Article `memory.md` when historical decisions matter.
4. Article `analysis_plan.md`.
5. Article `manuscript/manuscript.qmd`, when it exists.
6. Article `results/selected/` and `figures/selected/`.
7. This file.
8. The relevant manuscript structure, journal instructions, or `reference.docx`, when provided.

Ignore article `results/all/` and `figures/all/` by default during manuscript drafting unless the user explicitly asks to review exploratory outputs.

## 1. Manuscript structure

The following is an example section map for an empirical article. Adopt it only when it fits the study and the target journal:

```text
ABSTRACT
Objective:
Methods:
Results:
Conclusions:
Keywords:
Background
1 Introduction
2 Methods
  2.1 Study design
  2.2 Measures
  2.3 Statistical Analysis
3 Results
  3.1 Characteristics of the study population
  3.2 Main analysis / primary results
  3.3 Additional analysis / subgroup analysis, if applicable
  3.4 Robustness checks, if applicable
  3.5 Sensitivity analysis
4 Discussion
5 Limitations
6 Conclusion
List of abbreviations
Acknowledgements
CRediT authorship contribution statement
Funding
Declaration of competing interest
Declarations
Consent for publication
References
```

Rules:
- Follow the approved study structure and target-journal instructions where they differ. Do not force unused sections into a manuscript.
- Do not invent sections, results, sample sizes, effect estimates, ethics information, funding sources, or references.
- If required information is missing, mark it as `[NEEDS CONFIRMATION]` rather than fabricating content.
- Keep section headings concise and consistent.
- Use numbered headings for the main text sections from Introduction to Conclusion.
- Abstract headings should usually remain unnumbered.

## 1.1 Source And Output Contract

Use `manuscript.qmd` as the single editable manuscript source.

The default generation path is:

`R analysis -> manuscript.qmd -> manuscript/output/manuscript.md -> manuscript/output/manuscript.docx`

Rules:

- Edit `manuscript.qmd`; do not manually maintain parallel Markdown, Word, and LaTeX master copies.
- Use generated `manuscript/output/manuscript.md` for whole-document content, citation-placeholder, and numerical checking.
- Use generated `manuscript/output/manuscript.docx` for visual quality control, Track Changes, coauthor review, and submission.
- Transfer accepted Word edits back into `manuscript.qmd` before regenerating outputs.
- Insert R results directly into QMD whenever practical. Set random seeds where relevant and record the R/package environment needed to reproduce the output.
- Declare the bibliography and output formats in the QMD front matter using project-relative paths. Reference `reference.docx` only when that file exists and Word styling is required.
- Convert a stable manuscript to LaTeX only when the target journal explicitly requires it.
- Use an approved generic structural reference only when one has been supplied and checked for project-specific content. No Word structure template is bundled here.
- Use `reference.docx`, when present, for document-level Word styles only. Do not expect it to reproduce dynamic table appearance.

## 2. Generated Word Formatting

Default manuscript formatting:

- Font: Times New Roman.
- Font size: 12 pt as a local draft default, subject to journal instructions.
- Line spacing: double-spaced.
- Paragraph indentation: follow the journal or document template; do not assume a language-specific first-line indent.
- Alignment: left aligned for body text unless journal template requires justified text.
- Page margins: use standard manuscript margins unless the target journal specifies otherwise.
- Use consistent spacing before and after headings.
- Avoid decorative formatting.
- Avoid manual line breaks inside normal paragraphs.

## 3. Writing style

General rules:

- Write in formal academic English suitable for SCI journal submission.
- Writing or polishing tools, if available, may help draft Results narrative, but they cannot supply missing evidence or change verified numbers.
- Results narratives should describe only the main findings that support the table or figure in that subsection.
- Use concise, direct, and evidence-based wording.
- Match the strength of claims to the evidence.
- For any cross-sectional analysis, do not infer temporal or causal effects from associations alone.
- Do not overstate statistical significance or causal inference.
- Use “associated with” for observational findings unless the design supports causal inference.
- Use “no clear evidence of an association/difference” rather than “no effect” when uncertainty remains.
- Keep Results factual and compact.
- Reserve interpretation, mechanisms, clinical implications, and comparison with prior studies for Discussion.

Cross-sectional wording rules:

- Preferred wording: `was associated with`, `showed an association with`, `was higher/lower among`, `participants with ... had higher/lower ...`, `the model indicated`.
- Avoid causal wording: `led to`, `resulted in`, `caused`, `affected`, `influenced`, `predicted` when it implies causality, `protective effect`, `risk factor` unless explicitly framed as association. Use `increased` or `decreased` only for descriptive differences or model-estimated score changes, not to imply causation.
- For small statistically significant effects, describe them as `modest`, `small`, or `limited in magnitude` when appropriate.
- Do not turn small coefficients, marginal associations, subgroup patterns, or sensitivity findings into strong claims.
- If an estimate is statistically significant but small, report it accurately and avoid promotional language such as `strong`, `substantial`, `marked`, or `robust` unless the effect size and sensitivity checks justify that wording.

Abstract rules:

- Use a structured abstract when the target journal allows it.
- Recommended subheadings: Objective, Methods, Results, Conclusions.
- Include the study design, sample size, main variables, primary statistical methods, major effect estimates, and conclusion.
- Do not include unsupported background claims in the abstract.

## 4. Statistical notation

Italicize statistical symbols when formatting allows:

- *P*
- *F*
- *t*
- *z*
- *r*
- *β*
- *B*
- *η²*
- *ε²*
- Cramér’s *V*

Usually do not italicize:

- OR
- RR
- HR
- CI
- SE
- SD
- IQR
- AUC
- AUROC
- AIC
- BIC
- RMSEA
- CFI
- TLI
- SRMR

Special cases:

- χ² may be written as χ² in ordinary manuscript formatting.
- If following strict APA-style statistical formatting, χ² may be treated as a statistical symbol and italicized consistently.
- Do not spend excessive effort on χ² styling unless the journal or user explicitly requires it.

Spacing and symbols:

- Use spaces around operators: *P* < 0.001, *r* = 0.35, OR = 1.42.
- Use en dashes for ranges where possible: 18–35 years, 95% CI 0.71–1.87.
- Use a leading zero for values below 1: 0.05, 0.73.
- Report exact *P* values when appropriate.
- Use *P* < 0.001 rather than *P* = 0.000.
- Use consistent decimal places within each table and outcome family.

Recommended reporting examples:

```text
*B* = 0.28, SE = 0.07, 95% CI 0.14–0.42, *P* < 0.001
*β* = 0.16, *t* = 4.21, *P* < 0.001
OR = 1.35, 95% CI 1.12–1.63, *P* = 0.002
χ²(3) = 18.42, *P* < 0.001, Cramér’s *V* = 0.12
```

## 5. Tables

Use SCI-style three-line tables by default.

Table production workflow:

- Numerical truth comes from R analysis objects and reproducible tidy outputs.
- Use `gtsummary` for Table 1 and conventional regression summaries.
- Use `broom` or purpose-built tidy data frames for complex or custom model results.
- Use `flextable` for final Word table formatting in Quarto output.
- When Excel and QMD versions of a table are both required, generate them from the same R model object or tidy result data frame. Do not copy values manually from an Excel workbook into the manuscript.
- If an approved generic table reference exists, use it for visual review; do not use a populated study table as a reusable template.
- Implement table style in code only when the table is needed, and verify the rendered document against the target-journal requirements.
- Use `reference.docx` for manuscript-level Word styles, not as the primary table-formatting mechanism.

Table title:

- Place the title above the table.
- Format as: `Table 1. Title of the table`.
- Bold only `Table 1.`; do not bold the full title unless the target journal requires it.
- Use sentence case for the title.

Three-line table rules:

- Top border: 1.5 pt.
- Header-bottom border: 0.5 pt.
- Bottom border: 1.5 pt.
- When a multilevel header contains separate column groups, use 0.5 pt partial rules beneath the group headers and preserve a visible gap between adjacent group rules. Do not replace these separate group rules with one continuous horizontal line.
- Avoid vertical borders.
- Avoid excessive internal horizontal borders.
- Keep tables compact and readable.

Table layout rules:

- Avoid wide tables when possible.
- Prefer long, narrow tables over overly wide tables.
- If information can be placed in one column without loss of clarity, do not split it into multiple columns.
- Merge cells for repeated group labels when this improves readability.
- Do not merge cells if it makes downstream editing or statistical checking difficult.
- Use clear column names: Variable, Group, Mean ± SD, n (%), Estimate, SE, 95% CI, *P* value.
- Use consistent decimal places.
- Align numbers consistently.
- Put units in column headers when possible.

Table notes:

- Place notes below the table.
- Start with `Note:`.
- Do not bold `Note:`.
- Use notes to define abbreviations, explain model adjustment, clarify reference groups, and specify statistical tests.
- Do not repeat information already obvious from the title or column headers.

Recommended table note examples:

```text
Note: Values are presented as mean ± SD or n (%). CI, confidence interval; SE, standard error.
Note: Model adjusted for the prespecified covariates listed in the analysis plan.
Note: The reference category and model adjustments must match the analysis plan and code.
```

## 6. Figures

Figure title:

- Place the figure title below the figure.
- Format as: `Figure 1. Title of the figure`.
- Bold only `Figure 1.`; do not bold the full title unless the target journal requires it.
- Use sentence case.

Figure rules:

- Use high-resolution figures suitable for journal submission.
- Export formal figures only as PDF and TIFF by default. Use PDF when vector preservation, review, or manuscript assembly is needed; use TIFF for final high-resolution submission.
- Do not generate PNG, JPG, SVG, or repeated preview variants unless explicitly requested.
- Ensure all text in figures is legible after resizing.
- Use consistent font, axis labels, legend style, and decimal formatting across figures.
- Do not use unnecessary colors or decorative effects.
- Every figure must be cited in the text before or near where it appears.

Figure note/caption rules:

- The figure caption should define abbreviations and explain key symbols.
- For forest plots, clearly state the direction of effect.
- For regression plots or interaction plots, specify adjustment variables when applicable.

## 7. Results section format

Use an integrated narrative-evidence structure. Each Results subsection should contain its own relevant text, table, and/or figure together. Do not write all Results paragraphs first and then place all tables and figures later as a separate block.

For each Results subsection, use this order:

1. The subsection heading.
2. A concise paragraph describing only the key findings for that subsection.
3. Citation of the relevant table or figure.
4. The corresponding table or figure immediately after the paragraph, unless the journal explicitly requires all tables and figures at the end.
5. A table note or figure caption immediately attached to that table or figure.

Default Results block pattern:

```text
3.1 Characteristics of the study population

[Narrative summary of sample characteristics and the most important descriptive findings.] (**Table 1**)

Table 1. Descriptive characteristics of participants
[Table 1]
Note: ...

3.2 Main analysis

[Narrative summary of the main model and key estimates.] (**Table 2**)

Table 2. Multivariable regression results
[Table 2]
Note: ...
```

Text citation format:

- Use parenthetical citations such as (**Table 1**) or (**Figure 1**).
- Bold only the table or figure label when Word formatting allows.
- Cite each table and figure in the text before it appears.
- Keep the cited table or figure near the paragraph that discusses it.

Results writing rules:

- Begin with sample characteristics, then primary analysis, then secondary/subgroup/sensitivity analyses.
- Do not duplicate every number from the table in the paragraph.
- Report only the most important estimates in the text.
- When using a writing tool, preserve all verified numerical results exactly and check every substantive claim.
- Avoid interpreting mechanisms in Results.
- Avoid phrases such as “proved,” “confirmed,” or “demonstrated causality” unless the study design justifies them.
- For cross-sectional analyses, use association language and avoid causal interpretation.
- Do not overstate small effect sizes. Statistical significance alone is not enough to describe a result as strong, important, or clinically meaningful.
- If a Results subsection has no corresponding table or figure, it should still contain a clear reason in the narrative, such as a brief diagnostic or sensitivity finding.
- If one subsection needs multiple tables or figures, place each table or figure immediately after the paragraph that introduces it.
- If the target journal requires tables and figures at the end, still draft the manuscript internally as integrated Results blocks first, then move tables and figures only at the final formatting stage.

Example:

```text
The study population included [verified N] participants. Key characteristics are shown in (**Table 1**).

[Insert Table 1 here]
```

Example:

```text
The prespecified exposure was associated with the outcome after adjustment for the planned covariates; the estimate and uncertainty are reported in (**Table 3**).

[Insert Table 3 here]
```

## 8. Methods section expectations

The Methods section should include enough detail for replication.

Minimum required content:

- Study design and setting.
- Participants and eligibility criteria.
- Sample size and missing-data handling.
- Measures, scales, scoring ranges, and interpretation of higher scores.
- Reliability coefficients when applicable.
- Statistical software and package versions when available.
- Model specifications.
- Covariates and rationale for adjustment.
- Sensitivity analyses.
- Statistical significance threshold.
- Ethics approval and informed consent statement.

Measures subsection rules:

- Use `Measures` as the main subsection heading.
- In QMD, a `## Measures` section with level-three measure headings is one workable layout; follow the target journal's hierarchy.
- Include only measures used in the active manuscript.
- Do not insert a full measures source document when only selected scales are needed.
- If the dataset has an approved measures index, read that index and only the sources for measures used by the active article.
- Reuse an `Approved` measure `.md` file as canonical text. Treat a snippet marked as pending verification as a draft that requires source and citation checking before manuscript use.
- Preserve approved wording and core citation keys unless the user explicitly asks for rewriting or journal-specific compression.
- Fill article-specific reliability estimates, assessment timing, scoring implementation, and sample-specific modifications in the active `manuscript.qmd`; do not silently overwrite the reusable canonical snippet.
- Resolve citation keys through the team's reference manager, if used, and ensure the records exist in the article's `references.bib`. If a key cannot be resolved, report it rather than inventing or silently replacing the citation.

For systematic reviews/meta-analyses, include:

- Registration information.
- Reporting guideline, such as PRISMA 2020.
- Databases and search date.
- Eligibility criteria.
- Screening and extraction process.
- Risk-of-bias tool.
- Effect measures.
- Meta-analysis model.
- Heterogeneity statistics.
- Certainty-of-evidence method, such as GRADE.

## 9. Discussion section expectations

Recommended Discussion structure:

1. Principal findings.
2. Comparison with previous studies.
3. Possible explanations or mechanisms.
4. Strengths and implications.
5. Limitations.
6. Conclusion or future directions.

Discussion rules:

- Do not restate all results.
- Explain why the findings matter.
- Separate evidence-based interpretation from speculation.
- Use cautious language for observational, exploratory, underpowered, or low-certainty findings.
- Do not introduce new numerical results that were not reported in Results.

## 10. Abbreviations

Rules:

- Define each abbreviation at first use in the abstract and again at first use in the main text.
- Use a List of abbreviations section when the manuscript contains many abbreviations.
- Keep abbreviations consistent across text, tables, figures, and supplementary files.
- Avoid unnecessary abbreviations for terms used only a few times.

## 11. References

Rules:

- Do not invent references, DOIs, PMIDs, journal names, or publication years.
- Use `manuscript/references.bib` as the article's citation source of truth and keep only references actually cited in the manuscript or supplement.
- Preserve established citation keys from the team's reference manager whenever possible.
- A reference not in the team's reference manager may be added directly to `references.bib` after its authors, title, venue, year, DOI, URL, and document version have been checked against authoritative bibliographic sources.
- Do not treat metadata verification as proof that a source supports a manuscript claim. Check the abstract, full text, original table, or official report when theoretical, methodological, psychometric, numerical, disputed, or strong novelty claims require it.
- If using Zotero/Better BibTeX, do not configure whole-file auto-export to overwrite a bibliography containing entries added outside Zotero. Use whole-file export only when every project entry is managed in the corresponding collection.
- Use Quarto citation syntax such as `[@citekey]` for confirmed references.
- Use `[CITE: concise claim or source requirement]` for unresolved citations during drafting. Do not use vague placeholders or manually typed author-year parentheses as final citations.
- Create `reference_audit.md` only when useful for formal drafting, high-risk citation review, or submission auditing. Record the exact manuscript location, claim, reference, citekey, evidence checked, support level, status, and notes.
- Use audit statuses consistently: `Verified`, `Partial`, `Contextual`, `Metadata only`, `Unresolved`, and `Rejected`.
- Use the target journal's CSL style for rendered in-text citations and the bibliography. CSL does not control manuscript typography, Word paragraph styles, or table appearance.
- Ensure every in-text citation resolves to `references.bib`, remove duplicate records, and identify uncited bibliography entries before submission.
- Search the manuscript and supplement for every `[CITE:` placeholder before submission and resolve or explicitly remove each one.
- Treat citations in generated Word documents as output. Transfer citation changes back to QMD and regenerate rather than creating an independent Word citation system.

## 12. Ethics, funding, and declarations

Include these sections near the end of the manuscript unless the target journal requests another order:

```text
Acknowledgements
CRediT authorship contribution statement
Funding
Declaration of competing interest
Declarations
Consent for publication
References
```

Rules:

- Do not invent ethics approval numbers, consent statements, funding, or author contributions.
- Preserve user-provided ethics approval and consent wording unless asked to revise it.
- Use a no-competing-interests statement only after the authors have confirmed it; do not assume the absence of conflicts.

## 13. Supplementary materials

Use supplementary materials for:

- Long search strategies.
- Extended variable definitions.
- Full model outputs.
- Sensitivity analyses.
- Robustness checks.
- Additional figures that support but do not drive the main narrative.

Rules:

- Main text must remain understandable without reading the supplement.
- Every supplementary table or figure cited in the main text must exist and be numbered consistently.
- Use `Supplementary Table S1`, `Supplementary Fig. S1`, etc.
- Avoid conflicting numbering between main and supplementary figures.

## 14. Quality-control checklist before final Word export

Before generating the final manuscript Word file, check:

- [ ] All headings follow the approved structure.
- [ ] Font follows the journal or approved document template (Times New Roman is a local draft default).
- [ ] Font size follows the journal or approved document template (12 pt is a local draft default).
- [ ] Line spacing follows the journal or approved document template (double spacing is a local draft default).
- [ ] Body paragraph indentation follows the journal or approved document template.
- [ ] Statistical symbols are italicized where appropriate.
- [ ] Tables follow the journal or approved local format (three-line tables are a local default).
- [ ] Table titles are above tables and formatted as `Table 1. Title`.
- [ ] Figure titles are below figures and formatted as `Figure 1. Title`.
- [ ] Every table and figure is cited in the text.
- [ ] Results subsections contain a concise narrative before tables/figures.
- [ ] Results narratives use association wording for cross-sectional analyses.
- [ ] Small effect sizes are not overstated.
- [ ] Notes below tables begin with `Note:` and are not bold.
- [ ] No placeholder text remains unless explicitly marked as `[NEEDS CONFIRMATION]`.
- [ ] No invented references or unsupported claims are included.
- [ ] Section numbering is continuous and correct.
- [ ] Supplementary table and figure numbering is consistent.
- [ ] Ethics, funding, competing interest, and consent statements are present when required.

## 15. Default instruction for Codex

When generating or revising a manuscript:

1. Read the workspace and dataset rules, article state, and current analysis plan first.
2. Read this file and the target journal's current instructions before formatting.
3. Read verified project-specific outputs, tables, figures, citations, and user instructions before writing. Use an approved manuscript structure only when one is actually available.
4. Build the Results section as integrated subsection blocks: heading, relevant narrative, immediate table/figure, and note/caption.
5. When writing tools are used, verify all claims and preserve the checked numerical results.
6. Preserve all verified numerical results exactly.
7. For cross-sectional analyses, avoid causal wording and do not overstate small effects.
8. Mark missing information clearly instead of inventing it.
9. Produce a brief change log after revision.
