"""Descriptive clustering and PCA on reproducible synthetic blobs."""
import json
from pathlib import Path
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def explore():
    X, _ = make_blobs(n_samples=240, n_features=4, centers=3, cluster_std=1.2, random_state=42)
    Z = StandardScaler().fit_transform(X)
    model = KMeans(n_clusters=3, n_init=10, random_state=42).fit(Z)
    pca = PCA(n_components=2).fit(Z)
    projection = pca.transform(Z)
    report = dict(samples=len(X), clusters=3, seed=42,
                  cluster_sizes=np.bincount(model.labels_, minlength=3).tolist(),
                  silhouette=float(silhouette_score(Z, model.labels_)),
                  explained_variance_ratio=pca.explained_variance_ratio_.tolist(),
                  evaluation="descriptive fit on complete synthetic sample; no generalization claim")
    return report, projection, model.labels_


def main():
    report, projection, labels = explore()
    output = Path(__file__).parent / "outputs"
    output.mkdir(exist_ok=True)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(projection[:, 0], projection[:, 1], c=labels, cmap="viridis", s=20)
    ax.set(title="Synthetic clusters projected with PCA", xlabel="Principal component 1", ylabel="Principal component 2")
    fig.tight_layout()
    fig.savefig(output / "clusters.png", dpi=150)
    plt.close(fig)
    (output / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
