# PY-008 · Environments and reproducible setup

Prerequisite: [PY-007](../01-fundamentals/07-classes-and-objects.md). Goal: identify the interpreter, isolate packages and record reproducible run instructions.

## Why an environment?

Projects can require different package versions. A virtual environment separates installed Python packages; it does not isolate the operating system or make code safe. These hub examples use the standard library and require no third-party packages.

Open a terminal in the cloned hub root and choose a new .venv directory. Do not store source code inside it.

macOS/Linux:

```bash
python3 --version
python3 -m venv .venv
.venv/bin/python subjects/python/examples/environment_check.py
.venv/bin/python -m pip --version
```

Windows PowerShell, with the py launcher installed:

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\python.exe subjects/python/examples/environment_check.py
.\.venv\Scripts\python.exe -m pip --version
```

The [checker](../examples/environment_check.py) reports version, executable, working directory and whether sys.prefix differs from sys.base_prefix. Expect virtual_environment to be true; paths and versions vary. If venv/ensurepip is unavailable, repair your Python installation before continuing.

## Activation and dependencies

Activation is optional because the commands use the executable directly. bash/zsh can use source .venv/bin/activate; PowerShell can use .\.venv\Scripts\Activate.ps1. If activation is blocked, use the direct executable. After activation, python should resolve inside .venv; deactivate restores the prior shell path.

Use python -m pip with the intended interpreter. For a project with a reviewed requirements.txt, python -m pip install -r requirements.txt installs its listed dependencies. Do not run that here: these units need no external packages. Installation generally needs package downloads.

A version pin records a chosen package version. pip freeze lists installed distributions; it is not a dependency solver or a cross-platform lockfile. Review its output before sharing: direct references may contain private locations. Record Python and OS versions, package versions, and run/test commands together.

Recreate environments from instructions; do not copy .venv between computers or commit it. A successful import does not prove correct behavior.

## Reproduce a known example

```bash
.venv/bin/python subjects/python/examples/learner_record.py
.venv/bin/python -m unittest discover -s subjects/python/examples -p 'test_learner_record.py' -v
```

Windows: replace .venv/bin/python with .\.venv\Scripts\python.exe. Compare with [PY-007](../01-fundamentals/07-classes-and-objects.md).

[Questions](../../../assignments/PY-008/questions.md) · [Solutions](../../../assignments/PY-008/solutions.md) · [Next: Git](09-git-workflow.md)

References, checked 9 October 2026: [Python Software Foundation — venv](https://docs.python.org/3/library/venv.html); [pip project — freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/).

Validation: Linux/Python 3.12.14 fresh-venv commands and learner tests passed. Windows instructions were not executed in this environment.
