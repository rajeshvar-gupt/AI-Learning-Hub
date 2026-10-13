import importlib.util
from pathlib import Path
import unittest
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def load(folder, name):
    spec = importlib.util.spec_from_file_location(folder.replace('-', '_'), ROOT/'projects/intermediate'/folder/name)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


text = load('support-text-classifier', 'train.py')
attn = load('attention-lab', 'attention.py')


class TextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.train, cls.y_train, cls.test, cls.y_test = text.dataset()
        cls.search = text.select_model(cls.train, cls.y_train)
        cls.model = cls.search.best_estimator_

    def test_original_partitions(self):
        self.assertEqual(len(self.train), 36); self.assertEqual(len(self.test), 12)
        self.assertFalse(set(self.train)&set(self.test))
        self.assertEqual(len(set(self.train+self.test)), 48)

    def test_test_only_vocabulary_absent(self):
        vocab = self.model.named_steps['tfidf'].vocabulary_
        self.assertNotIn('dispute', vocab)
        self.assertIn('password', vocab)

    def test_transform_does_not_refit(self):
        vectorizer = self.model.named_steps['tfidf']
        before = vectorizer.vocabulary_.copy(); idf = vectorizer.idf_.copy()
        self.model.predict(['uniquewordfromthefuture'])
        self.assertEqual(before, vectorizer.vocabulary_)
        np.testing.assert_array_equal(idf, vectorizer.idf_)

    def test_oov_routes_to_review(self):
        result = text.route(self.model, ['zzzzunseenword'])[0]
        self.assertEqual(result['route'], 'needs_review'); self.assertEqual(result['known_features'], 0)

    def test_invalid_texts(self):
        for value in [[], [''], ['   '], [None], 'one string']:
            with self.assertRaises(ValueError): text.route(self.model, value)

    def test_invalid_training_labels(self):
        with self.assertRaises(ValueError): text.select_model(['a','b'], ['x'])
        with self.assertRaises(ValueError): text.select_model(['a','b','c'], ['x','x','x'])

    def test_prediction_contract(self):
        pred = self.model.predict(self.test)
        self.assertEqual(pred.shape, (12,)); self.assertTrue(set(pred).issubset(set(self.y_train)))
        self.assertEqual(len(self.search.cv_results_['params']), 4)


class AttentionTests(unittest.TestCase):
    def test_uniform_attention(self):
        out, w = attn.attention(np.zeros((1,2)), np.eye(2), np.array([[2.,0.],[0.,4.]]))
        np.testing.assert_allclose(w, [[.5,.5]]); np.testing.assert_allclose(out, [[1.,2.]])

    def test_causal_mask(self):
        out, w = attn.attention(np.eye(2), np.eye(2), np.eye(2), np.tril(np.ones((2,2),dtype=bool)))
        self.assertEqual(w[0,1], 0); self.assertEqual(w[0,0], 1)
        np.testing.assert_allclose(w.sum(axis=1), 1)

    def test_shift_invariance(self):
        Q = np.ones((1,2)); K=np.eye(2); V=np.eye(2)
        np.testing.assert_allclose(attn.attention(Q,K,V)[1], attn.attention(Q,K+100,V)[1])

    def test_invalid_shapes_and_masks(self):
        Q=K=V=np.eye(2)
        for values in [(np.array([1.,2.]),K,V,None), (Q,np.ones((2,3)),V,None),
                       (Q,K,V,np.zeros((2,2),dtype=bool)), (Q,K,V,np.ones((2,2))),
                       (np.full((2,2),np.nan),K,V,None)]:
            with self.assertRaises(ValueError): attn.attention(*values)


if __name__ == '__main__':
    unittest.main()
