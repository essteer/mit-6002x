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


def r_squared(observed, predicted):
    error = ((predicted - observed)**2).sum()
    meanError = error/len(observed)
    return 1 - (meanError/numpy.var(observed))


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


# fitData('springData.txt')
random.seed(0)


class temp_datum(object):
    def __init__(self, s):
        info = s.split(',')
        self.high = float(info[1])
        self.year = int(info[2][0:4])

    def get_high(self):
        return self.high

    def get_year(self):
        return self.year


def get_temp_data():
    in_file = open('temperatures.csv')
    data = []
    in_file.readline()  # add readline to discard header data
    for l in in_file:
        data.append(temp_datum(l))
    return data


def get_yearly_means(data):
    years = {}
    for d in data:
        try:
            years[d.get_year()].append(d.get_high())
        except:
            years[d.get_year()] = [d.get_high()]
    for y in years:
        years[y] = sum(years[y])/len(years[y])
    return years


data = get_temp_data()
years = get_yearly_means(data)
xVals, yVals = [], []
for e in years:
    xVals.append(e)
    yVals.append(years[e])
pylab.plot(xVals, yVals)
pylab.xlabel('Year')
pylab.ylabel('Mean Daily High (C)')
pylab.title('Select U.S. Cities')


def split_data(xVals, yVals):
    # sampling indices of elements, rather than elements themselves
    # to ensure x and y values line up
    to_train = random.sample(range(len(xVals)),
                             len(xVals)//2)
    train_x, train_y, test_x, test_y = [], [], [], []
    for i in range(len(xVals)):
        if i in to_train:
            train_x.append(xVals[i])
            train_y.append(yVals[i])
        else:
            test_x.append(xVals[i])
            test_y.append(yVals[i])
    return train_x, train_y, test_x, test_y


# Cross-validation
num_subsets = 10
dimensions = (1, 2, 3)
r_squares = {}
for d in dimensions:
    r_squares[d] = []

for f in range(num_subsets):
    train_x, train_y, test_x, test_y = split_data(xVals, yVals)

    for d in dimensions:
        model = pylab.polyfit(train_x, train_y, d)
        est_yVals = pylab.polyval(model, train_x)
        est_yVals = pylab.polyval(model, test_x)
        r_squares[d].append(r_squared(test_y, est_yVals))
print('Mean R-squares for test data')

for d in dimensions:
    mean = round(sum(r_squares[d])/len(r_squares[d]), 4)
    sd = round(numpy.std(r_squares[d]), 4)
    print('For dimensionality', d, 'mean =', mean,
          'Std =', sd)
print(r_squares[1])
