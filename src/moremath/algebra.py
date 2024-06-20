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

