# -*- coding: utf-8 -*-

from linearizator import linearizator

# Initialize linearizator object
lin = linearizator.Linearizator(x1=6.4, y1=20, x2=16.8, y2=85, unknown="y")

# Linearize
lin.linearize()

# Show equation of line
print(lin.pretty_equation())

# Calculate the value of a point
print(lin.calculate(6.4))

# Generate inverse linearization
lin.inverse()

# Show equation of line
print(lin.pretty_equation())

# Calculate the value of a point
print(lin.calculate(20))

