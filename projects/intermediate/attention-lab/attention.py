"""One-head scaled dot-product attention; demonstration, not a trained model."""
import json
import numpy as np


def attention(Q, K, V, allowed=None):
    Q, K, V = [np.asarray(x, dtype=float) for x in (Q, K, V)]
    if any(x.ndim != 2 or not all(x.shape) or not np.isfinite(x).all() for x in (Q, K, V)):
        raise ValueError('nonempty finite matrices required')
    if Q.shape[1] != K.shape[1] or K.shape[0] != V.shape[0]:
        raise ValueError('query/key dimensions and key/value counts must agree')
    scores = (Q @ K.T)/np.sqrt(Q.shape[1])
    if not np.isfinite(scores).all():
        raise ValueError('attention scores overflowed')
    if allowed is not None:
        allowed = np.asarray(allowed)
        if allowed.dtype != bool or allowed.shape != scores.shape or not allowed.any(axis=1).all():
            raise ValueError('boolean mask must allow at least one key per query')
        scores = np.where(allowed, scores, -np.inf)
    shifted = scores-scores.max(axis=1, keepdims=True)
    weights = np.exp(shifted)
    weights /= weights.sum(axis=1, keepdims=True)
    return weights @ V, weights


if __name__ == '__main__':
    Q = K = np.eye(2)
    V = np.array([[2., 0.], [0., 4.]])
    output, weights = attention(Q, K, V)
    causal_output, causal_weights = attention(Q, K, V, allowed=np.tril(np.ones((2,2), dtype=bool)))
    print(json.dumps(dict(weights=weights.tolist(), output=output.tolist(),
                         causal_weights=causal_weights.tolist(), causal_output=causal_output.tolist()), indent=2))
