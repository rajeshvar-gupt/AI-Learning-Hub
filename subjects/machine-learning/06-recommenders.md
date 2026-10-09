# ML-006 · Content-based book recommendations

Prerequisites: ML-005.


Outcome: implement similarity retrieval and distinguish it from a trained rating predictor.

A content-based recommender compares item descriptions. TF-IDF represents terms with weights that reflect frequency in a document and rarity across the catalog. Cosine similarity compares document-vector direction. Retrieve high-similarity items, exclude the query item and break ties deterministically.

The included catalog contains original invented titles and summaries. It needs no downloaded data or external API. This is an offline retrieval demo: it has no user histories, personalization, rating labels or measured recommendation quality. A zero similarity means no shared weighted terms under this representation, so the demo omits zero-score matches instead of presenting them as meaningful.

Collaborative filtering learns from user-item interactions and can capture taste beyond descriptions, but new users/items create a cold-start problem. Popularity is a useful baseline. For evaluation, hold out interactions by time when simulating future recommendation; avoid training on an interaction you later claim to predict.

Precision@k counts relevant recommendations among k shown items; recall@k compares relevant retrieved items with all relevant held-out items. Ranking metrics such as NDCG reward placing highly relevant items early. Offline interaction logs reflect previous exposure and position bias, so strong offline scores still need careful real-world evaluation.

Run the book lab and explain why a Python query returns a data-analysis title. Then add a description with entirely different vocabulary and inspect the empty-match behavior.


## Practice

[Questions](../../assignments/ML-006/questions.md) · [Solutions](../../assignments/ML-006/solutions.md) · [Module index](README.md) · [Complete path](../../THROUGH-ML.md)
