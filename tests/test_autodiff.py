import unittest
from ai_hub.autodiff import Dual


class AutodiffTests(unittest.TestCase):
    def test_product_and_quadratic(self):
        x=Dual(2,1);y=(x+-3)*(x+-3)
        self.assertEqual(y.value,1);self.assertEqual(y.tangent,-2)
        z=3*x*x+2*x+1
        self.assertEqual(z.value,17);self.assertEqual(z.tangent,14)
