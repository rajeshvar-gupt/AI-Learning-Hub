"""Two-hidden-layer neural network; manual gradients and offline digits data."""
import json
from pathlib import Path
import numpy as np
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split


def initialize(widths=(64, 32, 16, 10), seed=42):
    if len(widths) < 2 or any(not isinstance(w, int) or isinstance(w, bool) or w < 1 for w in widths):
        raise ValueError("positive integer layer widths required")
    rng = np.random.default_rng(seed)
    return [(rng.normal(size=(a, b))*np.sqrt(2/a), np.zeros(b)) for a, b in zip(widths, widths[1:])]


def forward(X, params):
    X = np.asarray(X, dtype=float)
    if X.ndim != 2 or not len(X) or not np.isfinite(X).all():
        raise ValueError("nonempty finite feature matrix required")
    activations = [X]
    for i, (W, b) in enumerate(params):
        z = activations[-1] @ W + b
        activations.append(np.maximum(z, 0) if i < len(params)-1 else z)
    return activations


def loss_grad(X, y, params):
    a = forward(X, params)
    y = np.asarray(y)
    logits = a[-1]
    if y.shape != (len(X),) or not np.issubdtype(y.dtype, np.integer) or np.any(y < 0) or np.any(y >= logits.shape[1]):
        raise ValueError("one integer class index per sample required")
    shifted = logits - logits.max(axis=1, keepdims=True)
    logp = shifted - np.log(np.exp(shifted).sum(axis=1, keepdims=True))
    loss = -logp[np.arange(len(y)), y].mean()
    delta = np.exp(logp)
    delta[np.arange(len(y)), y] -= 1
    delta /= len(y)
    grads = [None]*len(params)
    for i in reversed(range(len(params))):
        grads[i] = (a[i].T @ delta, delta.sum(axis=0))
        if i:
            delta = (delta @ params[i][0].T) * (a[i] > 0)
    return float(loss), grads


def fit(X, y, X_valid, y_valid, epochs=40, batch_size=64, rate=.08, seed=42):
    if any(isinstance(v, bool) or not isinstance(v, int) or v < 1 for v in [epochs, batch_size]):
        raise ValueError("epochs and batch size must be positive integers")
    if not np.isfinite(rate) or rate <= 0:
        raise ValueError("positive finite learning rate required")
    params = initialize((X.shape[1], 32, 16, 10), seed)
    loss_grad(X, y, params); loss_grad(X_valid, y_valid, params)
    rng = np.random.default_rng(seed)
    history, best_loss, best, best_epoch = [], np.inf, None, None
    for epoch in range(1, epochs+1):
        order = rng.permutation(len(X))
        for start in range(0, len(X), batch_size):
            idx = order[start:start+batch_size]
            _, grads = loss_grad(X[idx], y[idx], params)
            for (W, b), (dW, db) in zip(params, grads):
                W -= rate*dW; b -= rate*db
        train_loss, _ = loss_grad(X, y, params)
        valid_loss, _ = loss_grad(X_valid, y_valid, params)
        if not np.isfinite([train_loss, valid_loss]).all():
            raise ValueError("training diverged")
        history.append(dict(epoch=epoch, train_loss=train_loss, validation_loss=valid_loss))
        if valid_loss < best_loss:
            best_loss, best_epoch = valid_loss, epoch
            best = [(W.copy(), b.copy()) for W, b in params]
    return best, history, best_epoch


def split_data():
    data = load_digits()
    ids = np.arange(len(data.target))
    remaining, test = train_test_split(ids, test_size=.2, stratify=data.target, random_state=42)
    train, valid = train_test_split(remaining, test_size=.25, stratify=data.target[remaining], random_state=42)
    return data.data.astype(float)/16, data.target, train, valid, test


def main():
    X, y, train, valid, test = split_data()
    params, history, best_epoch = fit(X[train], y[train], X[valid], y[valid])
    pred = forward(X[test], params)[-1].argmax(axis=1)
    majority = np.bincount(y[train]).argmax()
    baseline = np.full(len(test), majority)
    def scores(p):
        return dict(accuracy=float(accuracy_score(y[test], p)), macro_f1=float(f1_score(y[test], p, average="macro", zero_division=0)))
    report = dict(seed=42, widths=[64,32,16,10], parameters=2778,
                  split_sizes=dict(train=len(train), validation=len(valid), test=len(test)),
                  epochs_run=len(history), best_epoch=best_epoch,
                  baseline_test=scores(baseline), network_test=scores(pred),
                  test_confusion_matrix=confusion_matrix(y[test], pred, labels=np.arange(10)).tolist(),
                  history=history)
    output = Path(__file__).parent / "outputs"
    output.mkdir(exist_ok=True)
    (output/"report.json").write_text(json.dumps(report, indent=2, allow_nan=False), encoding="utf-8")
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot([r["epoch"] for r in history], [r["train_loss"] for r in history], label="Train")
    ax.plot([r["epoch"] for r in history], [r["validation_loss"] for r in history], label="Validation")
    ax.set(xlabel="Epoch", ylabel="Mean cross-entropy", title="Digits neural-network learning curves")
    ax.legend();fig.tight_layout();fig.savefig(output/"learning-curves.png", dpi=150);plt.close(fig)
    print(json.dumps({k:v for k,v in report.items() if k not in ["history","test_confusion_matrix"]}, indent=2))


if __name__ == "__main__":
    main()
