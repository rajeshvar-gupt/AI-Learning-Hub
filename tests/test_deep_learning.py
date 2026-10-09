import importlib.util
from pathlib import Path
import unittest
import numpy as np
p = Path(__file__).resolve().parents[1]/"projects/intermediate/digits-neural-network/train.py"
spec = importlib.util.spec_from_file_location("digits_network", p)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)


class NetworkTests(unittest.TestCase):
    def test_shapes_and_count(self):
        params = m.initialize()
        self.assertEqual(m.forward(np.ones((3,64)), params)[-1].shape, (3,10))
        self.assertEqual(sum(W.size+b.size for W,b in params), 2778)

    def test_gradient_finite_difference(self):
        params = m.initialize((2,3,2), seed=6)
        X = np.array([[.3,.7],[-.4,.2],[.8,-.5]])
        y = np.array([0,1,0])
        _, grads = m.loss_grad(X,y,params)
        eps = 1e-6
        for pair, gradient in zip(params,grads):
            for array, analytic in zip(pair,gradient):
                for idx in np.ndindex(array.shape):
                    old = array[idx]
                    array[idx]=old+eps; plus=m.loss_grad(X,y,params)[0]
                    array[idx]=old-eps; minus=m.loss_grad(X,y,params)[0]
                    array[idx]=old
                    self.assertAlmostEqual((plus-minus)/(2*eps), analytic[idx], places=6)

    def test_extreme_logits_finite(self):
        loss, grads = m.loss_grad(np.array([[1.]]), np.array([1]), [(np.array([[1000.,-1000.]]),np.zeros(2))])
        self.assertAlmostEqual(loss,2000.)
        self.assertTrue(all(np.isfinite(g).all() for pair in grads for g in pair))

    def test_split_disjoint_and_complete(self):
        X,y,a,b,c=m.split_data()
        self.assertFalse(set(a)&set(b) or set(a)&set(c) or set(b)&set(c))
        self.assertEqual(len(set(a)|set(b)|set(c)),len(y))
        self.assertTrue(np.all((X>=0)&(X<=1)))

    def test_learning_and_best_checkpoint(self):
        X,y,a,b,_=m.split_data()
        params,history,epoch=m.fit(X[a],y[a],X[b],y[b],epochs=8)
        self.assertLess(history[-1]['train_loss'],history[0]['train_loss'])
        loss,_=m.loss_grad(X[b],y[b],params)
        self.assertAlmostEqual(loss,min(r['validation_loss'] for r in history))
        self.assertEqual(epoch, min(history,key=lambda r:r['validation_loss'])['epoch'])

    def test_invalid_inputs(self):
        params=m.initialize((2,3,2))
        for X,y in [(np.empty((0,2)),np.array([],dtype=int)),(np.ones((2,2)),np.array([0,2])),(np.ones((2,2)),np.array([.1,.2]))]:
            with self.assertRaises(ValueError):m.loss_grad(X,y,params)
        with self.assertRaises(ValueError):m.initialize((2,0,2))

    def test_reproducible_initialization(self):
        for a,b in zip(m.initialize(),m.initialize()):
            for x,y in zip(a,b):np.testing.assert_array_equal(x,y)


if __name__ == '__main__':unittest.main()
