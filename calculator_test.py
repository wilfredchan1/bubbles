import unittest
from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    calculator = Calculator()
    def test_add(self):
        self.assertEqual(4, self.calculator.add(2,2))
        self.assertEqual(3.2, self.calculator.add(1,2.2))

    def test_sub(self):
        self.assertEqual(2, self.calculator.sub(3,1))
        self.assertEqual(-2, self.calculator.sub(1,3))

    def test_mult(self):
        self.assertEqual(12, self.calculator.mult(3,4))
        self.assertEqual(13.5, self.calculator.mult(3,4.5))

    def test_div(self):
        self.assertEqual(3, self.calculator.div(9,3))
        
        with self.assertRaises(ZeroDivisionError):
            self.calculator.div(3,0)


if __name__ == "__main__":
    unittest.main() 