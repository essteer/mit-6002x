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


# fit_data('springData.txt')


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
#
# parameters for generating data
# xVals = range(-50, 51, 5)
# a, b, c = 3.0, 0.0, 0.0
# frac_outlier = 0.00
#
# generate data
# random.seed(0)
# yVals = gen_parabolic_data(a, b, c, xVals, frac_outlier)
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

#
# Compare models
# def ave_mean_squared_error(data, predicted):
#    error = 0.0
#    for i in range(len(data)):
#        error += (data[i] - predicted[i])**2
#    return error/len(data)

# est_yVals = pylab.polyval(model1, xVals)
# print('Ave. mean square error for linear model =',
#      ave_mean_squared_error(yVals, est_yVals))
# est_yVals = pylab.polyval(model2, xVals)
# print('Ave. mean square error for quadratic model =',
#      ave_mean_squared_error(yVals, est_yVals))


def r_squared(observed, predicted):
    error = ((predicted - observed)**2).sum()
    mean_error = error/len(observed)
    return 1 - (mean_error/numpy.var(observed))


def gen_fits(xVals, yVals, degrees):
    models = []
    for d in degrees:
        model = pylab.polyfit(xVals, yVals, d)
        models.append(model)
    return models


def test_fits(models, degrees, xVals, yVals, title):
    pylab.plot(xVals, yVals, 'o', label='Data')
    for i in range(len(models)):
        est_yVals = pylab.polyval(models[i], xVals)
        error = r_squared(yVals, est_yVals)
        pylab.plot(xVals, est_yVals,
                   label='Fit of degree '
                   + str(degrees[i])
                   + ', R2 = ' + str(round(error, 5)))
    pylab.legend(loc='best')
    pylab.title(title)


xVals, yVals = get_data('mysteryData.txt')
# degrees = (1, 2)
# models = gen_fits(xVals, yVals, degrees)
# test_fits(models, degrees, xVals, yVals, 'Mystery Data')

# Compare higher-order fits
degrees = (2, 4, 8, 16)
models = gen_fits(xVals, yVals, degrees)
test_fits(models, degrees, xVals, yVals, 'Mystery Data')


# def gen_parabolic_data(a, b, c, xVals, frac_outliers):
#    yVals = []
#    for x in xVals:
#        theoretical_val = a*x**2 + b*x + c
#        if random.random() > frac_outliers:
#            yVals.append(theoretical_val\
#            + random.gauss(0, 35))
#        else: #generate outlier
#            yVals.append(theoretical_val\
#            + random.gauss(0, theoretical_val*2))
#    f = open('mystery.txt','w')
#    f.write('x        y\n')
#    for i in range(len(yVals)):
#        f.write(str(yVals[i]) + ' ' + str(xVals[i]) + '\n')
#    f.close()
#    return yVals
#
# parameters for generating data
# xVals = range(-10, 11, 1)
# a, b, c = 3.0, 0.0, 0.0
# frac_outlier = 0.00
#
# generate data
# random.seed(0)
# yVals = gen_parabolic_data(a, b, c, xVals, frac_outlier)
