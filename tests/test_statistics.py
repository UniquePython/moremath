import unittest
from moremath.statistics import mean, median, mode, variance, standard_deviation

class TestStatisticsFunctions(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(mean([1, 2, 3]), 2.0)
        self.assertEqual(mean([2, 4, 6, 8, 10]), 6.0)

    def test_median(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(median([1, 3, 5, 7, 9]), 5)
        self.assertEqual(median([2, 4, 6, 8, 10]), 6)

    def test_mode(self):
        self.assertEqual(mode([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), 4)
        self.assertEqual(mode([1, 1, 2, 3, 3, 3, 4, 4, 4, 4]), 4)
        self.assertEqual(mode([1, 2, 3, 4, 5]), 1)  

    def test_standard_deviation(self):
        # Test case 1: Simple example
        data1 = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(standard_deviation(data1), 1.58, places=2)

        # Test case 2: All numbers the same
        data2 = [10] * 5
        self.assertAlmostEqual(standard_deviation(data2), 0.0, places=2)

        # Test case 3: Random data
        data3 = [5, 10, 15, 20, 25]
        self.assertAlmostEqual(standard_deviation(data3), 7.91, places=2)

    def test_variance(self):
        # Test case 1: Simple example
        data1 = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(variance(data1), 2.5, places=1)

        # Test case 2: All numbers the same
        data2 = [10] * 5
        self.assertAlmostEqual(variance(data2), 0.0, places=1)

        # Test case 3: Random data
        data3 = [5, 10, 15, 20, 25]
        self.assertAlmostEqual(variance(data3), 62.5, places=1)


if __name__ == '__main__':
    unittest.main()
