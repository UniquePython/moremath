# moremath

## Introduction

This Python package, `moremath`, provides a collection of advanced mathematical functions covering various areas such as algebra, statistics, arithmetic, geometry, and factors.

## Installation

You can install `moremath` via pip:

```bash
pip install moremath
```

# Usage

## Algebra

```python
from moremath.algebra import exponentiation, logarithm

exp = exponentiation(2, 3)
log = logarithm(1000, 10)

print(exp) #Output: 8
print(log) #Output: 3
```

## Statistics

```python
from moremath.statistics import mean, median, mode

mean = mean([1, 2, 3, 4, 5])
median = median([1, 2, 3, 4, 5])
mode = mode([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

print(mean) #Output: 3.0
print(median) #Output: 3
print(mode) #Output: 4
```

## Arithmetic

```python
from moremath.arithmetic import add, subtract, multiply, divide, factorial

sum = add(1, 2)
difference = subtract(10, 5)
product = multiply(5, 10)
quotient = divide(100, 25)
fact = factorial(5)

print(sum) #Output: 3
print(difference) #Output: 5
print(product) #Output: 50
print(quotient) #Output: 4
print(fact) #Output: 120
```

## Geometry

```python
from moremath.geometry import square_perimeter, square_area, rectangle_perimeter, rectangle_area, circle_perimeter, circle_area, cube_volume, cube_surface_area, sphere_volume, sphere_surface_area

sp = square_perimeter(4)
sa = sqare_area(4)
rp = rectangle_perimeter(4, 5)
ra = rectangle_area(4, 5)
cp = circle_perimeter(4)
ca = circle_area(4)
cv = cube_volume(3)
csa = cube_surface_area(3)
sv = sphere_volume(3)
ssa = sphere_surface_area(3)

print(sp) #Output: 16
print(sa) #Output: 16
print(rp) #Output: 18
print(ra) #Output: 20
print(cp) #Output: 25.12.... (approximate; actual results may have more digits)
print(ca) #Output: 50.24.... (approximate; actual results may have more digits)
print(cv) #Output: 27
print(csa) #Output: 54
print(sv) #Output: 113.04 (approximate; actual results may have more digits)
print(ssa) #Output: 113.04 (approximate; actual results may have more digits)
```

## Factors

```python
from moremath.factors import prime_factors

p_factors = prime_factors(100)

print(p_factors) #Output: [2, 2, 5, 5]
```

# Updates
## Version 0.0.2
- Updated the README to include real life use cases

## Version 0.1.2
- Optimized the code for faster execution

# License

## Copyright (c) 2024-present Ananyo Bhattacharya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.**
