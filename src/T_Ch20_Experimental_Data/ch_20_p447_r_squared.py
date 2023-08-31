# -*- coding: utf-8 -*-
import random
import numpy as np
import matplotlib.pyplot as plt
import scipy


def get_trajectory_data(file_name):
    distances = []
    heights1, heights2, heights3, heights4 = [], [], [], []
    with open(file_name, 'r') as data_file:
        data_file.readline()
        for line in data_file:
            d, h1, h2, h3, h4 = line.split(',')
            distances.append(float(d))
            heights1.append(float(h1))
            heights2.append(float(h2))
            heights3.append(float(h3))
            heights4.append(float(h4))
    return (distances, [heights1, heights2, heights3, heights4])


def process_trajectories(file_name):
    distances, heights = get_trajectory_data(file_name)
    num_trials = len(heights)
    distances = np.array(distances)
    # Get array containing mean height at each distance
    tot_heights = np.array([0]*len(distances))
    for h in heights:
        tot_heights = tot_heights + np.array(h)
    mean_heights = tot_heights/len(heights)
    plt.title('Trajectory of Projectile (Mean of '
              + str(num_trials) + ' Trials)')
    plt.xlabel('Inches from Launch Point')
    plt.ylabel('Inches above Launch Point')
    plt.plot(distances, mean_heights, 'ro')
    fit = np.polyfit(distances, mean_heights, 1)
    altitudes = np.polyval(fit, distances)
    plt.plot(distances, altitudes, 'b', label='Linear Fit')
    print('r**2 of linear fit =', r_squared(mean_heights, altitudes))
    fit = np.polyfit(distances, mean_heights, 2)
    altitudes = np.polyval(fit, distances)
    plt.plot(distances, altitudes, 'b:', label='Quadratic Fit')
    print('r**2 of quadratic fit =', r_squared(mean_heights, altitudes))
    plt.legend()


def r_squared(measured, predicted):
    """Assumes measured a one-dimensional array of measured values
               predicted a one-dimensional array of predicted values
       Returns coefficient of determination"""
    estimated_error = ((predicted - measured)**2).sum()
    mean_of_measured = measured.sum()/len(measured)
    variability = ((measured - mean_of_measured)**2).sum()
    return 1 - estimated_error/variability


process_trajectories('launcherData.csv')
