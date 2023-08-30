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


def make_hist(data, title, xlabel, ylabel, bins=20):
    pylab.hist(data, bins=bins)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)


def get_highs():
    in_file = open('temperatures.csv')
    population = []
    for l in in_file:
        try:
            tempC = float(l.split(',')[1])
            population.append(tempC)
        except:
            continue
    return population


def get_means_and_sds(population, sample, verbose=False):
    pop_mean = sum(population)/len(population)
    samples_mean = sum(sample)/len(sample)
    if verbose:
        make_hist(population,
                  'Daily High 1961-2015, Population\n' +
                  '(mean = ' + str(round(pop_mean, 2)) + ')',
                  'Degrees C', 'Number Days')
        pylab.figure()
        make_hist(sample, 'Daily High 1961-2015, Sample\n' +
                  '(mean = ' + str(round(samples_mean, 2)) + ')',
                  'Degrees C', 'Number Days')
        print('Population mean =', pop_mean)
        print('Standard deviation of population =',
              numpy.std(population))
        print('Sample mean =', samples_mean)
        print('Standard deviation of sample =',
              numpy.std(sample))
    return pop_mean, samples_mean,\
        numpy.std(population), numpy.std(sample)


random.seed(0)
population = get_highs()
sample = random.sample(population, 100)
get_means_and_sds(population, sample, True)
