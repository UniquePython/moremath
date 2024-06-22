from typing import List, Union
from math import isqrt

class PrimeUtilities:
    """Class to encapsulate prime number related utilities."""

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
    def sieve_of_eratosthenes(n: int) -> List[int]:
        """
        Generates all prime numbers up to n using the Sieve of Eratosthenes algorithm.

        Args:
            n (int): The upper limit for prime numbers.

        Returns:
            List[int]: A list of prime numbers up to n.
        """
        PrimeUtilities.check_number(n)
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

    @staticmethod
    def prime_factors(n: int) -> List[int]:
        """
        Finds prime factors of a given number.

        Args:
            n (int): The number to find prime factors for.

        Returns:
            List[int]: A list of prime factors of the given number.
        """
        PrimeUtilities.check_number(n)
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