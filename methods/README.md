# Methods Notes

These documents are migrated working notes, not a peer-reviewed methods handbook. They do not yet provide a complete, source-verified protocol for every method. Before use, check the primary methodological literature, current software documentation, estimand, data structure, and registered or approved analysis plan.

Status in this initial collection:

| Note | Current role | Required review before treating as a team SOP |
|---|---|---|
| `latent_profile_analysis/mplus_lpa_workflow.md` | LPA planning and reporting checklist | Verify model parameterization, class enumeration, starts, and auxiliary-variable procedures against current Mplus documentation and sources. |
| `latent_profile_analysis/mclust_lpa_robustness.md` | Advanced robustness ideas | Predefine which diagnostics answer the question; validate implementations and cite sources. |
| `latent_profile_analysis/mclust_sensitivity_workflow.md` | mclust comparison checklist | Verify package behavior/version and distinguish Gaussian mixtures from conventional LPA. |
| `network_analysis.md` | Reporting orientation | Not a full estimation SOP; specify network type, estimator, tuning, uncertainty, and comparison tests per study. |
| `regression/README.md` | Internal reporting conventions | Several table and FDR rules are team preferences, not universal requirements. |
| `regression/hierarchical_OLS_interaction_workflow.md` | Draft execution workflow | Confirm inference, multiplicity, diagnostics, and model sequence for each design. |
| `multilevel_models/random_intercept_contextual_workflow.md` | Adapted random-intercept/contextual association note | Verify the estimand, cluster-level exposure, number of clusters, estimation, boundary tests, and uncertainty for the study. |

A method note should say what question it serves, assumptions, required inputs, decisions that must be prespecified, diagnostics, interpretation limits, software versions, and evidence sources. Avoid treating a procedure as mandatory merely because it appears here.
