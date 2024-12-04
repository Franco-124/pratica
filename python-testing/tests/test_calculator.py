import unittest
from src.calculator import sum,subtract,divide,multiply

class Calculator(unittest.TestCase):
    def test_sum(self):
        assert sum(1, 2) == 3
    
    def test_rest(self):
        assert subtract(2, 1) == 1
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
            def division(a,b):    
                if b == 0:        
                    raise ValueError("La divisón por cero no esta permitida")    
                else:        
                     return a / b
    
    def test_multiply(self):
        assert multiply(3, 2) == 6
     