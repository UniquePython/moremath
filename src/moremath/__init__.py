__version__ = '0.1.2'

from .algebra import exponentiation, logarithm, sieve_of_eratosthenes, solve_cubic, solve_quadratic, prime_factors
from .statistics import mean, median, mode, standard_deviation, variance
from .arithmetic import add, subtract, multiply, divide, factorial
from .geometry import (
    square_perimeter, square_area,
    rectangle_perimeter, rectangle_area,
    circle_perimeter, circle_area,
    cube_volume, cube_surface_area,
    sphere_volume, sphere_surface_area, validate_positive_number
)
