import unittest
from moremath.geometry import square_perimeter, square_area, rectangle_perimeter, rectangle_area, \
    circle_perimeter, circle_area, cube_volume, cube_surface_area, sphere_volume, sphere_surface_area, \
    validate_positive_number, distance_between_points, equation_of_line, slope_of_line
import math

class TestGeometryFunctions(unittest.TestCase):

    def test_square_perimeter(self):
        self.assertAlmostEqual(square_perimeter(4), 16)
        self.assertAlmostEqual(square_perimeter(5), 20)
        with self.assertRaises(ValueError):
            square_perimeter(-1)

    def test_square_area(self):
        self.assertAlmostEqual(square_area(4), 16)
        self.assertAlmostEqual(square_area(5), 25)
        with self.assertRaises(ValueError):
            square_area(-1)

    def test_rectangle_perimeter(self):
        self.assertAlmostEqual(rectangle_perimeter(4, 5), 18)
        self.assertAlmostEqual(rectangle_perimeter(2, 3), 10)
        with self.assertRaises(ValueError):
            rectangle_perimeter(-1, 5)
        with self.assertRaises(ValueError):
            rectangle_perimeter(4, -1)

    def test_rectangle_area(self):
        self.assertAlmostEqual(rectangle_area(4, 5), 20)
        self.assertAlmostEqual(rectangle_area(2, 3), 6)
        with self.assertRaises(ValueError):
            rectangle_area(-1, 5)
        with self.assertRaises(ValueError):
            rectangle_area(4, -1)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(4), 2 * math.pi * 4)
        self.assertAlmostEqual(circle_perimeter(5), 2 * math.pi * 5)
        with self.assertRaises(ValueError):
            circle_perimeter(-1)

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(4), math.pi * 4 ** 2)
        self.assertAlmostEqual(circle_area(5), math.pi * 5 ** 2)
        with self.assertRaises(ValueError):
            circle_area(-1)

    def test_cube_volume(self):
        self.assertAlmostEqual(cube_volume(3), 27)
        self.assertAlmostEqual(cube_volume(4), 64)
        with self.assertRaises(ValueError):
            cube_volume(-1)

    def test_cube_surface_area(self):
        self.assertAlmostEqual(cube_surface_area(3), 6 * 3 ** 2)
        self.assertAlmostEqual(cube_surface_area(4), 6 * 4 ** 2)
        with self.assertRaises(ValueError):
            cube_surface_area(-1)

    def test_sphere_volume(self):
        self.assertAlmostEqual(sphere_volume(3), (4 / 3) * math.pi * 3 ** 3)
        self.assertAlmostEqual(sphere_volume(4), (4 / 3) * math.pi * 4 ** 3)
        with self.assertRaises(ValueError):
            sphere_volume(-1)

    def test_sphere_surface_area(self):
        self.assertAlmostEqual(sphere_surface_area(3), 4 * math.pi * 3 ** 2)
        self.assertAlmostEqual(sphere_surface_area(4), 4 * math.pi * 4 ** 2)
        with self.assertRaises(ValueError):
            sphere_surface_area(-1)

    def test_validate_positive_number(self):
        self.assertIsNone(validate_positive_number(5))  # Should not raise any errors
        with self.assertRaises(TypeError):
            validate_positive_number("string")  # Should raise TypeError
        with self.assertRaises(ValueError):
            validate_positive_number(0)  # Should raise ValueError

    def test_distance_between_points(self):
        # Test cases for distance calculation
        self.assertAlmostEqual(distance_between_points(1, 2, 4, 6), 5.0, places=1)
        self.assertAlmostEqual(distance_between_points(0, 0, 3, 4), 5.0, places=1)
        self.assertAlmostEqual(distance_between_points(-1, -2, -4, -6), 5.0, places=1)

    def test_slope_of_line(self):
        # Test cases for slope calculation
        self.assertAlmostEqual(slope_of_line(1, 2, 4, 6), 1.33, places=2)
        self.assertAlmostEqual(slope_of_line(0, 0, 3, 4), 1.33, places=2)
        self.assertAlmostEqual(slope_of_line(-1, -2, -4, -6), 1.33, places=2)
        with self.assertRaises(ValueError):
            slope_of_line(1, 2, 1, 6)  # Vertical line, should raise ValueError

    def test_equation_of_line(self):
        # Test cases for equation calculation
        self.assertEqual(equation_of_line(1, 2, 4, 6), "y = 1.33x + 0.67")
        self.assertEqual(equation_of_line(0, 0, 3, 4), "y = 1.33x")
        self.assertEqual(equation_of_line(-1, -2, -4, -6), "y = 1.33x - 0.67")
        self.assertEqual(equation_of_line(1, 2, 1, 6), "The line is vertical and slope is undefined.")

if __name__ == '__main__':
    unittest.main()
