# -*- coding: utf-8 -*-

import unittest
import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from linearizator import linearizator

class TestClass(unittest.TestCase):

    def setUp(self):
        self.linearizator = linearizator.Linearizator(x1=6.4, y1=20, x2=16.8, y2=85, unknown="y")

    def test_constructor(self):
        self.assertIsInstance(self.linearizator, linearizator.Linearizator, "Object is not an instance of linearizator")
        self.assertEqual(6.4, self.linearizator.x1)
        self.assertEqual(20, self.linearizator.y1)
        self.assertEqual(16.8, self.linearizator.x2)
        self.assertEqual(85, self.linearizator.y2)
        self.assertEqual("y", self.linearizator.unknown)
        self.assertIsNone(self.linearizator.equation)

    def test_getters_and_setters(self):
        x1 = 8
        self.linearizator.x1 = x1
        self.assertEqual(x1, self.linearizator.x1)
        y1 = 30
        self.linearizator.y1 = y1
        self.assertEqual(y1, self.linearizator.y1)
        x2 = 17
        self.linearizator.x2 = x2
        self.assertEqual(x2, self.linearizator.x2)
        y2 = 17
        self.linearizator.y2 = y2
        self.assertEqual(y2, self.linearizator.y2)
        unknown = "x"
        self.linearizator.unknown = unknown
        self.assertEqual(unknown, self.linearizator.unknown)
        equation = (-0.5, 2)
        self.linearizator.equation = equation
        self.assertEqual(equation, self.linearizator.equation)


class TestClassMethods(unittest.TestCase):
    def setUp(self):
            self.linearizator = linearizator.Linearizator(x1=6.4, y1=20, x2=16.8, y2=85, unknown="y")

    def test_linearize(self):
        self.linearizator.linearize()
        self.assertEqual((6.25, -20), self.linearizator.equation)
        self.assertEqual("y = 6.25x + (-20.0)", self.linearizator.pretty_equation())

    def test_inverse(self):
        self.linearizator.linearize()
        self.linearizator.inverse()
        self.assertEqual((0.16, 3.2), self.linearizator.equation)
        self.assertEqual("x = 0.16y + (3.2)", self.linearizator.pretty_equation())

    def test_calculate(self):
        self.linearizator.linearize()
        self.assertEqual(20, self.linearizator.calculate(6.4))
        self.assertEqual(85, self.linearizator.calculate(16.8))

if __name__ == '__main__':
    unittest.main(verbosity=2)