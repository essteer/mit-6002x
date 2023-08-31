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


plot_data('springData.txt')
