# PY-009 · Git workflow in one repository

Prerequisite: [PY-008](08-environments-and-dependencies.md). Goal: inspect, branch, stage, commit and review a small change in this hub.

Git tracks local history. GitHub hosts shared repositories and pull requests. A local commit is not a push; a push is not a merge.

## Open the existing hub

Use your existing clone. If you have none:

```bash
git clone https://github.com/rajeshvar-gupt/AI-Learning-Hub.git
cd AI-Learning-Hub
```

This creates a local copy, not another GitHub learning repository. Use Git with switch support; check git --version.

## Inspect, then branch

```bash
git status
git remote -v
git branch --show-current
git diff
```

status includes untracked files. Ordinary diff shows unstaged tracked edits, not untracked contents. Preserve unfinished work before switching branches.

With a clean working tree:

```bash
git switch main
git pull --ff-only
git switch -c docs/practice-setup-note
```

pull updates from the upstream only if a fast-forward is possible. If it fails, inspect the histories instead of forcing an update.

## Make one reviewed change

Use an editor to create notes/setup-practice.md:

```text
# Setup practice
I ran the learner-record example in a virtual environment.
```

Only claim the run after doing it. Then:

```bash
git status
git add notes/setup-practice.md
git diff --staged
git commit -m "docs: record environment practice"
git log -1 --oneline
```

add stages the current file contents. Later edits need another add to join the commit. A commit records staged changes, not every file in the folder. If identity is missing, configure repository-local user.name and user.email with your own chosen commit identity.

Unstage without deleting edits using git restore --staged notes/setup-practice.md. Plain git restore can discard working-tree changes; do not substitute it.

## Ignore generated files

A .gitignore can contain:

```text
.venv/
__pycache__/
*.pyc
.env
```

Ignores affect untracked files; they do not remove tracked content or erase history. Review staged changes and exclude credentials and real learner records.

## Share intentionally

If you have write access and intend to publish your practice change:

```bash
git push -u origin docs/practice-setup-note
```

Open a PR against main in AI-Learning-Hub. Describe the change and checks, and follow CONTRIBUTING.md. Authentication is separate from local history; never put a password in a command or source file. The local lab validation does not test your GitHub credentials or remote push.

[Questions](../../../assignments/PY-009/questions.md) · [Solutions](../../../assignments/PY-009/solutions.md) · [Next: HTTP/JSON](10-http-and-json.md)

References, checked 9 October 2026: [Git project — switch](https://git-scm.com/docs/git-switch); [Git project — add](https://git-scm.com/docs/git-add).

Validation: Git 2.51.1 local branch, staging, diff, unstage and commit checks passed in a temporary repository. Remote clone/pull/push were not exercised by the lab.
