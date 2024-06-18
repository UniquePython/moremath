from typing import Union

def check_number(x: Union[int, float]):
    """
    Check if the input is a number.
    """
    if isinstance(x, (int, float)):
        return True
    elif not isinstance(x, (int, float)):
        raise ValueError("Input must be a number.")

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Return the sum of two numbers a and b.
    """
    check_number(a)
    check_number(b)
    return a + b

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Return the difference between two numbers a and b.
    """
    check_number(a)
    check_number(b)
    return a - b

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Return the product of two numbers a and b.
    """
    check_number(a)
    check_number(b)
    return a * b

def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Return the result of the division of a by b.
    """
    check_number(a)
    check_number(b)
    if b == 0:
        raise ValueError("The divisor (b) must not be zero.")
    return a / b

def factorial(n: int) -> int:
    """
    Return the factorial of a non-negative integer n.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
