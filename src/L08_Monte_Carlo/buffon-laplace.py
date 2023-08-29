import numpy
import random
import pylab
import math

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
# set size of markers, e.g., circles representing points
pylab.rcParams['lines.markersize'] = 10
# set number of times marker is shown when displaying legend
pylab.rcParams['legend.numpoints'] = 1


def throw_needles(num_needles):
    in_circle = 0
    for needles in range(1, num_needles + 1, 1):
        x = random.random()
        y = random.random()
        # Pythagorean theorem to compute hypotenuse of triangle with base x and height y
        # this is the distance from the tip of the needle to the origin
        if (x*x + y*y)**0.5 <= 1.0:
            # radius of circle is 1, so needle is only in circle if < 1.0
            in_circle += 1
    return 4*(in_circle/float(num_needles))


def get_estimate(num_needles, num_trials):
    estimates = []
    for t in range(num_trials):
        pi_guess = throw_needles(num_needles)
        estimates.append(pi_guess)
    std_dev = numpy.std(estimates)
    current_estimate = sum(estimates)/len(estimates)
    print('Est. = ' + str(current_estimate) +
          ', Std. dev. = ' + str(round(std_dev, 6))
          + ', Needles = ' + str(num_needles))
    return (current_estimate, std_dev)


def est_pi(precision, num_trials):
    num_needles = 1000
    std_dev = precision
    while std_dev >= precision/1.96:  # 95% of values within 1.96 std dev of mean
        current_estimate, std_dev = get_estimate(num_needles, num_trials)
        num_needles *= 2  # double size of simulation each time until good result reached
    return current_estimate


random.seed(0)
est_pi(0.005, 100)
