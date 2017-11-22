# -*- coding: utf-8 -*-

from linearizator import linearizator

lin = linearizator.Linearizator()
lin.x1 = 8
lin.y1 = 30
lin.x2 = 17
lin.y2 = 84
lin.unknown = "y"
lin.linearize()
print(lin.pretty_equation())
print(lin.calculate(17))
lin.inverse()
print(lin.pretty_equation())
print(lin.calculate(84))