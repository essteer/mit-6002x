# Polynomial

Use linear regression to find a polynomial - then use the polynomial to solve for least squares.

**Polynomials with one variable (x)**

- 0 or sum of finite number of non-zero terms.
- Each term of the form cx^p
  - c, the coefficient, a real number; and
  - p, the degree of the term, a non-negative integer.
- The degree of the polynomial is the largest degree of any term.

Examples:

1. Line: ax + b
2. Parabola: ax^2 + bx + c (quadratic polynomial)

**Solving for least squares**

For our example, since we want a line, we will use a degree-one polynomial as a model of our data:

- y = ax + b
- a = slope of the line
- b = y intercept

Our goal is to find values of _a_ and _b_ such that when we use the polynomial to compute y values for all of the _x_ values in our experiment, the squared differences of these values and the corresponding observed values is minimised.

- This is a linear regression problem.
- There are many algorithms for doing this, including one similar to Newton's method (Newton-Raphson).

## PolyFit

- pylab.polyfit(observed_x, observed_y, n)
- Finds coefficients of a polynomial of degree n, that provides a best least squares fit for the observed data.

A call to pylab.polyfit(observed*x, observed_u, 1) returns a tuple with two floating-point values, \_a* and _b_
.
A call to pylab.polyfit(observed*x, observed_u, 2) returns a tuple with three floating-point values, \_a*, _b_, and _c_.

**Note on k**

_a_ is equal to change in (delta) distance divided by the change in force:

- _a_ = delta distance / delta force

The spring constant is delta force / delta distance

- _k_ = delta force / delta distance

_k_ is therefore the inverse of _a_, so we can obtain _k_ through 1/_a_.
