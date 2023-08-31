# -*- coding: utf-8 -*-
import random
import numpy as np
import matplotlib.pyplot as plt
import scipy


def get_data(input_file):
    with open(input_file, 'r') as data_file:
        distances = []
        masses = []
        data_file.readline()  # ignore header
        for line in data_file:
            d, m = line.split()
            distances.append(float(d))
            masses.append(float(m))
    return (masses, distances)


def plot_data(input_file):
    masses, distances = get_data(input_file)
    distances = np.array(distances)
    masses = np.array(masses)
    forces = masses*9.81
    plt.plot(forces, distances, 'bo', label='Measured displacements')
    plt.title('Measured Displacement of Spring')
    plt.xlabel('|Force| (Newtons)')
    plt.ylabel('Distance (metres')

# plot_data('springData.txt')


def fit_data(input_file):
    masses, distances = get_data(input_file)
    distances = np.array(distances)
    forces = np.array(masses)*9.81
    new_forces = np.append(forces, np.array([1.5*9.81]))
    plt.plot(forces, distances, 'ko',
             label='Measured displacements')
    plt.title('Measured Displacement of Spring')
    plt.xlabel('|Force| (Newtons)')
    plt.ylabel('Distance (meters)')

    # find linear fit
    a, b = np.polyfit(forces, distances, 1)
    predicted_distances = a*np.array(new_forces) + b
    k = 1.0/a  # see explanation in text
    plt.plot(new_forces, predicted_distances,
             label='Linear fit, k = ' + str(round(k, 5)))

    # find cubic fit
    fit = np.polyfit(forces, distances, 3)
    predicted_distances = np.polyval(fit, new_forces)
    plt.plot(new_forces, predicted_distances, 'k:', label='cubic fit')
    plt.legend(loc='best')


fit_data('springData.txt')
