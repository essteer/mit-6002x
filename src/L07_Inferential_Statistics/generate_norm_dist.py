import scipy.integrate
import random
import pylab

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
# set numpoints for legend
pylab.rcParams['legend.numpoints'] = 1

dist = []
for i in range(100000):
    dist.append(random.gauss(0, 30))
pylab.hist(dist, 30)


def gaussian(x, mu, sigma):
    # return 37 # removing the gaussian quality of the data by fixing the result
    factor1 = (1.0/(sigma*((2*pylab.pi)**0.5)))
    factor2 = pylab.e**-(((x-mu)**2)/(2*sigma**2))

    return factor1*factor2


def check_empirical(num_trials):
    for t in range(num_trials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print('For mu =', mu, 'and sigma =', sigma)
        for num_st_dev in (1, 1.96, 3):
            # prints the integral from -2 to +2, of a norm dist with mean 0 and std dev 1
            # this could be changed if desired
            area = scipy.integrate.quad(gaussian,
                                        mu-num_st_dev*sigma,
                                        mu+num_st_dev*sigma,
                                        (mu, sigma))[0]
            print('  Fraction within', num_st_dev, 'std =', round(area, 4))


check_empirical(3)
