import importlib.util
from pathlib import Path
import unittest
import numpy as np

path = Path(__file__).resolve().parents[1]/'projects/intermediate/transformer-mechanics/mechanics.py'
spec=importlib.util.spec_from_file_location('mechanics',path)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)


class TransformerTests(unittest.TestCase):
    def test_positions_at_origin(self):
        pos=m.positions(4,8)
        np.testing.assert_array_equal(pos[0,0::2],0)
        np.testing.assert_array_equal(pos[0,1::2],1)
        self.assertFalse(np.allclose(pos[0],pos[1]))

    def test_layer_norm_rows(self):
        X=np.array([[1.,2.,3.],[4.,8.,12.]])
        normalized=m.layer_norm(X)
        np.testing.assert_allclose(normalized.mean(axis=1),0,atol=1e-12)
        self.assertTrue(np.all(normalized.var(axis=1)<1))
        np.testing.assert_allclose(m.layer_norm(np.ones((2,3))),0)

    def test_multihead_shapes_and_masks(self):
        X=np.random.default_rng(1).normal(size=(4,8))
        out,w=m.multi_head(X,m.parameters(),allowed=np.tril(np.ones((4,4),dtype=bool)))
        self.assertEqual(out.shape,(4,8));self.assertEqual(w.shape,(2,4,4))
        np.testing.assert_allclose(w.sum(axis=-1),1)
        np.testing.assert_allclose(w[:,0,:],[[1,0,0,0],[1,0,0,0]])
        self.assertTrue(np.all(w[:,np.triu_indices(4,1)[0],np.triu_indices(4,1)[1]]==0))

    def test_identity_head_matches_manual_attention(self):
        X=np.eye(2);p={key:np.eye(2) for key in ['Wq','Wk','Wv','Wo']}
        out,w=m.multi_head(X,p,heads=1)
        expected=m.softmax(X @ X.T/np.sqrt(2))
        np.testing.assert_allclose(w[0],expected);np.testing.assert_allclose(out,expected @ X)

    def test_causal_block_ignores_future_tokens(self):
        X=np.random.default_rng(3).normal(size=(4,8));p=m.parameters()
        mask=np.tril(np.ones((4,4),dtype=bool))
        before,_=m.block(X,p,allowed=mask)
        X[3]+=np.arange(8)*10
        after,_=m.block(X,p,allowed=mask)
        np.testing.assert_allclose(before[:3],after[:3],atol=1e-12)

    def test_repeatable_block(self):
        X=m.positions(3,8)
        np.testing.assert_array_equal(m.block(X,m.parameters())[0],m.block(X,m.parameters())[0])

    def test_top_k_and_repeatable_decoding(self):
        token,p=m.decode([2.,1.,0.,-1.],temperature=.7,top_k=2)
        self.assertEqual(token,m.decode([2.,1.,0.,-1.],temperature=.7,top_k=2)[0])
        np.testing.assert_array_equal(p[2:],0);self.assertAlmostEqual(p.sum(),1)
        self.assertIn(token,[0,1])

    def test_top_one_is_greedy(self):
        token,p=m.decode([1.,3.,2.],top_k=1)
        self.assertEqual(token,1);np.testing.assert_array_equal(p,[0,1,0])

    def test_temperature_changes_entropy(self):
        _,cool=m.decode([2.,1.,0.],temperature=.2)
        _,warm=m.decode([2.,1.,0.],temperature=2.)
        self.assertGreater(cool.max(),warm.max())

    def test_invalid_inputs(self):
        for args in [(0,8),(3,7),(True,8)]:
            with self.assertRaises(ValueError):m.positions(*args)
        X=np.ones((3,8));p=m.parameters()
        with self.assertRaises(ValueError):m.multi_head(X,p,heads=3)
        with self.assertRaises(ValueError):m.multi_head(X,p,allowed=np.zeros((3,3),dtype=bool))
        for kwargs in [dict(temperature=0),dict(top_k=5),dict(top_k=True)]:
            with self.assertRaises(ValueError):m.decode([1.,2.,3.],**kwargs)
        with self.assertRaises(ValueError):m.layer_norm(np.full((2,3),np.nan))


if __name__=='__main__':unittest.main()
