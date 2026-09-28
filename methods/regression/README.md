# Regression Analysis and Reporting

> Status: Local team reporting conventions. Some rules in this document, including table layouts and FDR column labels, are house preferences, not universal statistical standards. The study design, prespecified analysis plan, estimator properties, and target journal take precedence.

## 1. Scope

This method library applies to:

- OLS regression for continuous outcomes.
- Hierarchical or sequential regression.
- HC3 heteroskedasticity-robust inference.
- CR2 cluster-robust inference.
- Subgroup analysis.
- Interaction analysis.
- Simple slopes and Johnson-Neyman analysis.
- MM robust regression and other sensitivity analyses.

## 2. Model Specification

- Model blocks must be determined by the theoretical framework, research question, or prespecified variable hierarchy.
- Model 1 usually includes demographic and structural variables.
- Later models should sequentially add theoretically more proximal variable blocks.
- The final model is the fully adjusted primary model.
- Each model must retain variables from previous models unless the study design explicitly requires replacement.
- Reference categories for categorical variables must be specified before modeling.
- Continuous variables should usually remain in their original continuous form.
- For interactions involving continuous variables, mean-center the continuous variables before constructing product terms.
- The intercept must be retained in complete model outputs and formal regression tables.

## 3. Choice of Statistical Inference

### HC3

Use HC3 heteroskedasticity-robust standard errors when the main concern is heteroskedasticity and there is no clear sampling, geographic, school, community, or other clustering structure that must be modeled.

### CR2 Cluster-Robust Inference

Use CR2 cluster-robust covariance estimates when participants are clearly clustered within cities, schools, communities, or other sampling units and the number of clusters is sufficient for cluster-robust inference. Report the clustering level and the small-sample corrected degrees of freedom.

### Multilevel Models

Use multilevel models when between-group variance, group-level exposures, cross-level effects, or the hierarchical structure itself is part of the research question.

### Sensitivity Use

When clustering may affect inference but the primary analysis uses HC3, CR2 cluster-robust results may be reported as a sensitivity analysis.

The inference method must be determined by study design and data structure, not by statistical significance.

## 4. Multiple-Testing Families

All multiple-testing columns must be named:

`FDR-adjusted P`

Do not use `q value`, `BH-FDR q`, or mixed column names.

Define separate testing families for:

- Overall univariable tests in Table 1.
- Substantive coefficients in the fully adjusted primary model.
- Prespecified interaction terms.
- Overall Wald tests for exploratory interactions.
- A prespecified family of secondary outcomes or exploratory exposures.

Do not include the following in FDR correction:

- Intercept.
- Reference categories.
- Model-fit statistics.
- Simple slopes used to interpret a retained interaction, unless the analysis plan specifies otherwise.

Each table note must state the exact scope of the FDR family.

## 5. Main Regression-Table Display Modes

Use one of the following mutually exclusive main-text display modes.

### Mode A: Full Hierarchical Models in the Main Text

Use when the number of models and predictors is small enough for the main text.

Recommended structure:

- Variable
- Model 1 B (95% CI)
- P
- Model 2 B (95% CI)
- P
- ...
- Fully adjusted model B (95% CI)
- P
- FDR-adjusted P

Rules:

- The first row must be the intercept.
- Only the fully adjusted model receives `FDR-adjusted P`.
- Table notes must define the variable blocks added in each model.
- Report model fit and incremental contribution.

### Mode B: Fully Adjusted Model in the Main Text

Use when there are many models or predictors.

Recommended structure:

- Variable
- B (95% CI)
- [Inference method] SE
- Standardized coefficient β
- t value
- P value
- FDR-adjusted P

Replace `[Inference method] SE` with the actual inference method:

- HC3 robust SE.
- City-clustered CR2 SE.
- School-clustered CR2 SE.
- Another explicitly used inference method.

Place complete hierarchical models and model-fit results in supplementary materials.

Codex should choose Mode A or Mode B based on page width, number of models, and number of variables. Do not place both primary regression-table modes in the main text.

## 6. Categorical Variables and Reference Groups

- Place the categorical variable name on its own row.
- State the reference category in the variable name, for example: `Sex (reference: female)`.
- Do not report a coefficient for the reference category.
- List comparison categories on indented rows below the variable name.
- Retain all non-reference categories for multicategory variables.
- Variable labels and reference categories must match the analysis code.
- Do not change the reference category after seeing regression results.

## 7. Subgroup Analyses and Formal Interactions

### Subgroup Models

Subgroup regression models are primarily descriptive estimates within each subgroup.

Recommended structure:

- Variable
- Subgroup 1 B (95% CI)
- P value
- Subgroup 2 B (95% CI)
- P value

### Formal Interaction Tests

Conclusions about between-group heterogeneity must come from formal interaction tests.

Do not use "significant in one subgroup but not significant in another" as evidence of a between-group difference.

For multicategory moderators:

- Report each interaction contrast.
- Use an overall Wald F test to jointly test all interaction coefficients.
- Apply FDR correction to overall interaction hypotheses.
- Base the main moderation conclusion on the overall Wald test.
- Use individual contrasts only to interpret the direction of differences.

Recommended exploratory interaction table structure:

- Moderator
- Predictor
- Interaction contrast
- B (95% CI)
- Overall Wald F (df1, df2)
- P
- FDR-adjusted P

## 8. Simple Slopes and Johnson-Neyman Analysis

For retained continuous-variable interactions, generate at least:

- Interaction coefficient.
- Simple slopes.
- Conditional effects table.
- Interaction plot.
- Johnson-Neyman analysis.

Calculate simple slopes at:

- Mean - 1 SD.
- Mean.
- Mean + 1 SD.

If the moderator is clearly skewed or bounded by scale limits, use meaningful percentiles instead and state this in the Methods.

Recommended simple-slopes table structure:

- Moderator level
- Conditional B (95% CI)
- Robust SE
- P value

Johnson-Neyman results should report:

- Moderator interval where the conditional association is distinguishable from 0.
- Threshold on the original moderator scale.
- Percentage of the analytic sample within the interval.
- Observed range of the moderator.

Johnson-Neyman plots must not extrapolate beyond the observed moderator range.

Standard wording:

`[Predictor] was positively associated with [outcome] at low (B=[...], 95% CI [...]) and mean (B=[...], 95% CI [...]) levels of [moderator]. At high [moderator], the estimated association was smaller and statistically uncertain (B=[...], 95% CI [...]).`

`Johnson-Neyman analysis indicated that the conditional association was statistically distinguishable from zero at [moderator] scores below/above [threshold], a range containing approximately [percentage]% of the analytic sample.`

## 9. Diagnostics

All primary OLS models must generate at least:

- Outcome distribution plot.
- Residuals vs Fitted.
- Normal Q-Q plot.
- Multicollinearity diagnostics.

Add as needed:

- Scale-Location plot.
- Cook's distance.
- Residuals vs Leverage.
- Influence statistics.
- Leverage and studentized residual diagnostics.

Basic diagnostic figure:

- Panel A: Normal Q-Q plot.
- Panel B: Residuals vs Fitted plot.

Extended diagnostic figure:

- Panel A: Residuals vs Fitted.
- Panel B: Normal Q-Q.
- Panel C: Scale-Location.
- Panel D: Cook's distance.

In large samples, mild Q-Q deviations alone should not invalidate OLS. Judge OLS using heteroskedasticity, influential observations, and robustness checks together.

Recommended collinearity table structure:

- Variable
- GVIF
- df
- Adjusted GVIF

For multi-degree-of-freedom categorical variables, use GVIF^(1/(2*df)) or an equivalent degree-of-freedom-adjusted GVIF.

## 10. Sensitivity Analyses

Sensitivity analyses must be triggered by study design, outcome distribution, or diagnostic results.

### MM Robust Regression

Consider MM robust regression when:

- Potentially high-impact observations are present.
- Residuals show clear tail departures.
- Primary coefficients may be affected by extreme outcome values.
- Stability of OLS coefficient direction and magnitude must be examined.

Recommended structure:

- Variable
- OLS B (SE)
- OLS standardized β
- OLS P
- Robust MM B (SE)
- Robust MM standardized β
- MM P
- ΔB (%)

Interpretation should focus on:

- Whether coefficient directions are consistent.
- Whether primary effect magnitudes are stable.
- Whether conclusions are driven by a small number of influential observations.

Do not judge stability only by whether statistical significance changes.

When OLS B is close to 0, ΔB (%) may be distorted; inspect the absolute difference as well.

Low MM robustness weight indicates potentially influential observations. Do not call them errors or invalid data without evidence.

### Exclusion of Low-Weight Observations

Use only when MM diagnostics indicate a small set of low-weight observations.

Compare:

- Full-sample MM.
- MM after exclusion of prespecified low-weight observations.
- Coefficient direction.
- Change in estimate magnitude.

The weight threshold must be specified before analysis or in the Methods.

### Logistic Regression Sensitivity Analysis

Use only when a continuous outcome has a clinical, theoretical, or practical threshold.

If a top-quartile or other data-driven threshold is used, explicitly label it as exploratory sensitivity analysis.

The purpose is to examine whether results are stable under an alternative outcome definition.

Do not describe dichotomization as solving a continuous-outcome problem.

Recommended structure:

- Variable
- OR (95% CI)
- P
- FDR-adjusted P

If SE is reported, label it as:

`SE of log-odds coefficient`

## 11. Model Fit

For hierarchical OLS, report:

- Model
- R²
- Adjusted R²
- ΔR²
- Block Wald F
- df
- P value

AIC and BIC are optional and are not required for ordinary hierarchical OLS.

Incremental contribution of model blocks should mainly use:

- ΔR².
- Block-level Wald test.
- Fully adjusted model R².

## 12. Main Text and Supplement Allocation

Prioritize the following in the main text:

- Participant characteristics.
- Main regression table.
- Prespecified core interaction table.
- Necessary core interaction figure.

Prioritize the following in supplementary materials:

- Complete hierarchical regression tables.
- Model fit and incremental contribution.
- Complete subgroup regression.
- Exploratory interactions.
- MM robust regression.
- Low-weight-observation sensitivity analysis.
- GVIF.
- Logistic sensitivity analysis.
- Outcome distribution plot.
- OLS diagnostic plots.
- Johnson-Neyman plot.

Use dynamic numbering. Do not fix eTable 1, eTable 2, or other final numbering in the method library.

## 13. Standard Results Wording

### Main Association

`In the fully adjusted model, higher [predictor] was associated with higher/lower [outcome] (B=[...], 95% CI [...]; FDR-adjusted P=[...]).`

### Categorical Comparison

`Compared with [reference category], participants in the [comparison category] group had higher/lower [outcome] scores (B=[...], 95% CI [...]; FDR-adjusted P=[...]).`

### Model Fit

`The fully adjusted model explained [R² percentage]% of the variance in [outcome]. The addition of [block] accounted for an incremental [ΔR² percentage]% of variance (block Wald F=[...], P=[...]).`

### Null or Uncertain Estimate

`The estimated association was small and statistically uncertain (B=[...], 95% CI [...]).`

### Subgroup Analysis

`Stratified estimates are presented descriptively. Formal interaction tests did/did not support differences in the association across [moderator] groups.`

### MM Sensitivity Analysis

`Coefficient directions were unchanged in the MM robust regression, and the principal estimates were similar in magnitude to those from the primary OLS model.`

### Logistic Sensitivity Analysis

`The findings were broadly consistent when [outcome] was modeled using the prespecified binary definition.`
