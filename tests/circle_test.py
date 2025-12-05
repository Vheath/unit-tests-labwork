import unittest
import math
import circle


class CircleTestCase(unittest.TestCase):

    # Площадь: радиус 0
    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    # Площадь: обычный радиус
    def test_regular_area(self):
        res = circle.area(2)
        expected = math.pi * 4  # π * 2^2
        self.assertAlmostEqual(res, expected, places=9)

    # Площадь: радиус = 1
    def test_one_radius_area(self):
        res = circle.area(1)
        expected = math.pi
        self.assertAlmostEqual(res, expected, places=9)

    # Площадь: нецелочисленный радиус
    def test_float_area(self):
        res = circle.area(2.5)
        expected = math.pi * (2.5**2)
        self.assertAlmostEqual(res, expected, places=9)

    # Площадь: большой радиус
    def test_big_area(self):
        r = 10 ** 10
        res = circle.area(r)
        expected = math.pi * r * r
        self.assertAlmostEqual(
            res, expected, delta=1e4
        )  # допускаем небольшую абсолютную погрешность

    # Периметр: радиус 0
    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    # Периметр: обычный радиус
    def test_regular_perimeter(self):
        res = circle.perimeter(2)
        expected = 2 * math.pi * 2
        self.assertAlmostEqual(res, expected, places=9)

    # Периметр: радиус = 1
    def test_one_radius_perimeter(self):
        res = circle.perimeter(1)
        expected = 2 * math.pi
        self.assertAlmostEqual(res, expected, places=9)

    # Периметр: нецелочисленный радиус
    def test_float_perimeter(self):
        res = circle.perimeter(2.5)
        expected = 2 * math.pi * 2.5
        self.assertAlmostEqual(res, expected, places=9)

    # Периметр: большой радиус
    def test_big_perimeter(self):
        r = 10 ** 12
        res = circle.perimeter(r)
        expected = 2 * math.pi * r
        self.assertAlmostEqual(res, expected, places = 9)
