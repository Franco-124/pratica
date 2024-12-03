import unittest
from src.calculator import sum,subtract,divide,multiply

class Calcultator(unittest.TestCase):
    def test_sum(self):
        assert sum(1, 2) == 3
    
    def test_rest(self):
        assert subtract(2, 1) == 1
    
    def test_divide(self):
        result=divide(10,2)
        expected = 5
        assert result==expected
        
        try:
            divide(10, 0)
        except ValueError as e:
            assert str(e) == "Cannot divide by zero"
        else:
            assert False, "Expected ValueError to be raised"
    
    def test_multiply(self):
        assert multiply(3, 2) == 6
     