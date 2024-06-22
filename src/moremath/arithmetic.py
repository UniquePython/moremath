from typing import Union

class MathOperations:
    """Class to encapsulate various mathematical operations."""

    @staticmethod
    def check_number(x: Union[int, float]) -> bool:
        """
        Check if the input is a number.
        """
        if isinstance(x, (int, float)):
            return True
        else:
            raise ValueError("Input must be a number.")

    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Return the sum of two numbers a and b.
        """
        MathOperations.check_number(a)
        MathOperations.check_number(b)
        return a + b

    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Return the difference between two numbers a and b.
        """
        MathOperations.check_number(a)
        MathOperations.check_number(b)
        return a - b

    @staticmethod
    def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Return the product of two numbers a and b.
        """
        MathOperations.check_number(a)
        MathOperations.check_number(b)
        return a * b

    @staticmethod
    def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Return the result of the division of a by b.
        """
        MathOperations.check_number(a)
        MathOperations.check_number(b)
        if b == 0:
            raise ValueError("The divisor (b) must not be zero.")
        return a / b

    @staticmethod
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
