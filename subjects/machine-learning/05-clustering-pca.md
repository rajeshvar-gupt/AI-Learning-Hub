# ML-005 · Clustering and dimensionality reduction

Prerequisites: ML-004, MATH-001.


Outcome: distinguish cluster structure from ground truth and use PCA as a projection.

K-means alternates assigning points to nearby centroids and updating each centroid to its assigned mean. It needs a chosen k and favors roughly compact Euclidean groups. Scaling affects its geometry. Different initialization can change the solution; fix a seed and use multiple initializations for reproducibility.

Silhouette compares within-cluster tightness with separation from other clusters. It is defined only with at least two clusters and fewer clusters than samples. A high score does not prove the clusters correspond to useful real categories. Select k with stability, interpretation and domain context as well as numerical diagnostics.

DBSCAN can find irregular density-connected groups and mark noise, but its distance radius is scale-sensitive and varying density is difficult. Hierarchical clustering builds nested groups; linkage choice changes the result and large datasets may be expensive.

PCA finds orthogonal directions of high variance after centering. Scaling before PCA changes what high variance means. Explained variance ratio reports how much training variation a component captures, not predictive accuracy or importance to a target. PCA is unsupervised; a low-variance direction can still predict a label well.

The lab fits scaled K-means and PCA on invented blobs, emits diagnostics and writes a two-dimensional projection. It is exploratory fitting on the whole synthetic sample, so silhouette is a descriptive score, not a held-out generalization result. If PCA feeds a supervised model, fit it inside that model's training pipeline.


## Practice

[Questions](../../assignments/ML-005/questions.md) · [Solutions](../../assignments/ML-005/solutions.md) · [Module index](README.md) · [Complete path](../../THROUGH-ML.md)
