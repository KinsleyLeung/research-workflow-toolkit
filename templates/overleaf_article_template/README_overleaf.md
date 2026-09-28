# Overleaf Article Template

This folder is a generic local template for an Overleaf/LaTeX manuscript project. Copy it only when the article enters formal manuscript drafting.

Starter defaults: 12 pt, a Times-compatible font when available, left-aligned text, and booktabs tables. These are local layout preferences; journal instructions and the supplied journal class take precedence.

`projects/<DATASET>/articles/<ARTICLE>/manuscript/overleaf/`

Then adapt the title, author information, journal class, bibliography style, section text, tables, and figure paths.

## Intended Boundary

Keep these files in Overleaf:

* `main.tex`
* `supplement.tex`
* `preamble.tex`
* `sections/*.tex`
* `tables/*.tex`
* PDF figures required for compilation
* `references.bib`
* journal `.cls`, `.bst`, and `.sty` files when required

Do not upload these to Overleaf:

* Raw data
* Cleaned data
* Analysis datasets
* `.rds`, `.RData`, `.csv`, `.xlsx`, `.dat`
* Mplus logs and outputs
* Literature PDF libraries
* Large TIFF figures
* Full result caches or diagnostics

Use PDF figures for Overleaf compilation. Keep TIFF figures locally in `figures/selected/` for final journal submission.

## Table Style

The default table style uses `booktabs`:

* Top rule: 1.5 pt
* Header/body rule: 0.5 pt
* Bottom rule: 1.5 pt
* Grouped-header rules: 0.5 pt, disconnected between groups

For grouped headers, use trimmed `\cmidrule` commands, for example:

```tex
\cmidrule(lr){2-3}\cmidrule(lr){4-5}
```

This creates separate short rules under each grouped header rather than one continuous rule.

## Result Source Rule

Tables in `tables/*.tex` should be exported from or checked against manuscript-selected aggregate workbooks in `results/selected/`, typically:

* one workbook for main manuscript tables;
* one workbook for supplementary tables;
* one sheet per table.

Do not manually change numerical results in LaTeX without updating the selected table workbook or documenting the change in `ARTICLE_STATE.md`.

## Source Text Rule

For reusable dataset-level Study design or Measures text, insert the approved `.tex` or `.md` source directly when available. Do not rewrite approved source text unless the user explicitly asks.

For any dataset, use approved study-design and measure sources when they exist. Include only the measures used in the active manuscript. Format measure headings according to the target journal and the selected document class. The snippet below is illustrative only.

```tex
\subsubsection{\textit{Scale Name}}
```
