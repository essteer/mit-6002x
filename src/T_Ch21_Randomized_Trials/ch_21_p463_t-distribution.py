# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

t_stat = -2.26  # t-statistic for PED-X example
t_dist = []
num_bins = 1000

for i in range(10000000):
    t_dist.append(np.random.standard_t(198))

plt.hist(t_dist, bins=num_bins,
         weights=np.array(len(t_dist)*[1.0])/len(t_dist))
plt.axvline(t_stat, color="w")
plt.axvline(-t_stat, color="w")
plt.title("T-distribution with 198 Degrees of Freedom")
plt.xlabel("T-Statistic")
plt.ylabel("Probability")

# The sum of the fractions of the area of the histogram to the left and right
# of the white lines equals the probability of getting a value at least
# as extreme as the observed value if:
# - the sample is representative of the population, and
# - the null hypothesis is true.

# The test should fail if the mean of the treatment group is either statistically
# statistically larger or smaller than the mean of the control group.
