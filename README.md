# moremath

`moremath` is a Python package that provides a collection of advanced mathematical functions covering various areas such as algebra, statistics, arithmetic, and geometry. This library is designed to assist developers, data scientists, and mathematicians in performing complex mathematical operations with ease.

# Installation

You can install the package via pip:
```console
pip install moremath
```

To install a specific version, use:
```console
pip install moremath==<version_number_here>
```

> [!NOTE]
> **Stable versions are as follows:**
> | Version |         Notes           |
> |---------|-------------------------|
> | 0.0.1   | Initial stable release. |
> | 0.0.2   | Minor improvements.     |
> | 0.1.2   | New features added.     |
> | 0.2.2   | Latest version.         |

# Modules
## Algebra
This deals with **exponentiation**, **logarithm**, **sieve of eratosthenes**, **prime factors**.

### Examples
#### - Exponentiation
```python
from moremath.algebra import exponentiation as exp

base = float(input("Enter the base:"))
exponent = float(input("Enter the exponent:"))

result = exp(base, exponent)
```

#### - Logarithm
```python
from moremath.algebra import logarithm as log

num = float(input("Enter the number whose logarithm you want to find:"))
base = float(input("Enter the base:"))

result = log(num, base)
```

#### - Sieve Of Eratosthenes
```python
from moremath.algebra import sieve_of_eratosthenes as se

num = int(input("Enter the number till which you want to generate prime numbers:"))

result = se(num)
```

#### - Prime Factors
```python
from moremath.algebra import prime_factors as pf

num = int(input("Enter the number whose prime factors you want to find:"))

result = pf(num)
```

## Arithmetic
This deals with **addition**, **subtraction**, **multiplication**, **division**, **factorial**.

### Examples
#### - Addition
```python
from moremath.arithmetic import add

num1 = input("Enter first number:")
num2 = input("Enter second number:")

result = add(num1, num2)
```

#### - Subtraction
```python
from moremath.arithmetic import subtract

num1 = input("Enter first number:")
num2 = input("Enter second number:")

result = subtract(num1, num2)
```

#### - Multiplication
```python
from moremath.arithmetic import multiply

num1 = input("Enter first number:")
num2 = input("Enter second number:")

result = multiply(num1, num2)
```

#### - Division
```python
from moremath.arithmetic import divide

num1 = input("Enter dividend:")
num2 = input("Enter divisor:")

result = divide(num1, num2)
```

#### - Factorial
```python
from moremath.arithmetic import factorial

num = input("Enter number:")

result = factorial(num)
```

## Geometry
This deals with **perimeter**, **area**, **volume**, **surface area**.

### Examples
#### - Square Perimeter
```python
from moremath.geometry import square_perimeter as sp

side = input("Enter side length:")

result = sp(side)
```

#### - Square Area
```python
from moremath.geometry import square_area as sa

side = input("Enter side length:")

result = sa(side)
```

#### - Rectangle Perimeter
```python
from moremath.geometry import rectangle_perimeter as rp

l = input("Enter length:")
b = input("Enter breadth:")

result = rp(l, b)
```

#### - Rectangle Area
```python
from moremath.geometry import rectangle_area as ra

l = input("Enter length:")
b = input("Enter breadth:")

result = ra(l, b)
```

#### - Circumference / Circle Perimeter
```python
from moremath.geometry import circle_perimeter as cp

r = input("Enter radius:")

result = cp(r)
```

#### - Circle Area
```python
from moremath.geometry import circle_area as ca

r = input("Enter radius:")

result = ca(r)
```

#### - Cube Volume
```python
from moremath.geometry import cube_volume as cv

a = input("Enter side:")

result = cv(a)
```

#### - Cube Surface Area
```python
from moremath.geometry import cube_surface_area as csa

a = input("Enter side:")

result = csa(a)
```

#### - Sphere Volume
```python
from moremath.geometry import sphere_volume as sv

r = input("Enter radius:")

result = sv(r)
```

#### - Sphere Surface Area
```python
from moremath.geometry import sphere_surface_area as ssa

r = input("Enter radius:")

result = ssa(r)
```

## Statistics
This deals with **mean**, **median**, **mode**, **variance**, **standard deviation**.

### Examples
#### - Mean
```python
from moremath.statistics import mean

data = [1, 3, 3, 6, 3, 7]
result = mean(data)
```

#### - Median
```python
from moremath.statistics import median

data = [1, 3, 3, 6, 3, 7]
result = median(data)
```

#### - Mode
```python
from moremath.statistics import mode

data = [1, 3, 3, 6, 3, 7]
result = mode(data)
```

#### - Variance
```python
from moremath.statistics import variance

data = [1, 3, 3, 6, 3, 7]
result = variance(data)
```

#### - Standard Deviation
```python
from moremath.statistics import standard_deviation as sd

data = [1, 3, 3, 6, 3, 7]
result = sd(data)
```
