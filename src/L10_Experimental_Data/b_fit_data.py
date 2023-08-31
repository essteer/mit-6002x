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


def fit_data(file_name):
    xVals, yVals = get_data(file_name)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81  # get force
    pylab.plot(xVals, yVals, 'bo',
               label='Measured points')
    label_plot()
    a, b = pylab.polyfit(xVals, yVals, 1)
    est_yVals = a*xVals + b
    print('a =', a, 'b =', b)
    pylab.plot(xVals, est_yVals, 'r',
               label='Linear fit, k = '
               + str(round(1/a, 5)))
    pylab.legend(loc='best')


fit_data('springData.txt')


# fit_data1 is another version of fit_data, this time using polyval
def fit_data1(file_name):
    xVals, yVals = get_data(file_name)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81  # get force
    pylab.plot(xVals, yVals, 'bo',
               label='Measured points')
    label_plot()

    # polyval makes the code independent of the degree of the polynomial
    # so the same code can be called with polynomials of different degrees
    model = pylab.polyfit(xVals, yVals, 1)
    est_yVals = pylab.polyval(model, xVals)

    pylab.plot(xVals, est_yVals, 'r',
               label='Linear fit, k = '
               + str(round(1/model[0], 5)))
    pylab.legend(loc='best')

# fit_data1('springData.txt')

# def gen_parabolic_data(a, b, c, xVals, frac_outliers):
#    yVals = []
#    for x in xVals:
#        theoreticalVal = a*x**2 + b*x + c
#        if random.random() > frac_outliers:
#            yVals.append(theoreticalVal\
#            + random.gauss(0, 1000))
#        else: #generate outlier
#            yVals.append(theoreticalVal\
#            + random.gauss(0, theoreticalVal*2))
#    return yVals
#
# parameters for generating data
# xVals = range(-50, 51, 5)
# a, b, c = 3.0, 0.0, 0.0
# fracOutlier = 0.00
#
# generate data
# random.seed(0)
# yVals = gen_parabolic_data(a, b, c, xVals, fracOutlier)
# pylab.plot(xVals, yVals, 'o', label = 'Data Points')
# pylab.title('Mystery Data')
#
# Try linear model
# model1 = pylab.polyfit(xVals, yVals, 1)
# pylab.plot(xVals, pylab.polyval(model1, xVals),
#           label = 'Linear Model')
#
# Try a quadratic model
# model2 = pylab.polyfit(xVals, yVals, 2)
# pylab.plot(xVals, pylab.polyval(model2, xVals),
#           'r--', label = 'Quadratic Model')
# pylab.legend()
