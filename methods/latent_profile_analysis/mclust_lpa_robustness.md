# mclust LPA Robustness Workflow

> Status: Advanced internal working note. The listed diagnostics are options to match to a specific model-selection concern, not a mandatory checklist. Validate package behavior, implementation, and interpretation against current sources before use.

## Purpose and Applicable Research Questions

Use this workflow when a Gaussian-mixture LPA result needs evidence that an interpretable profile is not only an artifact of covariance parameterization, random initialization, or a continuous severity gradient.

## Required Variables and Data Structure

- One row per participant.
- Continuous or approximately continuous profile indicators with documented scoring directions.
- A locked analytic filter and complete-case rule before mixture estimation.
- Standardized profile indicators for model fitting, with raw scores retained for interpretation.

## Recommended Model Sequence

1. Fit the main candidate covariance model across the candidate class range.
2. Fit diagonal covariance sensitivities, especially EEI and VVI, across the same class range when the substantive comparison is to classic LPA assumptions.
3. Inspect class means in both standardized and raw units for each adjacent candidate solution.
4. Use contingency tables, ARI, and centroid distances to compare adjacent solutions, especially retained K versus K + 1.
5. Use `clustCombi()` to evaluate whether BIC-favored Gaussian components merge into fewer substantive clusters.
6. Run repeated initialization for the focal K and K + 1 solutions; record valid runs, failed runs, log-likelihood/BIC spread, ARI against the best solution, and centroid distances.
7. Run split-half replication by independently fitting the focal model in random half samples and matching centroids to the full-sample reference profile.
8. Add bootstrap stability: fixed-model bootstrap for parameter uncertainty and bootstrap refitting for class-number selection frequency.
9. Test continuous alternatives by comparing a general resource factor, all continuous indicators, profile membership, and profile membership added to continuous models for theoretically relevant external variables.

## Diagnostics to Report

- Exact covariance model names and class range.
- Number of seeds, valid fits, failed or nonfinite-BIC fits.
- BIC, ICL, entropy, minimum class size, AvePP, class means.
- Adjacent-solution ARI and row-normalized cross-classification.
- Which parent class is split by K + 1.
- clustCombi merged-cluster path and clustCombiOptim result.
- Repeated-start distribution of BIC/log-likelihood and ARI against the best valid run.
- Split-half centroid distance, ARI against full-sample classification, and class proportion stability.
- Bootstrap selected-class frequency and any nonfit warnings.
- Incremental tests for profile membership after general-factor and all-indicator continuous alternatives.

## Interpretation Limits

- Do not treat the lowest BIC as sufficient for selecting the substantive profile solution.
- Diagonal and non-diagonal covariance models answer different questions; disagreement should be reported as model-assumption sensitivity, not failure.
- A recurring profile shape across covariance assumptions is stronger evidence than a single best-fit solution.
- `clustCombiOptim()` is a useful cluster-merging aid, not an automatic class-count decision rule.
- If profile membership adds little beyond all continuous indicators, frame profiles as descriptive summaries rather than evidence for configuration-specific effects.
- If profile membership adds information beyond continuous indicators, describe this as configuration evidence only in cross-sectional, noncausal terms unless the design supports stronger claims.
