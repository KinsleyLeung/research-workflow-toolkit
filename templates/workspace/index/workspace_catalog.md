# Workspace Catalog

This is a map of the **receiving workspace**, not a list of folders that must all exist today. Read the root `AGENTS.md` before entering a dataset or article.

| Path | Purpose |
|---|---|
| `README.md` | Human orientation and setup |
| `AGENTS.md` | AI collaborator operating rules and reading boundaries |
| `WORKFLOW.md` | Full research-stage workflow copied from the toolkit |
| `QUALITY_CONTROL.md` | Review gates copied from the toolkit |
| `projects/<DATASET>/` | Dataset-specific governance and article folders; create only after authorization |
| `projects/<DATASET>/articles/<ARTICLE>/` | One article's state, scripts, outputs, and manuscript |
| `methods_library/` | Verified or qualified methods useful across articles |
| `topic_library/` | Reusable theory, constructs, or literature logic |
| `shared/` | Formatting guidance and optional templates |
| `index/` | Navigation, structure, and stable workspace conventions |
| `handoff.md` | Optional workspace-level task handoff, never stored in `index/` |

## Quick reading map

| Task | Read first | Open only if needed |
|---|---|---|
| Workspace question or setup | Root `AGENTS.md`; `README.md` | `WORKFLOW.md`, this catalog, structure guide, workspace memory |
| New dataset | Root `AGENTS.md`; data-governance agreement | Dataset `README.md` or `AGENTS.md` when present |
| New article or direction | Root and dataset rules; article state when present | Decision history, topic notes |
| Exploratory analysis | Article state, data guide, current scripts | Relevant method note, prior decisions |
| Formal analysis | Locked/current plan; scripts; verified input definitions | Diagnostics and method source |
| Manuscript | Plan; manuscript source; selected outputs | Journal rules, bibliography, approved study or measure sources |
| Revision | Current and submitted versions; reviewer materials | Git diff and selected analysis outputs |
| Handoff | Relevant `handoff.md`; active state and plan | Only files named by the task |
| Git or release audit | Root rules; `.gitignore`; candidate list and diff | Selected file contents after review |

Never open raw data or unrelated article folders just because they are in the workspace.
