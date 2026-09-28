# Tables

Store LaTeX table files here.

Table files should be exported from or verified against:

manuscript-selected aggregate workbooks in `results/selected/`, typically one workbook for main manuscript tables and one workbook for supplementary tables, with one sheet per table.

Default table rules:

* `\toprule`: 1.5 pt
* `\midrule`: 0.5 pt
* `\bottomrule`: 1.5 pt
* grouped headers: separate `\cmidrule(lr){...}` segments at 0.5 pt

Do not manually change numerical results here without updating the selected table workbook or documenting the change in `ARTICLE_STATE.md`.
