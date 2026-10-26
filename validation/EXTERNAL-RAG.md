# External retrieval evaluation protocol

Run from the repository root after installing requirements-labs.txt:

```bash
python -m ai_hub.evaluate_rag
```

This command downloads approximately 4.9 MB of public data on the first run. It uses SQuAD 1.1 development data from [the official repository](https://github.com/rajpurkar/SQuAD-explorer), pinned to commit `eee5fdbf62f8613a7812b03419e6b29617b74fd1`, blob `e9a3f913ad1468ebe105b891334ca7b0bc0e2510`. Bytes must match that Git blob; the report also records SHA-256. A cached modified file is rejected rather than silently reused.

Attribution: Stanford Question Answering Dataset, Pranav Rajpurkar and collaborators, based on crowdworker questions and Wikipedia passages. The [official dataset site](https://rajpurkar.github.io/SQuAD-explorer/) distributes the dataset under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The repository's software MIT license is not substituted for the dataset license. Dataset text/questions remain in ignored runtime outputs; the committed summary contains aggregate metrics and provenance only.

Frozen selection: first 20 articles, first two paragraphs each, first two questions per paragraph. Fixed existing retrieval settings: default TF-IDF, 18-word chunks, overlap three and no question-driven tuning. Search returns up to five chunks; rank/recall refer to the first chunk whose document ID matches the labeled passage. A keyword-overlap comparator uses the same chunks. No labeled questions fit vectorizer statistics; the corpus alone fits the index.

There are 80 questions in the observed selection. It is an independently labeled, small encyclopedia QA subset, not a hidden SQuAD test submission, broad retrieval benchmark or course-support evaluation. It does not measure generated-answer quality. The explicit first-result protocol and all failures remain reproducible; no cherry-picked best run is reported.
