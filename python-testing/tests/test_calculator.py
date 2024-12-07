import unittest
from src.calculator import sum,subtract,divide,multiply

class Calculator(unittest.TestCase):
    def test_sum(self):
        assert sum(1, 2) == 3
    
    def test_rest(self):
        assert subtract(2, 1) == 1
    
    def test_multiply(self):
        result = multiply(2, 3)
        expected = 6
        assert result == expected
    
    def test_division(self):
        result = divide(10 ,2)
        expected = 5
        assert result == expected
    
    
    def test_divide_by_cero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

     