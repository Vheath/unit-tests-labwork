import unittest

import square


class SquareTestCase(unittest.TestCase):
    # Площадь: Квадрат со стороной 0
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    # Площадь: Квадрат с обычной стороной
    def test_regular_area(self):
        res = square.area(5)
        self.assertEqual(res, 25)

    # Площадь: Квадрат с длинами сторон 1, 1
    def test_one_square_area(self):
        res = square.area(1)
        self.assertEqual(res, 1)

    # Площадь: Квадрат с нецелочисленной длинной стороны
    def test_float_area(self):
        res = square.area(2.5)
        self.assertEqual(res, 6.25)

    # Площадь: Квадрат с большой длинной стороны
    def test_big_area(self):
        res = square.area(10 ** 19)
        self.assertEqual(res, 10 ** 38)


    # Периметр: Квадрат со стороной 0
    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    # Периметр: Обычные длины сторон 
    def test_regular_perimeter(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)

    # Периметр: Нецелочисленные длины сторон
    def test_float_perimeter(self):
        res = square.perimeter(2.5)
        self.assertEqual(res, 10)

    # Периметр: Квадрат с единичной длинной стороны
    def test_one_perimeter(self):
        res = square.perimeter(1)
        self.assertEqual(res, 4)

    # Периметр: Квадрат с большой длинной стороны
    def test_big_perimeter(self):
        res = square.perimeter(10 ** 29)
        self.assertEqual(res, 4 * (10 ** 29))
