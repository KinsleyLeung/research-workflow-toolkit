# Random-Intercept and Contextual Association Workflow

> Status: Adapted working note, not a source-verified SOP. Verify estimation, inference, and reporting against the current software documentation and primary methodological literature before using it in an analysis plan.

## When it fits

Consider this workflow when individuals are nested in identifiable clusters and the question concerns between-cluster variation, a cluster-level exposure, or a cross-level interaction. First establish that cluster membership and the exposure are measured and matched correctly. A random intercept is not a substitute for handling selection, unmeasured confounding, or spatial/temporal dependence.

## Inputs and decisions to record

- Outcome scale, unit of analysis, and cluster identifier.
- Number of clusters, cluster-size distribution, and missing cluster assignments.
- Cluster-level exposure source, year, matching rule, and coverage; avoid assigning a group aggregate to individuals without verifying the group mapping.
- Prespecified individual-level covariates, reference groups, sample filters, missing-data strategy, and centering or scaling choices.
- Whether the goal is variance partitioning, contextual association, or a prespecified cross-level interaction.

## Candidate sequence

1. Fit an intercept-only model to describe between-cluster variance and the intraclass correlation where meaningful.
2. Add the prespecified individual-level covariates without changing the analytic sample unexpectedly.
3. Add the cluster-level exposure if it is part of the research question.
4. Add a prespecified cross-level interaction only when the exposure and individual construct support that interpretation.

Keep the random-effects structure and estimation approach aligned across a nested comparison. When comparing models that differ in fixed effects by likelihood-ratio test, use maximum likelihood rather than REML, and verify the test's assumptions. A test of zero random-intercept variance is a boundary problem; do not treat an ordinary chi-square reference as automatically valid. A small number of clusters can make cluster-level effects and their uncertainty especially fragile.

Center continuous variables to make the intercept and interaction interpretable when appropriate, but choose the centering level based on the estimand. Report the original and transformed scales. Do not standardize a cluster-level index automatically when its original units have substantive meaning.

## Minimum reporting and checks

- Analytic N, number of clusters, cluster-size distribution, and sample changes across models.
- Fixed-effect estimates, uncertainty intervals, inferential method, and exact exposure/contrast scale.
- Between-cluster and residual variance estimates; intraclass correlation when appropriate.
- Convergence, influential clusters, residual or model checks relevant to the outcome family, and sensitivity to influential clusters or alternate adjustment sets when justified.
- Any model comparison with its estimation method and reference distribution.

Cluster-level correlations between the exposure and cluster means may be reported as a descriptive ecological check. They do not estimate an individual-level effect and can be unstable with few clusters.

## Interpretation limits

Cluster-level coefficients are contextual associations under the fitted model, not causal effects. A cross-level interaction is model-dependent heterogeneity in association, not proof that the context changes an individual's outcome. Report plausible confounding, measurement error, cross-level selection, and limited generalizability where relevant.
