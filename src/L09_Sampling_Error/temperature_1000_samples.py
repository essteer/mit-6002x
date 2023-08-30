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
sample_size = 200
num_samples = 1000
max_mean_diff = 0
max_SD_diff = 0
sample_means = []

for i in range(num_samples):
    sample = random.sample(population, sample_size)
    pop_mean, sample_mean, pop_SD, sample_SD =\
        get_means_and_sds(population, sample, verbose=False)
    sample_means.append(sample_mean)
    if abs(pop_mean - sample_mean) > max_mean_diff:
        max_mean_diff = abs(pop_mean - sample_mean)
    if abs(pop_SD - sample_SD) > max_SD_diff:
        max_SD_diff = abs(pop_SD - sample_SD)
print('Mean of sample Means =',
      round(sum(sample_means)/len(sample_means), 3))
print('Standard deviation of sample means =',
      round(numpy.std(sample_means), 3))
print('Maximum difference in means =',
      round(max_mean_diff, 3))
print('Maximum difference in standard deviations =',
      round(max_SD_diff, 3))
make_hist(sample_means, 'Means of Samples', 'Mean', 'Frequency')
# axvline draws a vertical line in red (due to color="r")
pylab.axvline(x=pop_mean, color='r')


def show_error_bars(population, sizes, num_trials):
    xVals = []
    size_means, size_SDs = [], []
    for sample_size in sizes:
        xVals.append(sample_size)
        trial_means = []
        for t in range(num_trials):
            sample = random.sample(population, sample_size)
            pop_mean, sample_mean, pop_SD, sample_SD =\
                get_means_and_sds(population, sample)
            trial_means.append(sample_mean)
        size_means.append(sum(trial_means)/len(trial_means))
        size_SDs.append(numpy.std(trial_means))
    pylab.errorbar(xVals, size_means,
                   yerr=1.96*pylab.array(size_SDs), fmt='o',
                   label='95% Confidence Interval')
    pylab.title('Mean Temperature ('
                + str(num_trials) + ' trials)')
    pylab.xlabel('Sample Size')
    pylab.ylabel('Mean')
    pylab.axhline(y=pop_mean, color='r', label='Population Mean')
    pylab.xlim(0, sizes[-1] + 10)
    pylab.legend()
    pylab.figure()


# population = get_highs()
# show_error_bars(population, (50, 100, 200, 300, 400, 500, 600), 50)
