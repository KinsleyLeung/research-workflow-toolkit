# mclust Sensitivity Workflow for Latent Profile Projects

> Status: Internal working note migrated from a local methods library. Treat it as a candidate comparison workflow, not as evidence that flexible Gaussian mixtures are interchangeable with conventional LPA. Verify package behavior and model assumptions for each study.

## Purpose and Applicable Research Questions

Use this note when default `mclust` Gaussian mixture modelling is used as a sensitivity or comparison analysis for a primary latent profile analysis. It is appropriate when the project needs to assess whether a covariance-flexible model-based clustering approach produces similar substantive participant profiles.

## Required Variables and Data Structure

- Use the same analytic sample and profile indicators as the primary LPA whenever possible.
- Record all inclusion filters, missing-data rules, indicator transformations, and standardization decisions.
- Keep a reproducible participant ID for merging class assignments back to downstream datasets.
- Inspect raw distributions for bounded, ordinal, highly tied, or zero-inflated indicators before interpreting classes.

## Recommended Model Sequence

1. Run `Mclust()` across a prespecified class range and the default covariance model set.
2. Repeat the screen with several fixed random seeds when initialization includes a subset step.
3. Extract the best BIC for each class count and covariance structure.
4. Refit candidate class counts around the selected solution using the selected covariance model.
5. Export class sizes, entropy or uncertainty summaries, standardized and raw indicator means, within-class SDs, and within-class correlations.
6. Plot adjacent candidate solutions side by side so that interpretability is judged across class counts rather than from the selected solution alone.
7. Run a split-half replication check for the leading candidate solution, matching half-sample profiles by standardized mean vectors.

## Primary Estimator or Inference Method

- Use the package's BIC convention: larger BIC values are preferred, even when values are negative.
- Treat covariance model labels explicitly. A default `mclust` VEV or related solution is not equivalent to a mean-profile LPA with equal diagonal variances.
- Use fixed seeds and save the fitted object only when needed for classification, uncertainty, or later diagnostics.

## Required Diagnostics

- Best BIC by class count and covariance model.
- Number of seeds selecting each class count and covariance model.
- Minimum class size and percentage.
- Mean posterior uncertainty or entropy-like summary.
- Class-specific standardized means and SDs.
- Near-zero within-class SD checks for every raw and standardized profile indicator.
- Empirical within-class correlations and, when useful, model-implied correlations.
- Split-half selected class counts and matched-profile similarity metrics.

## Interpretation Limits

- Do not describe default `mclust` as identical to conventional Mplus LPA unless the covariance restrictions are explicitly matched.
- Flexible covariance models may form classes by dispersion, covariance orientation, zero inflation, ties, or scale endpoints, not only by mean differences.
- Classes with zero or near-zero within-class SD on a profile indicator should be treated as distributional-pile splits and interpreted cautiously.
- If BIC keeps favoring more classes but profile shapes are repetitive or split-half recovery is weak, report the result as exploratory sensitivity evidence rather than selecting the highest-class model for the manuscript.

## Table and Figure Format

- Fit table: class count, covariance model, seed, BIC, loglikelihood, free parameters, entropy or uncertainty, minimum class size.
- Profile table: class size, raw means, standardized means, and within-class SDs.
- Diagnostics table: near-zero within-class SD indicators and within-class correlations.
- Figure: adjacent candidate solutions in the same panel layout with a common y-axis and profile labels ordered by substantive resource level.

## Minimum Results to Report

- Exact analytic N and filters.
- Indicator transformations and standardization.
- mclust version or R session record.
- Class range, covariance model range, and seeds.
- Best BIC by class count.
- Retained or compared class sizes and profile means.
- Diagnostics showing whether classes reflect interpretable mean profiles or distributional/covariance fragmentation.

## Supplementary Reporting Artifacts
