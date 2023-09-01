# -*- coding: utf-8 -*-
import random
import numpy as np
import matplotlib.pyplot as plt
import scipy

# If a function y = f(x) exhibits exponential growth,
# the log (to any base) of f(x) grows linearly.
# This can be visualised by plotting an exponential function
# with a logarithmic y-axis.

x_vals, y_vals = [], []
for i in range(10):
    x_vals.append(i)
    y_vals.append(3**i)
plt.plot(x_vals, y_vals, 'k')
plt.semilogy()
