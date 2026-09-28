# Network Analysis

> Status: Internal working note migrated from a local methods library. This is an orientation and reporting checklist, not a complete estimation protocol. Verify model choice, tuning, uncertainty, software behavior, and citations for each study before use.

Use this note when an article includes psychological or behavioral network analysis. Keep article-specific code, figures, and results in the article folder.

## Core Outputs

For condition-association networks, report the outputs needed to interpret both structure and robustness:

1. Edge weights.
2. Centrality indices, when theoretically useful.
3. Stability or accuracy diagnostics.
4. Node predictability, only when it is meaningful for the network type.

## Predictability by Network Type

| Network type | Is predictability appropriate? | Meaning |
|---|---|---|
| GGM / EBICglasso | Appropriate | Proportion of a node's variance explained by adjacent or remaining nodes, similar to R². |
| MGM | Appropriate | Continuous nodes use R²; categorical nodes use classification accuracy or normalized accuracy. |
| Ising model | Possible | Binary nodes are usually summarized using classification accuracy. |
| Pure correlation network | Usually not recommended | The network is not a conditional association network, so predictability has weak interpretability. |
| DAG / Bayesian network | Not reported using this logic | Interpretation focuses on directed dependency structure. |
| Temporal network / VAR | Possible, with a different meaning | Usually predictability of a node at the next time point. |
| Cross-lagged network | Possible, with a different meaning | Predictability refers to future nodes rather than cross-sectional local explanation. |

## Reporting Notes

- State the network type before reporting predictability.
- Define the predictability metric in the Methods section.
- Do not imply that high predictability means causality.
- Save full outputs in article `results/all/` and `figures/all/`.
- Save manuscript-ready outputs in article `results/selected/` and `figures/selected/`.
