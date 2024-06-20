from typing import Union, Tuple, List
import cmath
from math import isqrt
import numpy as np

def exponentiation(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """Calculate exponentiation of a base to a given exponent."""
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Both base and exponent must be integers or floats")
    return base ** exponent

def logarithm(x: Union[int, float], base: Union[int, float] = 10) -> Union[float, complex]:
    """Calculate logarithm of x with a specified base."""
    if not isinstance(x, (int, float)):
        raise TypeError("x must be an integer or float")
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be an integer or float")
    if x <= 0:
        raise ValueError("x must be greater than 0")
    if base <= 0 or base == 1:
        raise ValueError("Base must be greater than 0 and not equal to 1")
    from math import log
    return log(x, base)

def sieve_of_eratosthenes(n: int) -> List[int]:
    """
    Generates all prime numbers up to n using the Sieve of Eratosthenes algorithm.

    Args:
        n (int): The upper limit for prime numbers.

    Returns:
        List[int]: A list of prime numbers up to n.
    """
    if n < 2:
        return []
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n + 1) if primes[i]]

def prime_factors(n: int) -> List[int]:
    """
    Finds prime factors of a given number.

    Args:
        n (int): The number to find prime factors for.

    Returns:
        List[int]: A list of prime factors of the given number.
    """
    factors = []
    if n <= 1:
        return factors
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, isqrt(n) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)    
    return factors

def solve_quadratic(a: float, b: float, c: float) -> Union[str, Tuple[complex, complex]]:
    """
    Solves the quadratic equation ax^2 + bx + c = 0.

    Args:
        a (float): Coefficient of x^2.
        b (float): Coefficient of x.
        c (float): Constant term.

    Returns:
        Union[str, Tuple[complex, complex]]: Returns a tuple of two solutions if solvable,
                                             otherwise returns an error message.
    """
    if a == 0:
        return "Coefficient 'a' cannot be zero for a quadratic equation."
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        sol1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        sol2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    else:
        # Complex roots
        sol1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        sol2 = (-b - cmath.sqrt(discriminant)) / (2*a)

    return sol1, sol2

def solve_cubic(a: float, b: float, c: float, d: float) -> Union[str, List[complex]]:
    """
    Solves the cubic equation ax^3 + bx^2 + cx + d = 0.

    Args:
        a (float): Coefficient of x^3.
        b (float): Coefficient of x^2.
        c (float): Coefficient of x.
        d (float): Constant term.

    Returns:
        Union[str, List[complex]]: Returns a list of three solutions if solvable,
                                   otherwise returns an error message.
    """
    if a == 0:
        return "Coefficient 'a' cannot be zero for a cubic equation."

    # Normalize coefficients
    b /= a
    c /= a
    d /= a
    
    # Depressed cubic coefficients
    p = c - b**2 / 3
    q = 2 * b**3 / 27 - b * c / 3 + d
    delta = (q / 2)**2 + (p / 3)**3

    roots = []

    if delta > 0:
        # One real root and two complex conjugate roots
        u = np.cbrt(-q / 2 + np.sqrt(delta))
        v = np.cbrt(-q / 2 - np.sqrt(delta))
        root1 = u + v - b / 3
        root2 = -(u + v) / 2 - b / 3 + cmath.sqrt(3) * (u - v) / 2j
        root3 = -(u + v) / 2 - b / 3 - cmath.sqrt(3) * (u - v) / 2j
        roots = [root1, root2, root3]
    elif delta == 0:
        # All roots real, at least two are equal
        u = np.cbrt(-q / 2)
        root1 = 2 * u - b / 3
        root2 = -u - b / 3
        roots = [root1, root2, root2]
    else:
        # Three real roots
        theta = np.arccos(-q / (2 * np.sqrt(-(p / 3)**3)))
        root1 = 2 * np.sqrt(-p / 3) * np.cos(theta / 3) - b / 3
        root2 = 2 * np.sqrt(-p / 3) * np.cos((theta + 2 * np.pi) / 3) - b / 3
        root3 = 2 * np.sqrt(-p / 3) * np.cos((theta + 4 * np.pi) / 3) - b / 3
        roots = [root1, root2, root3]

    return roots