# Readiness and repair backlog

## Release levels

Cataloged: existence and basic files checked. Reviewed: selected code/docs inspected. Runnable: documented small example executed in a named environment. Evaluated: appropriate baseline, held-out cases and failures reported. Deployment-ready: configuration, tests, health behavior and rollback documented. Production use needs additional context-specific operational evidence.

## Priority work

| Project | Next bounded improvement | Evidence required |
|---|---|---|
| Weather | Use environment-based configuration and reliable request handling; label synthetic ML honestly | Mocked success, missing configuration, invalid city and timeout cases |
| Resume | Document resource setup and fix multipage/empty-text processing | Small synthetic fixtures and extraction tests |
| Book | Implement a small reproducible recommendation baseline after dataset review | Actual code, setup and known-input result |
| Face recognition | Assess dependencies and separate small inference demo from legacy environment | Reproducible setup result, explicit blockers and data/model permissions |
| Iris | Implement training, saved-model inference and API validation | Clean-environment smoke test and behavioral tests |

No repair is marked complete in this first batch. Maintain original attribution. Do not redistribute personal documents, faces or third-party assets merely because an existing repository includes them.

## Project acceptance checklist

Document problem, learning objectives, architecture, stack, dataset, installation, commands, output, code explanation, tests/evaluation, limitations, improvements, interview questions and challenges. Run from the documented directory. Keep secrets out of code. Include meaningful edge cases, not just happy-path screenshots.

[Catalog](catalog.md) · [Home](README.md)
