

def sum(a , b ):
    """
    >>> sum(5,7)
    12

    >>> sum(4,-4)
    0
    """
    return a + b

def subtract(a, b ):
    """
    >>> subtract(3,8)
    -5
    """
    return a - b

def divide(a ,b):
    """
    >>> divide(10,0)
    Traceback (most recent call last):
    ValueError: Cannot divide by zero

    """
    if b ==0:
        raise ValueError("Cannot divide by zero")
    return a / b

def multiply(a, b):
    return a * b


