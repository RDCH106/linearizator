# -*- coding: utf-8 -*-

from linearizator import linearizator

lin = linearizator.linearizator(x1=6.4, y1=20, x2=16.8, y2=85, unknown="y")
lin.linearize()
print(lin.pretty_equation())
print(lin.calculate(6.4))
lin.inverse()
print(lin.pretty_equation())
print(lin.calculate(20))

