# Local execution and deployment handoff

## Iris API

From the repository root after installing requirements-labs.txt:

```bash
python -m ai_hub.iris_api train
python -m ai_hub.iris_api serve --host 127.0.0.1 --port 8000
```

In a second terminal:

```bash
curl http://127.0.0.1:8000/health
curl -H 'Content-Type: application/json' -d '{"samples":[[5.1,3.5,1.4,0.2]]}' http://127.0.0.1:8000/predict
```

POST returns labels and three-class probabilities. Features are sepal length, sepal width, petal length and petal width in centimeters. Stop with Ctrl+C. The unit suite starts an ephemeral localhost server and tests actual HTTP requests, malformed JSON, invalid values, missing routes and size limits.

The standard-library server is educational localhost code. It is not a public production server: no TLS/authentication, slow-client limits or deployment access policy is implemented. A future hosted service needs an appropriate serving stack and these controls.

## Container recipe — hosted validation prepared

```bash
docker build -t ai-learning-hub:review .
docker run --rm -p 127.0.0.1:8000:8000 ai-learning-hub:review
```

Docker is unavailable locally. The follow-up's hosted Ubuntu CI built and started the image and verified localhost health/prediction/error behavior; see VALIDATION-CLOSURE.md for the exact run. This follow-up awaits review/merge. The recipe trains a small model at build time and serves as a non-root user. Do not add secrets to the image. No Render/Neon resources or live URL were created, and no free-tier or cost guarantee is made. Local machine resource use still applies.

## Optional Gemini live call — not executed

Set GEMINI_API_KEY and GEMINI_MODEL in your shell using values from your authorized provider account. Do not commit them or paste them into lesson files. Review current account access, data policies, prices and quota before opting in.

```bash
python -m ai_hub.demo assistant --live
```

The default command without --live uses a fixture. The REST adapter is covered by injected-transport tests; live connectivity, model availability and answer quality remain unverified. No model ID or price is invented by the course. The weather adapter similarly uses OPENWEATHER_API_KEY only for a separately authorized live exercise; current observations are not an ML forecast.

## Rollback exercise

Keep the previous trusted model JSON and matching schema/preprocessing version. Train a candidate into a different path with --model, run tests, serve that path on a different localhost port and compare fixed requests. To roll back, stop the candidate and restart the prior compatible artifact. Do not overwrite or delete the only copy of a known-good artifact. The procedure is a teaching exercise, not evidence of an existing deployed service.

## CI evidence

The workflow definition runs scripts/run_checks.py on Python 3.12. Local command execution is recorded in VALIDATION-REMAINING.md. A workflow file is not a hosted CI pass; inspect actual GitHub run results after pushing.

Hosted CI evidence: [successful fresh-install/check run](https://github.com/rajeshvar-gupt/AI-Learning-Hub/actions/runs/40418645281) on source commit `ceef28d8aa3f7d323e27c2a3427c4b5546a4a00f`. It does not validate Docker or a public deployment.

Run the same bounded container check on an authorized Docker host with `python scripts/docker_smoke.py`. It creates one temporary container and stops that exact ID afterward. It does not deploy a public service.
