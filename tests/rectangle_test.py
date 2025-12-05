import unittest

import rectangle


class RectangleTestCase(unittest.TestCase):
    # Площадь: Прямоугольник со стороной 0
    def test_zero_area(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    # Площадь: Прямоугольник с обычными сторонами
    def test_regular_area(self):
        res = rectangle.area(5, 4)
        self.assertEqual(res, 20)

    # Площадь: Прямоугольник с длинами сторон 10, 10
    def test_square_area(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    # Площадь: Прямоугольник с длинами сторон 1, 1
    def test_one_square_area(self):
        res = rectangle.area(1, 1)
        self.assertEqual(res, 1)

    # Площадь: Прямоугольник с нецелочисленной длинной стороны
    def test_float_area(self):
        res = rectangle.area(2.5, 4)
        self.assertEqual(res, 10)

    # Площадь: Прямоугольник с большими длинами сторон
    def test_big_area(self):
        res = rectangle.area(100000000000000000, 40000000)
        self.assertEqual(res, 4000000000000000000000000)

    # Периметр: обычные длины сторон 
    def test_regular_perimeter(self):
        res = rectangle.perimeter(10, 5)
        self.assertEqual(res, 30)

    # Периметр: нецелочисленные длины сторон
    def test_float_perimeter(self):
        res = rectangle.perimeter(2.5, 3.5)
        self.assertEqual(res, 12)

    # Периметр: нулевые длины сторон
    def test_zero_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

    # Периметр: Прямоугольник с длинами сторон 1, 1
    def test_one_perimeter(self):
        res = rectangle.perimeter(1, 1)
        self.assertEqual(res, 4)

    # Периметр: Прямоугольник с большими длинами сторон
    def test_big_perimeter(self):
        res = rectangle.perimeter(100000000000000000, 40000000)
        self.assertEqual(res, 200000000080000000)
