from typing import Union
import math

class Geometry:
    """Class to encapsulate various geometric operations."""

    @staticmethod
    def validate_positive_number(value: Union[int, float]) -> None:
        """Validate if the input is a positive number."""
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        if value <= 0:
            raise ValueError("Input must be a positive number.")

    @staticmethod
    def square_perimeter(side_length: Union[int, float]) -> Union[int, float]:
        """Calculate the perimeter of a square."""
        Geometry.validate_positive_number(side_length)
        return 4 * side_length

    @staticmethod
    def square_area(side_length: Union[int, float]) -> Union[int, float]:
        """Calculate the area of a square."""
        Geometry.validate_positive_number(side_length)
        return side_length ** 2

    @staticmethod
    def rectangle_perimeter(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
        """Calculate the perimeter of a rectangle."""
        Geometry.validate_positive_number(length)
        Geometry.validate_positive_number(width)
        return 2 * (length + width)

    @staticmethod
    def rectangle_area(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
        """Calculate the area of a rectangle."""
        Geometry.validate_positive_number(length)
        Geometry.validate_positive_number(width)
        return length * width

    @staticmethod
    def circle_perimeter(radius: Union[int, float]) -> Union[int, float]:
        """Calculate the perimeter of a circle."""
        Geometry.validate_positive_number(radius)
        return 2 * math.pi * radius

    @staticmethod
    def circle_area(radius: Union[int, float]) -> Union[int, float]:
        """Calculate the area of a circle."""
        Geometry.validate_positive_number(radius)
        return math.pi * radius ** 2

    @staticmethod
    def cube_volume(side_length: Union[int, float]) -> Union[int, float]:
        """Calculate the volume of a cube."""
        Geometry.validate_positive_number(side_length)
        return side_length ** 3

    @staticmethod
    def cube_surface_area(side_length: Union[int, float]) -> Union[int, float]:
        """Calculate the surface area of a cube."""
        Geometry.validate_positive_number(side_length)
        return 6 * side_length ** 2

    @staticmethod
    def sphere_volume(radius: Union[int, float]) -> Union[int, float]:
        """Calculate the volume of a sphere."""
        Geometry.validate_positive_number(radius)
        return (4 / 3) * math.pi * radius ** 3

    @staticmethod
    def sphere_surface_area(radius: Union[int, float]) -> Union[int, float]:
        """Calculate the surface area of a sphere."""
        Geometry.validate_positive_number(radius)
        return 4 * math.pi * radius ** 2
