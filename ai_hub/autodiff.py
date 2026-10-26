"""Scalar forward-mode automatic differentiation, not a tensor framework."""
from dataclasses import dataclass


@dataclass
class Dual:
    value: float
    tangent: float = 0.

    def __add__(self, other):
        other=other if isinstance(other,Dual) else Dual(other)
        return Dual(self.value+other.value,self.tangent+other.tangent)
    __radd__=__add__

    def __mul__(self, other):
        other=other if isinstance(other,Dual) else Dual(other)
        return Dual(self.value*other.value,self.tangent*other.value+self.value*other.tangent)
    __rmul__=__mul__


if __name__=='__main__':
    x=Dual(2.,1.);y=(x+-3)*(x+-3)
    print({'loss':y.value,'derivative':y.tangent})
