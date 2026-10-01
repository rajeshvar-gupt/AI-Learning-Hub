# Single-repository architecture

User decision, 1 October 2026: create **only AI-Learning-Hub**, with all new educational content inside it. This supersedes every earlier four-repository or 24-repository proposal. No sibling learning repository should be created.

| Folder | Owns |
|---|---|
| roadmaps/ | Learning order, prerequisites, role routes and career portfolio guidance |
| notes/ | Concise revision notes and cheat-sheets/ |
| subjects/ | Full tutorials and focused labs, organized by subject as content is added |
| projects/ | All new learning-project implementations and project catalog |
| assignments/ | Questions, starter material and separate solutions |
| interview-preparation/ | Subject and scenario interview collections when authored |
| resources/ | Verified references with dates and access/provenance notes |

README.md is the homepage. CURRICULUM.md defines the complete subject map. ROADMAP.md holds 90 development tasks. PROGRESS.md records actual status. curriculum.json maps stable topic IDs to repository-relative paths.

## Organization rules

Use one canonical location for each lesson/project and relative Markdown links everywhere within the hub. Link related notes, assignments, projects and next topics instead of copying their content. Use numbered kebab-case lesson paths and snake_case Python modules. Do not create empty topic folders to imply completed coverage.

Existing repositories are left intact. Reviewed legacy public projects may be referenced, but new implementations belong here. Do not copy private notebooks, credentials, personal data or third-party assets into the hub without the required authorization and rights review. Existing project history is not silently migrated.

## Development workflow

Read progress and open PRs → select unfinished task → search for duplicates → branch → author → validate → update navigation and progress → open PR → review → publish. Initial repository bootstrap can use a coherent first commit; subsequent substantial changes use PRs. Record actual checks and actual commit URLs.

Use prepared, published, planned and blocked consistently. Prepared means authored locally, not live on GitHub. Daily continuation must use this single repository and must not resurrect the earlier multi-repository design.

[Home](README.md)
