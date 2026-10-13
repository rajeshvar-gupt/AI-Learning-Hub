# Support-message text classification

Status: prepared for review. Prerequisites: NLP-001–003.

Route original invented messages into billing, access and course categories using a TF-IDF/logistic-regression pipeline. This is an instructional classifier, not an automated support agent or a production recommendation.

## Run

From the repository root, activate the existing environment installed from requirements-ml.txt:

```bash
python projects/intermediate/support-text-classifier/train.py
python -m unittest discover -s tests -p 'test_nlp.py' -v
```

No keys, internet requests or external dataset downloads are needed at runtime. The fixture defines 36 training and 12 test messages, written originally for this repository. They are not real customer or learner records. Fixed partitions are visible for teaching and should not be reused as an independent benchmark after test-driven changes.

Three training folds choose among four unigram/bigram and regularization configurations. Vocabulary and IDF are fitted inside each fold. The selected pipeline is refitted on the training partition and evaluated alongside a training-majority baseline. The script writes outputs/report.json, overwriting its own previous output on rerun. That generated directory is covered by the existing parent ignore rules.

The report contains all candidates, selected parameters, class metrics, confusion counts and individual test predictions. [Observed results](../../../VALIDATION-NLP.md). Unknown words are ignored by the word vocabulary; the route helper sets needs_review for an all-zero vector. A nonzero vector still does not prove that the message has a known intent. Blank strings are rejected.

Practice: explain why the test-only word “dispute” is absent from the learned vocabulary, identify one possible ambiguity, and propose an experiment with new representative training/validation data. No language-model generation, sensitive-document extraction or live message sending occurs.

[Lessons](../../../subjects/nlp/README.md)
