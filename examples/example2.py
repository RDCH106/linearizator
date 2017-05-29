# -*- coding: utf-8 -*-

from linearizator import linearizator

lin2 = linearizator.linearizator(x1=8, y1=30, x2=17, y2=84)
lin2.linearize()
print(lin2.pretty_equation())
print(lin2.calculate(17))
lin2.inverse()
print(lin2.pretty_equation())
print(lin2.calculate(84))