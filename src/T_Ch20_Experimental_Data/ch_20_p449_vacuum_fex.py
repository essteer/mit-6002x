# -*- coding: utf-8 -*-
import numpy as np
from scipy.optimize import curve_fit

# In a vacuum, the speed of a falling object is defined by the equation
# v = v0 + gt, where
# v0 is the initial velocity of the object,
# t is the number of seconds the object has been falling, and
# g is the gravitational constant,
# roughly 9.81 m/sec2 on the surface of the Earth, and 3.711 m/sec2 on Mars.
#
# A scientist measures the velocity of a falling object on an unknown planet.
# She does this by measuring the downward velocity of an object at different points in time.
# At time 0, the object has an unknown velocity of v0.
# Implement a function that fits a model to the time and velocity data and estimates g for that planet and v0 for the experiment.
# It should return its estimates for g and v0, and also r-squared for the model.


def calculate_r_squared(measured, predicted):
    """Assumes measured a one-dimensional array of measured values
               predicted a one-dimensional array of predicted values
       Returns coefficient of determination"""
    estimated_error = ((predicted - measured)**2).sum()
    mean_of_measured = measured.sum()/len(measured)
    variability = ((measured - mean_of_measured)**2).sum()
    return 1 - estimated_error/variability


def falling_object_model(t, v0, g):
    return v0 + g * t


def estimate_parameters(t, v):
    # Fit the model to the data to estimate v0 and g
    params, covariance = curve_fit(falling_object_model, t, v)

    # Get the estimated values
    v0_estimated, g_estimated = params

    # Calculate R-squared
    r_squared = calculate_r_squared(v, falling_object_model(
        t, v0_estimated, g_estimated))

    return v0_estimated, g_estimated, r_squared


# Example usage:
t = np.array([0, 1, 2, 3, 4, 5])  # Time data in seconds
v = np.array([2.0, 5.5, 10.0, 15.7, 21.6, 27.7])  # Velocity data

v0_estimated, g_estimated, r_squared = estimate_parameters(t, v)

print("Estimated v0:", v0_estimated)
print("Estimated g:", g_estimated)
print("R-squared:", r_squared)
