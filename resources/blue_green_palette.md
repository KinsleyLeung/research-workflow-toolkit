# Blue-Green Sequential Palette

An optional five-step palette for an ordered variable or continuous map/heatmap. It was adapted from a project figure note after removing the study-specific use case. It is a visual convention, not a requirement.

| Order | Hex | Suggested role |
|---:|---|---|
| 1 | `#F7F6EF` | Light background or lowest value |
| 2 | `#D7E5D0` | Low value |
| 3 | `#9BC1AD` | Middle value |
| 4 | `#5B91A3` | High value |
| 5 | `#32617D` | Highest value or dark emphasis |

Use a diverging palette when signed deviations around a meaningful zero must be visible. Check legend direction, grayscale legibility, and text contrast at final figure size. Do not use color alone to encode a critical distinction.

```r
blue_green_palette <- c("#F7F6EF", "#D7E5D0", "#9BC1AD", "#5B91A3", "#32617D")
```
