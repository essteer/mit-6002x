# -*- coding: utf-8 -*-
import random
import numpy as np
import matplotlib.pyplot as plt
import scipy
import math


def create_data(f, x_vals):
    """Assumes f is a function of one argument
                x_vals is an array of suitable arguments for f
       Returns array containing results of applying f to the
               elements of x_vals"""
    y_vals = []
    for i in x_vals:
        y_vals.append(f(x_vals[i]))
    return np.array(y_vals)


def fit_exp_data(x_vals, y_vals):
    """Assumes x_vals and y_vals arrays of numbers such that
        y_vals[i] == f(x_vals[i]), where f is an exponential function
       Returns a, b, base such that log(f(x), base) == ax + b"""
    log_vals = []
    for y in y_vals:
        log_vals.append(math.log(y, 2))  # get log base 2
    fit = np.polyfit(x_vals, log_vals, 1)
    return fit, 2


x_vals = range(10)
# f = lambda x: 3**x
def f(x): return 3**x


y_vals = create_data(f, x_vals)

plt.plot(x_vals, y_vals, 'ko', label="Actual values")
fit, base = fit_exp_data(x_vals, y_vals)
predictedy_vals = []

for x in x_vals:
    predictedy_vals.append(base**np.polyval(fit, x))
plt.plot(x_vals, predictedy_vals, label="Predicted values")
plt.title("Fitting an Exponential Function")
plt.legend(loc="upper left")

# Look at a value for x not in original data
print("f(20) =", f(20))
print("Predicted value =", int(base**(np.polyval(fit, [20]))))
