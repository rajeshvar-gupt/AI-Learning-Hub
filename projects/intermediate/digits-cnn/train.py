"""Train a small NumPy CNN with explicit kernel gradients on bundled digits."""
import json
from pathlib import Path
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split


def initialize(seed=42):
    rng = np.random.default_rng(seed)
    return dict(K=rng.normal(size=(4, 3, 3))*np.sqrt(2/9),
                b=np.zeros(4), W=rng.normal(size=(144, 10))*np.sqrt(2/144),
                c=np.zeros(10))


def forward(X, p):
    X = np.asarray(X, dtype=float)
    if X.ndim != 3 or X.shape[1:] != (8, 8) or not len(X) or not np.isfinite(X).all():
        raise ValueError("nonempty finite batch of 8x8 grayscale images required")
    windows = sliding_window_view(X, (3, 3), axis=(1, 2))
    # Cross-correlation, as commonly used in CNN layers; kernels are not flipped.
    z = np.einsum('nijab,fab->nijf', windows, p['K']) + p['b']
    features = np.maximum(z, 0).reshape(len(X), -1)
    logits = features @ p['W'] + p['c']
    return logits, (windows, z, features)


def loss_grad(X, y, p):
    logits, (windows, z, features) = forward(X, p)
    y = np.asarray(y)
    if y.shape != (len(X),) or not np.issubdtype(y.dtype, np.integer) or np.any(y < 0) or np.any(y >= 10):
        raise ValueError("one integer label in 0..9 per image required")
    shifted = logits - logits.max(axis=1, keepdims=True)
    logp = shifted - np.log(np.exp(shifted).sum(axis=1, keepdims=True))
    loss = -logp[np.arange(len(y)), y].mean()
    delta = np.exp(logp)
    delta[np.arange(len(y)), y] -= 1
    delta /= len(y)
    dz = (delta @ p['W'].T).reshape(z.shape) * (z > 0)
    grads = dict(W=features.T @ delta, c=delta.sum(axis=0),
                 K=np.einsum('nijab,nijf->fab', windows, dz),
                 b=dz.sum(axis=(0, 1, 2)))
    return float(loss), grads


def split_data():
    data = load_digits()
    ids = np.arange(len(data.target))
    remaining, test = train_test_split(ids, test_size=.2, stratify=data.target, random_state=42)
    train, valid = train_test_split(remaining, test_size=.25, stratify=data.target[remaining], random_state=42)
    return data.images.astype(float)/16, data.target, train, valid, test


def fit(X, y, X_valid, y_valid, epochs=25, batch_size=64, rate=.08):
    if any(isinstance(v, bool) or not isinstance(v, int) or v < 1 for v in [epochs, batch_size]):
        raise ValueError("epochs and batch size must be positive integers")
    if not np.isfinite(rate) or rate <= 0:
        raise ValueError("positive finite learning rate required")
    p = initialize()
    loss_grad(X, y, p); loss_grad(X_valid, y_valid, p)
    rng = np.random.default_rng(42)
    history, best_loss, best, best_epoch = [], np.inf, None, None
    for epoch in range(1, epochs+1):
        order = rng.permutation(len(X))
        for start in range(0, len(X), batch_size):
            idx = order[start:start+batch_size]
            _, grads = loss_grad(X[idx], y[idx], p)
            for key in p:
                p[key] -= rate*grads[key]
        train_loss, _ = loss_grad(X, y, p)
        valid_loss, _ = loss_grad(X_valid, y_valid, p)
        if not np.isfinite([train_loss, valid_loss]).all():
            raise ValueError("training diverged")
        history.append(dict(epoch=epoch, train_loss=train_loss, validation_loss=valid_loss))
        if valid_loss < best_loss:
            best_loss, best_epoch = valid_loss, epoch
            best = {key: value.copy() for key, value in p.items()}
    return best, history, best_epoch


def main():
    X, y, train, valid, test = split_data()
    p, history, best_epoch = fit(X[train], y[train], X[valid], y[valid])
    pred = forward(X[test], p)[0].argmax(axis=1)
    baseline = np.full(len(test), np.bincount(y[train]).argmax())
    def metrics(labels):
        return dict(accuracy=float(accuracy_score(y[test], labels)),
                    macro_f1=float(f1_score(y[test], labels, average='macro', zero_division=0)))
    report = dict(seed=42, architecture='3x3 valid convolution, 4 channels, ReLU, flatten, 10 logits',
                  parameters=sum(v.size for v in p.values()),
                  split_sizes=dict(train=len(train), validation=len(valid), test=len(test)),
                  epochs_run=len(history), best_epoch=best_epoch,
                  baseline_test=metrics(baseline), cnn_test=metrics(pred),
                  label_order=list(range(10)),
                  test_confusion_matrix=confusion_matrix(y[test], pred, labels=range(10)).tolist(),
                  history=history)
    output = Path(__file__).parent/'outputs'
    output.mkdir(exist_ok=True)
    (output/'report.json').write_text(json.dumps(report, indent=2, allow_nan=False), encoding='utf-8')
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    for key, name in [('train_loss', 'Train'), ('validation_loss', 'Validation')]:
        axes[0].plot([r['epoch'] for r in history], [r[key] for r in history], label=name)
    axes[0].set(xlabel='Epoch', ylabel='Mean cross-entropy', title='CNN learning curves')
    axes[0].legend()
    axes[1].imshow(np.concatenate(list(p['K']), axis=1), cmap='coolwarm')
    axes[1].set(title='Four learned 3x3 kernels', xticks=[], yticks=[])
    fig.tight_layout(); fig.savefig(output/'training.png', dpi=150); plt.close(fig)
    print(json.dumps({k:v for k,v in report.items() if k not in ['history','test_confusion_matrix']}, indent=2))


if __name__ == '__main__':
    main()
