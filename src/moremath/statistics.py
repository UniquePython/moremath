from typing import List, Union
from collections import Counter
import statistics
import math

def mean(data: List[Union[int, float]]) -> Union[int, float]:
    """
    Calculate the mean (average) of a list of numbers.

    Args:
        data (List[Union[int, float]]): List of numbers (integers or floats).

    Returns:
        Union[int, float]: Mean of the input data.

    Raises:
        ValueError: If the input list is empty.
    """
    if not data:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(data) / len(data)

def median(data: List[Union[int, float]]) -> Union[int, float]:
    """
    Calculate the median of a list of numbers.

    Args:
        data (List[Union[int, float]]): List of numbers (integers or floats).

    Returns:
        Union[int, float]: Median of the input data.

    Raises:
        ValueError: If the input list is empty.
    """
    if not data:
        raise ValueError("Cannot calculate median of empty list")
    return statistics.median(data)

def mode(data: List[Union[int, float]]) -> Union[int, float]:
    """
    Calculate the mode of a list of numbers.

    Args:
        data (List[Union[int, float]]): List of numbers (integers or floats).

    Returns:
        Union[int, float]: Mode of the input data.

    Raises:
        ValueError: If the input list is empty.
    """
    if not data:
        raise ValueError("Cannot calculate mode of empty list")
    counts = Counter(data)
    mode_values = counts.most_common(1)
    return mode_values[0][0]

def variance(data: List[Union[int, float]]) -> Union[int, float]:
    """
    Calculate the variance of a list of numbers.

    Args:
        data (List[Union[int, float]]): List of numbers (integers or floats).

    Returns:
        Union[int, float]: Variance of the input data.

    Raises:
        ValueError: If the input list has fewer than two elements (variance is undefined).
    """
    if len(data) < 2:
        raise ValueError("Variance requires at least two data points")
    mean_value = mean(data)
    return sum((x - mean_value) ** 2 for x in data) / (len(data) - 1)

def standard_deviation(data: List[Union[int, float]]) -> Union[int, float]:
    """
    Calculate the standard deviation of a list of numbers.

    Args:
        data (List[Union[int, float]]): List of numbers (integers or floats).

    Returns:
        Union[int, float]: Standard deviation of the input data.

    Raises:
        ValueError: If the input list has fewer than two elements (standard deviation is undefined).
    """
    if len(data) < 2:
        raise ValueError("Standard deviation requires at least two data points")
    return math.sqrt(variance(data))
