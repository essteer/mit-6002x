import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate

print(scipy.integrate.quad(abs, 0, 5)[0])

# normal distribution can be generated easily with random.gauss(mu, sigma)


def gaussian(x, mu, sigma):
    """assumes x, mu, sigma numbers
       returns the value of P(x) for a Gaussian
       with mean mu and sd sigma"""
    factor1 = (1.0/(sigma*((2*np.pi)**0.5)))
    factor2 = np.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2


# scipy.integrate.quad has three required parameters, and one optional parameter:
# - a function or method to be integrated
# - a number representing the lower limit of the integration
# - a number representing the upper limit of the integration
# - an optional tuple supplying values for all arguments, except the first, of the function to be integrated

# the quad function returns a tuple of two floats
# the first float approximates the value of the integral
# the second float estimates the absolute error in the result

def check_empirical(mu_max, sigma_max, num_trials):
    """assumes mu_max, sigma_max, num_trials positive ints
       prints fraction of values of a Gaussians (with randomly
       chosen mu and sigman) falling within 1, 2, 3 standard
       deviations"""
    for t in range(num_trials):
        mu = random.randint(-mu_max, mu_max + 1)
        sigma = random.randint(1, sigma_max)
        print("For mu =", mu, "and sigma =", sigma)
        for num_std in (1, 2, 3):
            area = scipy.integrate.quad(
                gaussian, mu-num_std*sigma, mu+num_std*sigma, (mu, sigma))[0]
            print(" Fraction within", num_std, "std =", round(area, 4))


check_empirical(10, 10, 3)

print(
    f"Area between -1 and 1 for standard normal distribution is {round(scipy.integrate.quad(gaussian, -1, 1, (0, 1))[0], 4)}")
