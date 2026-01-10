import unittest
import logging
from HomeworkCalc import Calculator


class TestHomework22(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_error(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def test_maximum(self):
        self.assertEqual(self.calc.maximum(100, 50), 100)

    def test_minimum(self):
        self.assertEqual(self.calc.minimum(100, 50), 50)

    def test_percent(self):
        self.assertEqual(self.calc.percent(1000, 5), 50)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)


if __name__ == "__main__":
    logging.error("Test str work")
    unittest.main()
