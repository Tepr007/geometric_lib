import math
import unittest

import circle
import rectangle
import square
import triangle


class CircleTests(unittest.TestCase):
    def test_area(self):
        cases = ((0, 0), (2, 4 * math.pi), (1.5, 2.25 * math.pi))
        for radius, expected in cases:
            with self.subTest(radius=radius):
                self.assertAlmostEqual(circle.area(radius), expected)

    def test_perimeter(self):
        cases = ((0, 0), (2, 4 * math.pi), (1.5, 3 * math.pi))
        for radius, expected in cases:
            with self.subTest(radius=radius):
                self.assertAlmostEqual(circle.perimeter(radius), expected)


class SquareTests(unittest.TestCase):
    def test_area(self):
        cases = ((0, 0), (5, 25), (1.5, 2.25))
        for side, expected in cases:
            with self.subTest(side=side):
                self.assertAlmostEqual(square.area(side), expected)

    def test_perimeter(self):
        cases = ((0, 0), (5, 20), (1.5, 6))
        for side, expected in cases:
            with self.subTest(side=side):
                self.assertAlmostEqual(square.perimeter(side), expected)


class RectangleTests(unittest.TestCase):
    def test_area(self):
        cases = ((5, 3, 15), (0, 3, 0), (1.5, 2, 3))
        for width, height, expected in cases:
            with self.subTest(width=width, height=height):
                self.assertAlmostEqual(rectangle.area(width, height), expected)

    def test_perimeter(self):
        cases = ((5, 3, 16), (0, 3, 6), (1.5, 2, 7))
        for width, height, expected in cases:
            with self.subTest(width=width, height=height):
                self.assertAlmostEqual(
                    rectangle.perimeter(width, height), expected
                )


class TriangleTests(unittest.TestCase):
    def test_area(self):
        cases = ((5, 3, 7.5), (0, 3, 0), (1.5, 2, 1.5))
        for base, height, expected in cases:
            with self.subTest(base=base, height=height):
                self.assertAlmostEqual(triangle.area(base, height), expected)

    def test_perimeter(self):
        cases = ((3, 4, 5, 12), (0, 0, 0, 0), (1.5, 2, 2.5, 6))
        for side_a, side_b, side_c, expected in cases:
            with self.subTest(sides=(side_a, side_b, side_c)):
                self.assertAlmostEqual(
                    triangle.perimeter(side_a, side_b, side_c), expected
                )


class SecurityInputTests(unittest.TestCase):
    def test_expression_strings_are_rejected(self):
        expression = "1 + 1"
        calls = (
            ("circle.area", circle.area, (expression,)),
            ("circle.perimeter", circle.perimeter, (expression,)),
            ("square.area", square.area, (expression,)),
            ("square.perimeter", square.perimeter, (expression,)),
            ("rectangle.area", rectangle.area, (expression, 3)),
            ("rectangle.perimeter", rectangle.perimeter, (expression, 3)),
            ("triangle.area", triangle.area, (expression, 3)),
            ("triangle.perimeter", triangle.perimeter, (expression, 2, 3)),
        )
        for name, function, args in calls:
            with self.subTest(function=name):
                with self.assertRaises(TypeError):
                    function(*args)

        
