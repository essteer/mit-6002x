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


def sem(pop_SD, sample_size):
    return pop_SD/sample_size**0.5

# sample_sizes = (25, 50, 100, 200, 300, 400, 500, 600)
# num_trials = 50
# population = get_highs()
# pop_SD = numpy.std(population)
# sems = []
# sample_SDs = []
# for size in sample_sizes:
#    sems.append(sem(pop_SD, size))
#    means = []
#    for t in range(num_trials):
#        sample = random.sample(population, size)
#        means.append(sum(sample)/len(sample))
#    sample_SDs.append(numpy.std(means))
# pylab.plot(sample_sizes, sample_SDs,
#           label = 'Std of 50 means')
# pylab.plot(sample_sizes, sems, 'r--', label = 'SEM')
# pylab.title('SEM vs. SD for 50 Means')
# pylab.legend()


def get_diffs(population, sample_sizes):
    pop_SD = numpy.std(population)
    diffs_fracs = []
    for sample_size in sample_sizes:
        diffs = []
        for t in range(100):
            sample = random.sample(population, sample_size)
            diffs.append(abs(pop_SD - numpy.std(sample)))
        diff_mean = sum(diffs)/len(diffs)
        diffs_fracs.append(diff_mean/pop_SD)
    return pylab.array(diffs_fracs)*100


def plot_diffs(sample_sizes, diffs, title, label):
    pylab.plot(sample_sizes, diffs, label=label)
    pylab.xlabel('Sample Size')
    pylab.ylabel('% Difference in SD')
    pylab.title(title)
    pylab.legend()

# sample_sizes = range(20, 600, 1)
# diffs = get_diffs(get_highs(), sample_sizes)
# plot_diffs(sample_sizes, diffs,
#          'Sample SD vs Population SD, Temperatures',
#          label = 'High temps')


def plot_distributions():
    uniform, normal, exp = [], [], []
    for i in range(100000):
        uniform.append(random.random())
        normal.append(random.gauss(0, 1))
        exp.append(random.expovariate(0.5))
    make_hist(uniform, 'Uniform', 'Value', 'Frequency')
    pylab.figure()
    make_hist(normal, 'Gaussian', 'Value', 'Frequency')
    pylab.figure()
    make_hist(exp, 'Exponential', 'Value', 'Frequency')

# plot_distributions()


def compare_dists():
    uniform, normal, exp = [], [], []
    for i in range(100000):
        uniform.append(random.random())
        normal.append(random.gauss(0, 1))
        exp.append(random.expovariate(0.5))
    sample_sizes = range(20, 600, 1)
    u_diffs = get_diffs(uniform, sample_sizes)
    n_diffs = get_diffs(normal, sample_sizes)
    e_diffs = get_diffs(exp, sample_sizes)
    plot_diffs(sample_sizes, u_diffs,
               'Sample SD vs Population SD',
               'Uniform population')
    plot_diffs(sample_sizes, n_diffs,
               'Sample SD vs Population SD',
               'Normal population')
    plot_diffs(sample_sizes, e_diffs,
               'Sample SD vs Population SD',
               'Exponential population')


compare_dists()
#
# pop_sizes = (10000, 100000, 1000000)
# sample_sizes = range(20, 600, 1)
# for size in pop_sizes:
#    population = []
#    for i in range(size):
#        population.append(random.expovariate(0.5))
#    e_diffs = get_diffs(population, sample_sizes)
#    plot_diffs(sample_sizes, e_diffs,
#              'Sample SD vs Population SD, Uniform',
#              'Population size = ' + str(size))
