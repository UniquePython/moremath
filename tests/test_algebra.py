import unittest
from moremath.algebra import exponentiation, logarithm, sieve_of_eratosthenes, prime_factors

class TestAlgebraFunctions(unittest.TestCase):
    def test_exponentiation(self):
        self.assertEqual(exponentiation(2, 3), 8)
        self.assertEqual(exponentiation(5, 2), 25)
        self.assertAlmostEqual(exponentiation(2, 0.5), 1.4142135623730951, places=10)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(100, 10), 2)
        self.assertAlmostEqual(logarithm(10, 10), 1)
        self.assertAlmostEqual(logarithm(1, 10), 0)
        self.assertAlmostEqual(logarithm(2, 2), 1)
        self.assertAlmostEqual(logarithm(1000, 10), 3)

    def test_exponentiation_invalid_input(self):
        with self.assertRaises(TypeError):
            exponentiation("2", 3)
        with self.assertRaises(TypeError):
            exponentiation(2, "3")

    def test_logarithm_invalid_input(self):
        with self.assertRaises(TypeError):
            logarithm("100", 10)
        with self.assertRaises(TypeError):
            logarithm(100, "10")
        with self.assertRaises(ValueError):
            logarithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(100, 0)
        with self.assertRaises(ValueError):
            logarithm(100, 1)

    def test_sieve_of_eratosthenes(self):
        self.assertEqual(sieve_of_eratosthenes(0), [])
        self.assertEqual(sieve_of_eratosthenes(1), [])
        self.assertEqual(sieve_of_eratosthenes(2), [2])
        self.assertEqual(sieve_of_eratosthenes(10), [2, 3, 5, 7])
        self.assertEqual(sieve_of_eratosthenes(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(sieve_of_eratosthenes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        self.assertEqual(sieve_of_eratosthenes(50), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
        self.assertEqual(sieve_of_eratosthenes(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                                                      59, 61, 67, 71, 73, 79, 83, 89, 97])
        self.assertEqual(sieve_of_eratosthenes(1000), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                                                       59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
                                                       113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
                                                       179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
                                                       239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
                                                       307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367,
                                                       373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433,
                                                       439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
                                                       503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                                                       587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643,
                                                       647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719,
                                                       727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
                                                       809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
                                                       877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947,
                                                       953, 967, 971, 977, 983, 991, 997])

    def test_prime_factors(self):
        self.assertEqual(prime_factors(7), [7])
        self.assertEqual(prime_factors(12), [2, 2, 3])
        self.assertEqual(prime_factors(1), [])
        self.assertEqual(prime_factors(0), [])
        self.assertEqual(prime_factors(97), [97])
        self.assertEqual(prime_factors(100), [2, 2, 5, 5])

if __name__ == '__main__':
    unittest.main()
