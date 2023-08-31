# -*- coding: utf-8 -*-
import random
import pylab
import numpy

# set line width
pylab.rcParams['lines.linewidth'] = 4
# set font size for titles
pylab.rcParams['axes.titlesize'] = 20
# set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
# set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
# set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
# set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
# set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
# set size of markers
pylab.rcParams['lines.markersize'] = 10
# set number of examples shown in legends
pylab.rcParams['legend.numpoints'] = 1


def get_data(file_name):
    data_file = open(file_name, 'r')
    distances = []
    masses = []
    data_file.readline()  # discard header
    for line in data_file:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    data_file.close()
    return (masses, distances)


def label_plot():
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')


def plot_data(file_name):
    xVals, yVals = get_data(file_name)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81  # acc. due to gravity
    pylab.plot(xVals, yVals, 'bo',
               label='Measured displacements')
    label_plot()


plot_data('springData.txt')
