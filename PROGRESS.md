# Progress

Updated 9 October 2026. **One public AI-Learning-Hub repository contains all new learning resources.**

## Foundation release

Published in this repository's main branch. This is the initial documentation and foundations release, not the completed 90-day curriculum. Daily automation is not active.

| Deliverable | State |
|---|---|
| Single-repository architecture and curriculum folder map | Published |
| Homepage, start-here and curriculum registry | Published |
| AI engineer roadmap, eleven role routes and portfolio guide | Published |
| AI foundations, revision sheet and GitHub reading guide | Published |
| Diagnostic assignment and separate solutions | Published |
| Existing-project catalog, readiness backlog and authoring template | Published |
| 90-day development plan | Published plan; tasks remain to be implemented |
| Python tutorials PY-001 through PY-010 and student-score project | Published |
| Further subject tutorials and new project implementations | Planned |
| Legacy project repairs or migration | Pending review; not performed |

## Validation

24 files prepared; 72 relative Markdown link targets and curriculum paths checked. All 90 task IDs are sequential. The foundations Python example produced its documented output. Four official reference pages were checked on 1 October 2026. Existing application code was not executed in this release and is not labeled runnable.

## Release evidence

See the [main-branch history](https://github.com/rajeshvar-gupt/AI-Learning-Hub/commits/main/) for the initial foundation commit. Existing repositories remain unchanged. No private notebooks, credentials, resumes or face images were imported.

## Session Day 2 · 2 October 2026

Published PY-001 and PY-002 on main through [PR #1](https://github.com/rajeshvar-gupt/AI-Learning-Hub/pull/1), merged on 2 October 2026 ([merge commit](https://github.com/rajeshvar-gupt/AI-Learning-Hub/commit/f8ab74223891877c2444102284dabe6b4fb58fc7)). Original calendar D002 was already covered by the foundation release. This session follows the recorded next action and advances D008 / introductory D009 without claiming the entire Python module is complete.

Added setup/run instructions, variables/types lesson, a runnable fixed-input profile example, a revision sheet, five assignment questions and separate solutions. No third-party dependencies or keys required. Homepage, curriculum map, registry and plan updated.

Validation: Python 3.12.14 example output, assignment solution output, 45-minute and zero-day variants, and internal links checked. The merged PR above records the lesson changes. Daily automation remains inactive.

Added the next requested unit: input conversion, comparisons and conditions, with an interactive goal checker and separate practice/solutions. Tested valid, boundary, zero, negative, blank, decimal and nonnumeric input.

## Session Day 3 · 3 October 2026

Published PY-003 on main through [PR #2](https://github.com/rajeshvar-gupt/AI-Learning-Hub/pull/2), merged on 3 October 2026 ([merge commit](https://github.com/rajeshvar-gupt/AI-Learning-Hub/commit/9b7352118dd56ef09208add57e5686f220f1be43)). Adds for/range, while, break/continue, a repeated-input study log, separate practice/solutions and a revision sheet. Navigation and the curriculum registry include the new unit. This advances loop prerequisites for D010; the full functions-based score CLI remains planned.

Validation covers documented snippets, accumulation, immediate quit, zero, invalid text, decimals, negatives, whitespace/case in the quit command, the positive-only assignment variant, and internal links. Daily automation remains inactive.

## Session Day 4 · 7 October 2026

Published PY-004 and PROJ-PY-001 through [PR #3](https://github.com/rajeshvar-gupt/AI-Learning-Hub/pull/3), merged on 8 October 2026 ([merge commit](https://github.com/rajeshvar-gupt/AI-Learning-Hub/commit/1d12e803f6583d515f95aeb313cf8a51d3e3a8f9)). Teaches functions, arguments/defaults, return versus print, local variables and the lists needed for the student-score CLI. The project validates whole-number marks from 0 to 100, handles empty input and EOF, and reports count, total, mean, minimum and maximum.

Includes separate questions/solutions, revision notes, project instructions and automated checks. Validation covers invalid inputs, range boundaries, empty and zero-only data, rounding, calculation side effects, repeated input, EOF and safe importing, plus executable teaching snippets and relative links. All eight tests, six teaching snippets and the documented sample report passed on Python 3.12.14; 65 relative links and curriculum paths were checked. This implements the D010 score-CLI scope; it does not complete all remaining D009 collections topics or D011 file handling. Daily automation remains inactive.

## Session Day 5 · 7 October 2026

Published PY-005 through [PR #4](https://github.com/rajeshvar-gupt/AI-Learning-Hub/pull/4), retargeted to main after PR #3 merged and merged on 8 October 2026 ([merge commit](https://github.com/rajeshvar-gupt/AI-Learning-Hub/commit/c611cab75822630c652ee541d4106286f33bf722)). This dependent contribution adds text-file save/load commands to the same score project, a file-handling lesson, six exercises with solutions and revision notes. It is available on main.

Saves refuse existing targets and validate input before creating files. Loads reject invalid records with line numbers. Empty, missing, malformed and non-UTF-8 files have explicit behavior. Tests use temporary files; permission failure is simulated. Validation: all 19 project tests (11 file tests plus 8 existing tests), both file lesson snippets, 50 relative links and curriculum paths passed on Python 3.12.14. This advances D011 file handling and module reuse; classes remain planned. Daily automation remains inactive.

## Session Day 6 · 9 October 2026

Published PY-006 through [PR #5](https://github.com/rajeshvar-gupt/AI-Learning-Hub/pull/5), merged on 9 October 2026 ([merge commit](https://github.com/rajeshvar-gupt/AI-Learning-Hub/commit/e06309bd0a635551d3b242ba5e595a2680229360)). Covers lists, tuples, dictionaries and sets, indexing/slicing, shallow copying, nested mutability, membership, hashability and comprehensions. Includes a fixed-data enrollment example, eight exercises with separate solutions and a revision sheet. Validation on Python 3.12.14: 11 teaching snippets, exact example output, empty/duplicate grouping, input preservation and independent course lists, plus collection error checks passed. Checked 44 relative links and curriculum paths. This expands D009 collections coverage. Daily automation remains inactive.

## Session Day 7 · 9 October 2026

Published PY-007 through [PR #6](https://github.com/rajeshvar-gupt/AI-Learning-Hub/pull/6), merged on 9 October 2026 ([merge commit](https://github.com/rajeshvar-gupt/AI-Learning-Hub/commit/545a847167522d104c7d351e967a063d93d9168c)). Covers classes, instances, __init__, self, attributes, methods, independent mutable state and internal naming conventions. Includes a learner-record example, eight exercises with separate solutions, revision notes and automated tests. Validation: all eight tests, two lesson snippets and the combined assignment solution passed; 47 relative links and curriculum paths were checked. It advances the basic-classes portion of D011; inheritance and other advanced OOP topics remain planned. Daily automation remains inactive.

## Sessions Day 8–10 · 9 October 2026

Published PY-008, PY-009 and PY-010 together through [PR #7](https://github.com/rajeshvar-gupt/AI-Learning-Hub/pull/7), merged on 9 October 2026 ([merge commit](https://github.com/rajeshvar-gupt/AI-Learning-Hub/commit/347ff453690a3e6fefccf25e91ee56ba0ebb134d)). The bundle covers environments/dependencies, Git workflow, and HTTP/JSON fundamentals, matching D013. Includes an environment checker, offline response validator, automated response tests and five exercises with separate solutions for each unit. Validation on Linux with Python 3.12.14 and Git 2.51.1: fresh venv creation, interpreter checker and pip inspection passed; 8 existing learner tests and 6 response tests passed inside that environment. Local Git branch/stage/diff/unstage/commit checks, the JSON snippet and exact demo output passed. Checked 62 relative links and curriculum paths. Windows commands were documented but not executed; remote GitHub clone/push and real HTTP traffic were not tested. Official Python, pip, Git and MDN references checked on 9 October 2026. No new GitHub repository or external API account is required. Daily automation remains inactive.

## Next session

The core learning path through machine learning is published. Work through the exercises and capstone in [THROUGH-ML.md](THROUGH-ML.md). Deep learning is the next planned subject; begin it when requested. Track legacy repairs separately and keep all learning material in this repository.

[Home](README.md)

## 2026-10-09 · Combined path through core ML

Requested: complete remaining content through machine learning in the existing hub.

Published: PY-011, MATH-001–003, STAT-001–002, DATA-001–003 and ML-001–007; separate exercise/solution sets for every lesson; five offline projects; a sales notebook wrapper; revision/interview sheet; model-card template; pinned environment; and validation evidence. See [THROUGH-ML.md](THROUGH-ML.md) and [VALIDATION-ML.md](VALIDATION-ML.md).

This entry records content implementation, not learner mastery. Existing published resources retain their status. All 21 new registry entries are published following the user's instruction to complete the release. Deep learning onward is still planned. Legacy project repairs and original roadmap dates remain separate. The daily automation remains inactive.

Publication: [PR #8](https://github.com/rajeshvar-gupt/AI-Learning-Hub/pull/8) merged on 2026-10-09 at commit `dc46a269e1828c1fa36ea3d51ad67bb6ade59809`. The user requested completion after the review-ready release was presented. The previously validated code is unchanged: 50 tests passed. No hosted CI checks were configured on this PR.

Next session: support the published exercises or continue into deep learning when requested. Do not create another learning repository.

## 2026-10-09 · Deep learning extension

Prepared DL-001–005, separate assignments/solutions, revision sheet, primary references and a NumPy digits network with two hidden layers. See [module](subjects/deep-learning/README.md) and [validation](VALIDATION-DL.md). New resources remain prepared pending review. This implements dense-network foundations; later architecture specializations remain planned. The daily automation remains inactive.
