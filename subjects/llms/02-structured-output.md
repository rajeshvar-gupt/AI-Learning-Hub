# LLM-002 · Structured outputs and bounded provider handling

Prerequisites: LLM-001. Status: published.

Outcome: validate provider output and handle transient failures without infinite loops.

Provider schema configuration can constrain syntax, but application validation must still check types, required fields and citation scope. The adapter rejects incomplete/blocked outputs and malformed JSON. A valid JSON object can still contain false content, so schema checks are not factual verification.

The example makes at most three attempts for selected transient HTTP failures, including 429. Authentication failures and connection timeouts do not loop automatically. Short exponential waits are injectable for tests. Real services should also consider Retry-After, a global time budget and cancellation; these production extensions are not implemented.

Do not print credentials or raw provider errors containing request URLs. The Gemini key is sent in a header. The default demonstration uses MockLLM and makes no network request. Mock tests cover request shape, retries and invalid responses; live validation is separately outstanding.

[Questions](../../assignments/LLM-002/questions.md) · [Solutions](../../assignments/LLM-002/solutions.md) · [Module](README.md) · [Run guide](../../FINAL-PATH.md)
