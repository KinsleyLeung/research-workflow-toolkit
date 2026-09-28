# Hierarchical OLS Regression and Interaction Workflow

> Status: Draft internal workflow. Use only when the outcome, sampling design, estimand, and model assumptions support OLS. The sequence and inference choices must be justified for the active study, not selected from significance patterns.

## 1. Scope

Use this workflow for cross-sectional or observational studies with a continuous outcome analyzed using ordinary least squares (OLS) regression, including hierarchical model building, subgroup analyses, interaction tests, and sensitivity analyses.

The workflow standardizes analysis decisions, output files, tables, figures, and manuscript reporting. Article-specific variables, coefficients, sample sizes, and conclusions remain in the article folder.

## 2. Required analysis specification

Before fitting models, create or confirm an article-level `analysis_plan.md` containing:

```markdown
Outcome:
Primary predictors or exposures:
Covariate blocks and theoretical order:
Reference categories:
Primary fully adjusted model:
Primary covariance estimator: conventional / HC3 / CR2 cluster-robust
Cluster level, if applicable:
Primary FDR family:
Prespecified interactions:
Exploratory interaction family:
Subgroup analyses:
Diagnostic criteria:
Sensitivity analyses and activation rules:
Main-table display: hierarchical models / full model only
```

The model sequence must be theoretically defined before inspecting coefficient significance.

## 3. Data preparation

1. Verify variable coding, ranges, direction, reference categories, missingness, and analytic sample size.
2. Summarize continuous variables using mean (SD) when appropriate; add median (IQR) when distributions are strongly skewed.
3. Summarize categorical variables using number (%).
4. Record all exclusions and changes in sample size.
5. Mean-center continuous variables used in interaction terms. Centering changes the interpretation of lower-order terms but does not change the interaction coefficient or model fit.
6. Retain the continuous outcome for the primary OLS analysis. Dichotomization is reserved for a clinically, theoretically, or operationally meaningful sensitivity definition.

## 4. Primary hierarchical OLS models

### 4.1 Model sequence

Enter predictors in prespecified theoretical blocks. Designate the final model as the primary fully adjusted model.

For each model, retain:

- Unstandardized coefficient B
- 95% confidence interval
- Robust or cluster-robust standard error
- Standardized coefficient β when useful for relative magnitude
- t statistic and two-sided P value
- R² and adjusted R²
- ΔR² for each added block
- Robust block-level Wald F test and degrees of freedom when robust inference is used

Always retain the intercept in generated results and manuscript regression tables.

### 4.2 Covariance estimator

Choose the inferential method from the data structure:

- Use HC3 heteroscedasticity-robust standard errors when heteroscedasticity is the principal concern and no defensible clustering level is required.
- Use CR2 cluster-robust inference when observations are meaningfully nested within a prespecified cluster such as city, school, or community and the number of clusters is adequate. Report the cluster level and small-sample-adjusted degrees of freedom.
- Use HC3 as primary and CR2 as sensitivity analysis when clustering is plausible but the primary cluster definition is uncertain.
- Use a multilevel model when between-cluster variance or cluster-level effects are part of the research question.

The table header must name the actual estimator, for example `HC3 robust SE` or `City-clustered CR2 SE`.

## 5. Multiple-testing control

Use the label **FDR-adjusted P** consistently in tables, notes, Results, and supplements.

Define separate FDR families for conceptually distinct hypothesis sets. Typical families are:

1. Univariable comparisons in Table 1
2. Substantive coefficients in the fully adjusted primary model
3. Prespecified interaction hypotheses
4. Exploratory overall interaction hypotheses
5. A defined family of secondary outcomes or service-specific predictors

Do not include the intercept, reference rows, model-fit statistics, or simple-slope estimates in the primary-model FDR family unless the analysis specification explicitly requires this.

For a multi-category moderator, apply FDR correction to the overall interaction hypothesis rather than treating each dummy interaction coefficient as an independent primary hypothesis.

## 6. Main manuscript tables

### Table 1. Participant characteristics and univariable comparisons

Recommended columns:

`Characteristic | No. (%) | [Outcome] Score, Mean (SD) | t/F value | P value | FDR-adjusted P`

Rules:

- Place each categorical variable name on a separate parent row.
- Report the variable-level t or omnibus F statistic, P value, and FDR-adjusted P on the parent row.
- List categories on indented child rows with No. (%) and outcome mean (SD).
- Do not repeat the variable-level test on category rows.
- State in the note that binary variables used independent-samples t tests and variables with more than two categories used one-way analysis of variance, or name the alternative tests actually used.
- Use `sample mean`, not `national mean`, unless a nationally representative weighted estimator was used.

### Primary regression table: choose one display

#### Option A. All hierarchical models in the main manuscript

Use when the number of models and predictors fits legibly on the page.

For each model report `B (95% CI)` and `P`; add `FDR-adjusted P` only for the fully adjusted model. Include the intercept as the first row. Place each categorical predictor on a parent row with its reference category, followed by indented comparison categories.

#### Option B. Fully adjusted model in the main manuscript

Use when the full hierarchical table is too wide or long.

Recommended columns:

`Variable | B (95% CI) | [Inference method] SE | Standardized coefficient β | t value | P value | FDR-adjusted P`

Place the complete hierarchical models and model-fit table in the supplement.

### Model-fit table

Recommended columns:

`Model | R² | Adjusted R² | ΔR² | Block Wald F (df1, df2) | P value`

AIC and BIC are optional descriptive additions and are not required for standard hierarchical OLS reporting.

## 7. Subgroup analyses

Use subgroup models to describe stratum-specific estimates. Recommended columns:

`Variable | Subgroup 1 B (95% CI) | P value | Subgroup 2 B (95% CI) | P value`

The subgroup models should use the same covariate set as the fully adjusted primary model unless a variable is structurally unavailable within a stratum.

Differences in significance across subgroup models do not establish effect heterogeneity. Base claims of heterogeneity on a formal interaction test.

## 8. Interaction analyses

### 8.1 Prespecified interaction

Fit the interaction in the fully adjusted primary model. Report the two lower-order terms and the interaction term.

Panel A columns:

`Term | B (95% CI) | [Inference method] SE | P value | FDR-adjusted P`

For continuous moderators, also report conditional effects.

Panel B columns:

`Moderator level | Conditional B (95% CI) | [Inference method] SE | P value`

Use mean and mean ±1 SD when these values fall within the observed range and provide interpretable contrasts. For bounded or strongly skewed moderators, use prespecified percentiles such as the 10th, 50th, and 90th percentiles.

Recommended Results wording:

> [Predictor] was positively associated with [Outcome] at low (B = [value], 95% CI [lower] to [upper]) and mean (B = [value], 95% CI [lower] to [upper]) levels of [Moderator]. At high [Moderator], the estimated association was smaller and statistically uncertain (B = [value], 95% CI [lower] to [upper]).

Use `statistically uncertain` when the confidence interval includes zero; avoid interpreting a non-significant simple slope as proof of no association.

### 8.2 Johnson-Neyman analysis

Use Johnson-Neyman analysis for continuous moderators when the interaction is substantively relevant. Report:

- The threshold or interval in the moderator's original units
- Whether the conditional effect is distinguishable from zero below, above, or within that interval
- The percentage of the analytic sample within the relevant region
- A figure restricted to the observed moderator range

Recommended wording:

> Johnson-Neyman analysis indicated that the conditional association was statistically distinguishable from zero at [Moderator] scores below [threshold], a range containing approximately [percentage]% of the analytic sample (eFigure [X] in the Supplement).

Recommended figure title:

> eFigure [X]. Johnson-Neyman analysis of the association between [Predictor] and [Outcome] across levels of [Moderator]

### 8.3 Exploratory interaction family

Recommended columns:

`Moderator | Predictor | Interaction contrast | B (95% CI) | Overall Wald F (df1, df2) | P value | FDR-adjusted P`

Rules:

- For a binary moderator, the interaction coefficient and one-degree-of-freedom overall test are equivalent.
- For a multi-category moderator, list each contrast but report the joint Wald test once for the predictor-moderator hypothesis.
- Apply FDR correction across the prespecified set of overall interaction hypotheses.
- Treat individual contrasts as descriptive when the overall interaction test is the inferential target.

## 9. Diagnostics

Generate at least:

1. Residuals vs Fitted
2. Normal Q-Q

Add when useful:

3. Scale-Location
4. Cook's distance
5. Residuals vs Leverage

Also report GVIF and the degrees-of-freedom-adjusted form `GVIF^(1/(2×df))` for multi-level categorical predictors.

In large samples, modest Q-Q departures are common. Interpret diagnostics jointly with heteroscedasticity, leverage, influence, and coefficient stability rather than rejecting OLS from the Q-Q plot alone.

## 10. Sensitivity analyses

### 10.1 Cluster-robust or HC3 sensitivity

When the primary estimator does not address a plausible alternative dependence structure, refit the fully adjusted model using the alternative covariance estimator and compare coefficient direction, magnitude, confidence intervals, and inference.

### 10.2 MM robust regression

Use MM-estimator robust regression when diagnostics indicate influential observations, heavy residual tails, or concern that a small set of observations may materially affect coefficients.

Recommended comparison columns:

`Variable | OLS B (SE) | OLS β | P value | MM B (SE) | MM β | P value | ΔB (%)`

Calculate:

`ΔB (%) = 100 × (B_MM − B_OLS) / |B_OLS|`

When the OLS coefficient is close to zero, percentage change is unstable; report the absolute coefficient difference and interpret cautiously.

MM model-based standard errors may not incorporate the same clustering correction as the primary OLS model. Use MM primarily to evaluate coefficient direction and magnitude stability. A change in statistical significance alone does not establish instability.

Low MM robustness weights identify observations receiving less influence in the robust fit. Do not label them data errors or outliers without substantive verification.

### 10.3 MM analysis after excluding low-weight observations

If a prespecified weight threshold is used, compare the full-sample MM model with the MM model after exclusion. Report the threshold, number and percentage excluded, and coefficient changes. Keep the primary OLS analysis based on the full eligible sample.

### 10.4 Logistic sensitivity analysis

Use logistic regression only when a meaningful binary outcome definition exists, such as a validated clinical threshold, a policy-relevant cutoff, or a clearly labeled exploratory upper-quantile definition.

Recommended columns:

`Variable | OR (95% CI) | P value | FDR-adjusted P`

If an SE column is retained, label it `SE of log-odds coefficient`; it is not the standard error of the odds ratio.

The logistic model tests robustness to outcome definition. It does not repair a continuous outcome and should not replace the primary OLS analysis solely because the continuous outcome is bounded or non-normal.

## 11. Figures

### eFigure 1. Outcome distribution

Title:

> eFigure [X]. Distribution of [Outcome] Scores Among Study Participants

Note:

> The dashed line indicates the overall sample mean.

### eFigure 2. OLS diagnostic plots

Basic version:

> (a) Normal Q-Q plot; (b) Residuals vs Fitted plot

Extended version:

> (a) Residuals vs Fitted; (b) Normal Q-Q; (c) Scale-Location; (d) Cook's distance

### Figure style

- Use Times New Roman throughout.
- Use restrained scientific colors.
- Use sequential gradients for ordered or continuous values.
- Use balanced diverging colors for effects around a reference value.
- Use clearly distinguishable contrast colors for categorical groups.
- Avoid rainbow palettes, fluorescent colors, decorative effects, and unnecessary saturation.
- Save complete figures to `figures/all/` and manuscript-ready versions to `figures/selected/`.

## 12. Output routing

Generate complete machine-readable outputs first:

- `results/all/`: all model coefficients, tests, model fit, simple slopes, Johnson-Neyman intervals, and sensitivity analyses
- `results/diagnostics/`: residual diagnostics, influence statistics, GVIF, and error logs
- `figures/all/`: all generated figures

After result selection:

- `results/selected/`: manuscript-ready tables and selected estimates
- `figures/selected/`: manuscript-ready figures

The main manuscript should normally contain Table 1, one primary regression display, and the principal prespecified interaction table or figure. Full hierarchical results, diagnostics, exploratory subgroup analyses, exploratory interaction families, and sensitivity analyses usually belong in the supplement.

## 13. Manuscript reporting checklist

Before finalizing the Results and supplement, verify that:

- The analytic sample size is consistent across text, tables, and figures.
- The intercept appears in regression tables.
- Reference categories are explicit.
- The actual robust inference method and cluster level are named.
- FDR families are defined and the label `FDR-adjusted P` is used consistently.
- Main conclusions rely on the fully adjusted primary model.
- Subgroup heterogeneity claims rely on interaction tests.
- Simple slopes and Johnson-Neyman results are reported for relevant continuous interactions.
- Sensitivity analyses are interpreted through coefficient stability, not significance switching.
- `sample mean` is used unless national representativeness is justified.
- All table and figure values are traceable to verified result files.
