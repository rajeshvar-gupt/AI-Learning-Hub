import importlib.util
from pathlib import Path
import unittest
import numpy as np

path = Path(__file__).resolve().parents[1]/'projects/intermediate/digits-cnn/train.py'
spec = importlib.util.spec_from_file_location('digits_cnn', path)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)


class CNNTests(unittest.TestCase):
    def test_known_cross_correlation(self):
        p = m.initialize(); p['K'].fill(1); p['b'].fill(0)
        _, (_, z, features) = m.forward(np.ones((2, 8, 8)), p)
        np.testing.assert_allclose(z, 9)
        self.assertEqual(z.shape, (2, 6, 6, 4))
        self.assertEqual(features.shape, (2, 144))
        self.assertEqual(sum(v.size for v in p.values()), 1490)

    def test_all_parameter_gradients(self):
        rng = np.random.default_rng(7)
        X = rng.normal(size=(2, 8, 8)); y = np.array([1, 4]); p = m.initialize(6)
        _, grads = m.loss_grad(X, y, p)
        epsilon = 1e-6
        for key, array in p.items():
            for index in np.ndindex(array.shape):
                value = array[index]
                array[index] = value+epsilon; plus = m.loss_grad(X, y, p)[0]
                array[index] = value-epsilon; minus = m.loss_grad(X, y, p)[0]
                array[index] = value
                self.assertAlmostEqual((plus-minus)/(2*epsilon), grads[key][index], places=6)

    def test_learning_and_checkpoint(self):
        X,y,a,b,_ = m.split_data()
        p,history,epoch = m.fit(X[a],y[a],X[b],y[b],epochs=4)
        self.assertLess(history[-1]['train_loss'], history[0]['train_loss'])
        self.assertAlmostEqual(m.loss_grad(X[b],y[b],p)[0], min(r['validation_loss'] for r in history))
        self.assertEqual(epoch, min(history,key=lambda r:r['validation_loss'])['epoch'])

    def test_splits(self):
        X,y,a,b,c = m.split_data()
        self.assertFalse(set(a)&set(b) or set(a)&set(c) or set(b)&set(c))
        self.assertEqual(len(set(a)|set(b)|set(c)), len(y))
        self.assertTrue(np.all((X>=0)&(X<=1)))

    def test_invalid_inputs(self):
        p = m.initialize()
        for X,y in [(np.ones((2,7,7)),np.array([0,1])), (np.ones((2,8,8)),np.array([0,10])),
                    (np.full((2,8,8),np.nan),np.array([0,1])), (np.ones((2,8,8)),np.array([0.,1.]))]:
            with self.assertRaises(ValueError): m.loss_grad(X,y,p)
        with self.assertRaises(ValueError): m.fit(np.ones((2,8,8)),np.array([0,1]),np.ones((2,8,8)),np.array([0,1]),epochs=0)

    def test_repeatable_initialization(self):
        a,b = m.initialize(),m.initialize()
        for key in a: np.testing.assert_array_equal(a[key],b[key])


if __name__ == '__main__':
    unittest.main()
