import math
import unittest

import circle
import rectangle
import square
import triangle


class CircleTests(unittest.TestCase):
    def test_area(self):
        standard_cases = ((1, math.pi), (2, 4 * math.pi), (1.5, 2.25 * math.pi))
        for radius, expected in standard_cases:
            with self.subTest(msg="standard_cases", radius=radius):
                self.assertAlmostEqual(circle.area(radius), expected)

        zero_cases = ((0, 0), (0.0, 0.0))
        for radius, expected in zero_cases:
            with self.subTest(msg="zero_cases", radius=radius):
                self.assertAlmostEqual(circle.area(radius), expected)

        negative_cases = ((-1, math.pi), (-2, 4 * math.pi), (-1.5, 2.25 * math.pi))
        for radius, expected in negative_cases:
            with self.subTest(msg="negative_cases", radius=radius):
                self.assertAlmostEqual(circle.area(radius), expected)

        string_cases = (("0", TypeError), ("2 + 2", TypeError), ("1.5", TypeError))
        for radius, expected in string_cases:
            with self.subTest(msg="string_cases", radius=radius):
                with self.assertRaises(expected):
                    circle.area(radius)

        edge_cases = ((10**100, math.pi * 10**200), (-(10**100), math.pi * 10**200))
        for radius, expected in edge_cases:
            with self.subTest(msg="edge_cases", radius=radius):
                self.assertTrue(math.isclose(circle.area(radius), expected))

    def test_perimeter(self):
        standard_cases = ((0, 0), (2, 4 * math.pi), (1.5, 3 * math.pi))
        for radius, expected in standard_cases:
            with self.subTest(msg="standard_cases", radius=radius):
                self.assertAlmostEqual(circle.perimeter(radius), expected)

        zero_cases = ((0, 0), (0.0, 0.0))
        for radius, expected in zero_cases:
            with self.subTest(msg="zero_cases", radius=radius):
                self.assertAlmostEqual(circle.perimeter(radius), expected)

        negative_cases = ((-1, -2 * math.pi), (-2, -4 * math.pi), (-1.5, -3 * math.pi))
        for radius, expected in negative_cases:
            with self.subTest(msg="negative_cases", radius=radius):
                self.assertAlmostEqual(circle.perimeter(radius), expected)

        string_cases = (("0", TypeError), ("2 + 2", TypeError), ("1.5", TypeError))
        for radius, expected in string_cases:
            with self.subTest(msg="string_cases", radius=radius):
                with self.assertRaises(expected):
                    circle.perimeter(radius)

        edge_cases = ((10**100, 2 * math.pi * 10**100), (-(10**100), -2 * math.pi * 10**100))
        for radius, expected in edge_cases:
            with self.subTest(msg="edge_cases", radius=radius):
                self.assertTrue(math.isclose(circle.perimeter(radius), expected))


class SquareTests(unittest.TestCase):
    def test_area(self):
        standard_cases = ((1, 1), (5, 25), (1.5, 2.25))
        for side, expected in standard_cases:
            with self.subTest(msg="standard_cases", side=side):
                self.assertAlmostEqual(square.area(side), expected)

        zero_cases = ((0, 0), (0.0, 0.0))
        for side, expected in zero_cases:
            with self.subTest(msg="zero_cases", side=side):
                self.assertAlmostEqual(square.area(side), expected)

        negative_cases = ((-1, 1), (-5, 25), (-1.5, 2.25))
        for side, expected in negative_cases:
            with self.subTest(msg="negative_cases", side=side):
                self.assertAlmostEqual(square.area(side), expected)

        string_cases = (("0", TypeError), ("2 + 2", TypeError), ("1.5", TypeError))
        for side, expected in string_cases:
            with self.subTest(msg="string_cases", side=side):
                with self.assertRaises(expected):
                    square.area(side)

        edge_cases = ((10**100, 10**200), (-(10**100), 10**200))
        for side, expected in edge_cases:
            with self.subTest(msg="edge_cases", side=side):
                self.assertAlmostEqual(square.area(side), expected)

    def test_perimeter(self):
        standard_cases = ((1, 4), (5, 20), (1.5, 6))
        for side, expected in standard_cases:
            with self.subTest(msg="standard_cases", side=side):
                self.assertAlmostEqual(square.perimeter(side), expected)

        zero_cases = ((0, 0), (0.0, 0.0))
        for side, expected in zero_cases:
            with self.subTest(msg="zero_cases", side=side):
                self.assertAlmostEqual(square.perimeter(side), expected)

        negative_cases = ((-1, -4), (-5, -20), (-1.5, -6))
        for side, expected in negative_cases:
            with self.subTest(msg="negative_cases", side=side):
                self.assertAlmostEqual(square.perimeter(side), expected)

        string_cases = (("0", TypeError), ("2 + 2", TypeError), ("1.5", TypeError))
        for side, expected in string_cases:
            with self.subTest(msg="string_cases", side=side):
                with self.assertRaises(expected):
                    square.perimeter(side)

        edge_cases = ((10**100, 4 * 10**100), (-(10**100), -4 * 10**100))
        for side, expected in edge_cases:
            with self.subTest(msg="edge_cases", side=side):
                self.assertAlmostEqual(square.perimeter(side), expected)


class RectangleTests(unittest.TestCase):
    def test_area(self):
        standard_cases = ((5, 3, 15), (1.5, 2, 3), (2, 2, 4))
        for width, height, expected in standard_cases:
            with self.subTest(msg="standard_cases", width=width, height=height):
                self.assertAlmostEqual(rectangle.area(width, height), expected)

        zero_cases = ((0, 3, 0), (3, 0, 0), (0.0, 0.0, 0.0))
        for width, height, expected in zero_cases:
            with self.subTest(msg="zero_cases", width=width, height=height):
                self.assertAlmostEqual(rectangle.area(width, height), expected)

        negative_cases = ((-5, 3, -15), (5, -3, -15), (-5, -3, 15))
        for width, height, expected in negative_cases:
            with self.subTest(msg="negative_cases", width=width, height=height):
                self.assertAlmostEqual(rectangle.area(width, height), expected)

        string_cases = (("0", 3, TypeError), (5, "2 + 2", TypeError), ("1.5", 2, TypeError))
        for width, height, expected in string_cases:
            with self.subTest(msg="string_cases", width=width, height=height):
                with self.assertRaises(expected):
                    rectangle.area(width, height)

        edge_cases = ((10**100, 10**100, 10**200), (-(10**100), 10**100, -(10**200)))
        for width, height, expected in edge_cases:
            with self.subTest(msg="edge_cases", width=width, height=height):
                self.assertAlmostEqual(rectangle.area(width, height), expected)

    def test_perimeter(self):
        standard_cases = ((5, 3, 16), (1.5, 2, 7), (2, 2, 8))
        for width, height, expected in standard_cases:
            with self.subTest(msg="standard_cases", width=width, height=height):
                self.assertAlmostEqual(rectangle.perimeter(width, height), expected)

        zero_cases = ((0, 3, 6), (3, 0, 6), (0.0, 0.0, 0.0))
        for width, height, expected in zero_cases:
            with self.subTest(msg="zero_cases", width=width, height=height):
                self.assertAlmostEqual(rectangle.perimeter(width, height), expected)

        negative_cases = ((-5, 3, -4), (5, -3, 4), (-5, -3, -16))
        for width, height, expected in negative_cases:
            with self.subTest(msg="negative_cases", width=width, height=height):
                self.assertAlmostEqual(rectangle.perimeter(width, height), expected)

        string_cases = (("0", 3, TypeError), (5, "2 + 2", TypeError), ("1.5", 2, TypeError))
        for width, height, expected in string_cases:
            with self.subTest(msg="string_cases", width=width, height=height):
                with self.assertRaises(expected):
                    rectangle.perimeter(width, height)

        edge_cases = ((10**100, 10**100, 4 * 10**100), (-(10**100), -(10**100), -4 * 10**100))
        for width, height, expected in edge_cases:
            with self.subTest(msg="edge_cases", width=width, height=height):
                self.assertAlmostEqual(rectangle.perimeter(width, height), expected)


class TriangleTests(unittest.TestCase):
    def test_area(self):
        standard_cases = ((5, 3, 7.5), (1.5, 2, 1.5), (2, 2, 2))
        for base, height, expected in standard_cases:
            with self.subTest(msg="standard_cases", base=base, height=height):
                self.assertAlmostEqual(triangle.area(base, height), expected)

        zero_cases = ((0, 3, 0), (3, 0, 0), (0.0, 0.0, 0.0))
        for base, height, expected in zero_cases:
            with self.subTest(msg="zero_cases", base=base, height=height):
                self.assertAlmostEqual(triangle.area(base, height), expected)

        negative_cases = ((-5, 3, -7.5), (5, -3, -7.5), (-5, -3, 7.5))
        for base, height, expected in negative_cases:
            with self.subTest(msg="negative_cases", base=base, height=height):
                self.assertAlmostEqual(triangle.area(base, height), expected)

        string_cases = (("0", 3, TypeError), (5, "2 + 2", TypeError), ("1.5", 2, TypeError))
        for base, height, expected in string_cases:
            with self.subTest(msg="string_cases", base=base, height=height):
                with self.assertRaises(expected):
                    triangle.area(base, height)

        edge_cases = (
            (10**100, 10**100, 5 * 10**199),
            (-(10**100), 10**100, -(5 * 10**199)))
        for base, height, expected in edge_cases:
            with self.subTest(msg="edge_cases", base=base, height=height):
                self.assertAlmostEqual(triangle.area(base, height), expected)

    def test_perimeter(self):
        standard_cases = ((3, 4, 5, 12), (1.5, 2, 2.5, 6), (2, 2, 2, 6))
        for side_a, side_b, side_c, expected in standard_cases:
            with self.subTest(msg="standard_cases", sides=(side_a, side_b, side_c)):
                self.assertAlmostEqual(
                    triangle.perimeter(side_a, side_b, side_c), expected
                )

        zero_cases = ((0, 0, 0, 0), (0.0, 0.0, 0.0, 0.0))
        for side_a, side_b, side_c, expected in zero_cases:
            with self.subTest(msg="zero_cases", sides=(side_a, side_b, side_c)):
                self.assertAlmostEqual(
                    triangle.perimeter(side_a, side_b, side_c), expected
                )

        negative_cases = ((-3, 4, 5, 6), (3, -4, 5, 4), (-3, -4, -5, -12))
        for side_a, side_b, side_c, expected in negative_cases:
            with self.subTest(msg="negative_cases", sides=(side_a, side_b, side_c)):
                self.assertAlmostEqual(
                    triangle.perimeter(side_a, side_b, side_c), expected
                )

        string_cases = (
            ("3", 4, 5, TypeError),
            (3, "2 + 2", 5, TypeError),
            (3, 4, "5", TypeError),
        )
        for side_a, side_b, side_c, expected in string_cases:
            with self.subTest(msg="string_cases", sides=(side_a, side_b, side_c)):
                with self.assertRaises(expected):
                    triangle.perimeter(side_a, side_b, side_c)

        edge_cases = ((10**100, 10**100, 10**100, 3 * 10**100), (-(10**100), -(10**100), -(10**100), -3 * 10**100))
        for side_a, side_b, side_c, expected in edge_cases:
            with self.subTest(msg="edge_cases", sides=(side_a, side_b, side_c)):
                self.assertAlmostEqual(
                    triangle.perimeter(side_a, side_b, side_c), expected
                )
