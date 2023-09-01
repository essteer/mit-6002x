# -*- coding: utf-8 -*-
import random
import numpy as np
import matplotlib.pyplot as plt
import scipy

vals = []
for i in range(10):
    vals.append(3**i)
plt.plot(vals, 'ko', label="Actual points")
xVals = np.arange(10)
fit = np.polyfit(xVals, vals, 5)
y_vals = np.polyval(fit, xVals)
plt.plot(y_vals, 'kx', label="Predicted points",
         markeredgewidth=2, markersize=25)
plt.title("Fitting y = 3**x")
plt.legend(loc="upper left")

print("Model predicts that 3**20 is roughly", np.polyval(fit, [3**20])[0])
print("Actual value of 3**20 is", 3**20)
