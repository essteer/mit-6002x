# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import random

# This program plots the mean p-value of 1,000 trials against
# the size of the samples used in those trials.

random.seed(0)
num_trials = 50
gaussian_1, gaussian_2 = [], []

# For each sample size and each trial, generate two samples:
# - both are drawn from a Gaussian with a standard deviation of 5
# - one has a mean of 100, the other a mean of 100.5
for _ in range(3100):
    gaussian_1.append(random.gauss(100, 5))
    gaussian_2.append(random.gauss(100.5, 5))

p_vals_means = []

for sample_size in range(50, 3040, 50):
    p_vals = []
    for t in range(num_trials):
        sample_1 = random.sample(gaussian_1, sample_size)
        sample_2 = random.sample(gaussian_2, sample_size)
        p_vals.append(scipy.stats.ttest_ind(sample_1, sample_2)[1])
    p_vals_means.append(sum(p_vals)/len(p_vals))

plt.plot(range(50, 3040, 50), p_vals_means, label='Mean p-value')
plt.ylabel('Mean p-value (500 trials)')
plt.xlabel('Sample Size')
plt.title('Gaussians with SD = 5, Means 100 & 100.5')
plt.axhline(0.05, color='r', linestyle='dashed', label='p = 0.05')
plt.axhline(0.01, linestyle=':', label='p = 0.01')
plt.yticks(np.arange(0, 1, 0.1))
plt.semilogy()
plt.legend()

# The mean p-value drop linearly with the sample size.
# The 0.5% difference in means becomes consistently statistically significant
# at the 5% level once the sample size reaches ~2,000, and
# at the 1% level once the sample size reaches ~3,000.
