from typing import Union
from math import log

class Algebra:
    """Class to encapsulate various mathematical operations."""

    @staticmethod
    def check_number(x: Union[int, float]):
        """
        Check if the input is a number.
        """
        if isinstance(x, (int, float)):
            return True
        elif not isinstance(x, (int, float)):
            raise ValueError("Input must be a number.")

    @staticmethod
    def exponentiation(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """Calculate exponentiation of a base to a given exponent."""
        Algebra.check_number(base)
        Algebra.check_number(exponent)
        return base ** exponent

    @staticmethod
    def logarithm(x: Union[int, float], base: Union[int, float] = 10) -> Union[float, complex]:
        """Calculate logarithm of x with a specified base."""
        Algebra.check_number(x)
        Algebra.check_number(base)
        if base <= 0 or base == 1:
            raise ValueError("Base must be greater than 0 and not equal to 1")
        return log(x, base)
