import unittest
import triangle


class TriangleTestCase(unittest.TestCase):
    # Площадь: основание длинною 0 (любая высота)
    def test_zero_base_area(self):
        res = triangle.area(0, 5)
        self.assertEqual(res, 0)

    # Площадь: высота длинною 0 (любое основание)
    def test_zero_height_area(self):
        res = triangle.area(5, 0)
        self.assertEqual(res, 0)

    # Площадь: оба аргумента - 0
    def test_zero_area(self):
        res = triangle.area(0, 0)
        self.assertEqual(res, 0)

    # Площадь: обычные значения
    def test_regular_area(self):
        res = triangle.area(5, 4)
        self.assertEqual(res, 10)

    # Площадь: основание и высота = 1
    def test_one_side_area(self):
        res = triangle.area(1, 2)
        self.assertEqual(res, 1)

    # Площадь: нецелочисленные значения
    def test_float_area(self):
        res = triangle.area(2.5, 3)
        self.assertEqual(res, 3.75)

    # Площадь: большие значения
    def test_big_area(self):
        res = triangle.area(10**10, 2 * 10**10)
        self.assertEqual(res, 10**20)

    # Периметр: все стороны 0
    def test_zero_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    # Периметр: обычные длины сторон
    def test_regular_perimeter(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    # Периметр: нецелочисленные длины сторон
    def test_float_perimeter(self):
        res = triangle.perimeter(2.5, 3.0, 4.5)
        self.assertEqual(res, 10.0)

    # Периметр: все стороны = 1
    def test_one_perimeter(self):
        res = triangle.perimeter(1, 1, 1)
        self.assertEqual(res, 3)

    # Периметр: большие длины сторон
    def test_big_perimeter(self):
        side = 10**15
        res = triangle.perimeter(side, side, side)
        self.assertEqual(res, 3 * side)
