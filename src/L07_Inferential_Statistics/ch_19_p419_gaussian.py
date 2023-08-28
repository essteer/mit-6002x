import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate  # this failed when importing only scipy


def gaussian(x, mu, sigma):
    factor1 = (1/(sigma*((2*np.pi)**0.5)))
    factor2 = np.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2


area = round(scipy.integrate.quad(gaussian, -3, 3, (0, 1))[0], 4)
print('Probability of being within 3', 'of true mean of tight dist. =', area)

area = round(scipy.integrate.quad(gaussian, -3, 3, (0, 100))[0], 4)
print('Probability of being within 3', 'of true mean of wide dist. =', area)
