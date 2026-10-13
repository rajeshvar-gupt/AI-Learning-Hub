"""Seeded, untrained transformer forward mechanics and fixed-logit decoding."""
import json
from pathlib import Path
import numpy as np


def positive_integer(value, name):
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(name+' must be a positive integer')


def positions(length, width):
    positive_integer(length, 'length'); positive_integer(width, 'width')
    if width % 2:
        raise ValueError('this positional implementation requires even width')
    pos = np.arange(length)[:, None]
    scales = 10000.**(-np.arange(0, width, 2)/width)
    result = np.empty((length, width))
    result[:, 0::2] = np.sin(pos*scales)
    result[:, 1::2] = np.cos(pos*scales)
    return result


def softmax(logits):
    x = np.asarray(logits, dtype=float)
    if not x.size or not np.isfinite(x).all():
        raise ValueError('finite nonempty logits required')
    shifted = x-x.max(axis=-1, keepdims=True)
    exp = np.exp(shifted)
    return exp/exp.sum(axis=-1, keepdims=True)


def layer_norm(X, epsilon=1e-5):
    X = np.asarray(X, dtype=float)
    if X.ndim != 2 or not all(X.shape) or not np.isfinite(X).all():
        raise ValueError('nonempty finite token matrix required')
    if not np.isfinite(epsilon) or epsilon <= 0:
        raise ValueError('positive finite epsilon required')
    return (X-X.mean(axis=-1, keepdims=True))/np.sqrt(X.var(axis=-1, keepdims=True)+epsilon)


def parameters(width=8, seed=42):
    positive_integer(width, 'width')
    rng = np.random.default_rng(seed)
    def matrix(a, b): return rng.normal(size=(a, b))/np.sqrt(a)
    return dict(Wq=matrix(width,width), Wk=matrix(width,width), Wv=matrix(width,width),
                Wo=matrix(width,width), W1=matrix(width,2*width), b1=np.zeros(2*width),
                W2=matrix(2*width,width), b2=np.zeros(width))


def multi_head(X, p, heads=2, allowed=None):
    X = np.asarray(X, dtype=float)
    if X.ndim != 2 or not all(X.shape) or not np.isfinite(X).all():
        raise ValueError('nonempty finite token matrix required')
    positive_integer(heads, 'heads')
    n, width = X.shape
    if width % heads:
        raise ValueError('width must be divisible by heads')
    depth = width//heads
    Q,K,V = [(X @ p[key]).reshape(n,heads,depth).transpose(1,0,2) for key in ['Wq','Wk','Wv']]
    scores = (Q @ K.transpose(0,2,1))/np.sqrt(depth)
    if not np.isfinite(scores).all():
        raise ValueError('attention scores overflowed')
    if allowed is None:
        allowed = np.ones((n,n), dtype=bool)
    allowed = np.asarray(allowed)
    if allowed.dtype != bool or allowed.shape != (n,n) or not allowed.any(axis=1).all():
        raise ValueError('boolean mask needs one allowed key per query')
    scores = np.where(allowed[None,:,:], scores, -np.inf)
    shifted = scores-scores.max(axis=-1, keepdims=True)
    weights = np.exp(shifted)
    weights /= weights.sum(axis=-1, keepdims=True)
    joined = (weights @ V).transpose(1,0,2).reshape(n,width)
    return joined @ p['Wo'], weights


def block(X, p, heads=2, allowed=None):
    # Pre-normalization, unit gains/zero offsets, no dropout.
    attended, weights = multi_head(layer_norm(X), p, heads, allowed)
    residual = X+attended
    hidden = np.maximum(layer_norm(residual) @ p['W1']+p['b1'], 0)
    return residual+hidden @ p['W2']+p['b2'], weights


def decode(logits, temperature=1., top_k=None, seed=42):
    x = np.asarray(logits, dtype=float)
    if x.ndim != 1 or not len(x) or not np.isfinite(x).all():
        raise ValueError('one finite nonempty logit vector required')
    if not np.isfinite(temperature) or temperature <= 0:
        raise ValueError('positive finite temperature required')
    # Shift before division to reduce overflow for small temperatures.
    with np.errstate(over='ignore'):
        scaled = (x-x.max())/temperature
    if top_k is None:
        top_k = len(x)
    positive_integer(top_k, 'top_k')
    if top_k > len(x):
        raise ValueError('top_k exceeds vocabulary size')
    ranked = np.argsort(-x, kind='stable')[:top_k]
    exp = np.exp(scaled[ranked])
    probabilities = np.zeros(len(x))
    probabilities[ranked] = exp/exp.sum()
    token = int(np.random.default_rng(seed).choice(len(x), p=probabilities))
    return token, probabilities


def main():
    rng = np.random.default_rng(42)
    # IDs supplied directly; no tokenizer or learned embedding training.
    embedding = rng.normal(size=(6,8))*.1
    ids = np.array([1,3,2,5])
    X = embedding[ids]+positions(len(ids),8)
    allowed = np.tril(np.ones((len(ids),len(ids)), dtype=bool))
    output, weights = block(X, parameters(), heads=2, allowed=allowed)
    token, probabilities = decode([2.,1.,0.,-1.], temperature=.7, top_k=2)
    report = dict(status='untrained forward demonstration; no language benchmark',
                  seed=42, input_shape=list(X.shape), output_shape=list(output.shape),
                  attention_shape=list(weights.shape),
                  row_sums=weights.sum(axis=-1).tolist(), first_query_weights=weights[:,0,:].tolist(),
                  block_output=output.tolist(),
                  fixed_logit_decoding=dict(sampled_token=token, probabilities=probabilities.tolist()))
    output_dir = Path(__file__).parent/'outputs'
    output_dir.mkdir(exist_ok=True)
    (output_dir/'report.json').write_text(json.dumps(report, indent=2, allow_nan=False), encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
