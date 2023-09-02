# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Z-scaling
# Each feature has a mean of 0 and standard deviation of 1


def z_scale_features(vals):
    """
    Assumes vals is a sequence of floats
    """
    result = np.array(vals)
    mean = float(sum(result)) / len(result)
    result = result - mean
    return result / np.std(result)


# Interpolation
# Map minimum value to 0, maximum value to 1, and linearly interpolate everything inbetween
def i_scale_features(vals):
    """
    Assumes vals is a sequence of floats
    """
    min_val, max_val = min(vals), max(vals)
    fit = plt.polyfit([min_val, max_val], [0, 1], 1)
    return plt.polyval(fit, vals)
