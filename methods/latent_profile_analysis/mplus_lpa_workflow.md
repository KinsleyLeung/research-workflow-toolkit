# Mplus Latent Profile Analysis Workflow

> Status: Internal working note migrated from a local methods library. Numeric examples for class ranges and random starts are practical starting points, not universal requirements. Verify parameterization, enumeration, auxiliary-variable procedures, and software-version details against current primary sources before using this as a team SOP.

## Purpose and Applicable Research Questions

Use this note for cross-sectional latent profile analysis with continuous profile indicators when the goal is to identify participant subgroups based on multivariate behavior, psychosocial, or health-resource patterns.

## Required Variables and Data Structure

- One row per participant.
- Continuous profile indicators with documented scoring direction.
- Explicit inclusion/exclusion filters before profile estimation.
- A reproducible ID variable for merging Mplus posterior classifications back to the analytic dataset.

## Recommended Model Sequence

1. Prepare a complete-case profile-indicator dataset after applying prespecified analytic filters.
2. Transform severely skewed indicators before standardization when justified, and record the transformation.
3. Standardize profile indicators within the analytic sample.
4. Estimate 2-7 class solutions using a simple primary Mplus parameterization first: class-specific means, equal within-class variances, and zero within-class covariances.
5. Consider more flexible variance or covariance structures only if they converge cleanly and replicate the best loglikelihood.
6. For candidate solutions, rerun with substantially increased random starts before interpretation.

## Primary Estimator or Inference Method

- Use MLR for continuous mixture models unless a project-specific reason supports another estimator.
- Use many random starts. A practical sequence is screening with `STARTS = 800 200`, then candidate confirmation with at least `STARTS = 5000 1000`.

## Required Diagnostics

- Normal model termination.
- Best loglikelihood replication.
- Entropy and average posterior probabilities.
- Smallest class size and percentage.
- Class-specific indicator means in standardized and raw units.
- Warnings about local maxima, nonpositive definite matrices, nonreplicated likelihoods, or boundary estimates.

## Sensitivity Analyses

- Compare adjacent class solutions around the retained solution.
- Do not retain a solution solely because BIC is lowest if it is not replicated, produces very small classes, or lacks substantive interpretability.
- Treat unstable class-specific variance or covariance models as sensitivity attempts, not primary evidence.

## External Variables, Clustering, and Multiple Testing

- Use automatic R3STEP for prespecified antecedent or risk-background predictors of class membership. Include demographic covariates in the R3STEP auxiliary block when the substantive question requires adjusted class-membership comparisons, and report the chosen reference class.
- Use BCH for continuous distal outcomes when class-formation uncertainty should be preserved. Treat BCH means/tests as the primary distal-outcome comparison; covariate-adjusted modal-class models should be clearly labeled as diagnostics or sensitivity analyses unless a manual BCH model is explicitly implemented.
- With `TYPE = COMPLEX MIXTURE`, Mplus does not support automatic `DCATEGORICAL`/`DCONTINUOUS` auxiliary tests. If categorical distal variables require cluster-robust inference, document the failed/incompatible Mplus run and use a clearly labeled manual or R-based cluster-robust alternative.
- Predefine FDR families before interpretation. Separate conceptually distinct families, such as psychological distress outcomes and lifestyle outcomes. Do not include a single prespecified background-risk predictor in distal-outcome FDR families unless it is part of a planned multi-test family.

## Table and Figure Format

- Report fit indices for each class number: loglikelihood, free parameters, AIC, BIC, sample-size adjusted BIC, entropy, smallest class size, and loglikelihood replication status.
- Report retained-class indicator means in raw units and standardized units.
- Include AvePP for each retained class.

## Minimum Results to Report

- Exact analytic N and filters.
- Indicator transformations and standardization.
- Mplus parameterization and random starts.
- Fit comparison across class numbers.
- Retained class sizes and percentages.
- Retained class indicator profile table.
- Any nonconvergence or nonreplication problems.

## Supplementary Reporting Artifacts
