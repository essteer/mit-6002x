# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import random

random.seed(148)
treatment_dist = (119.5, 5.0)
control_dist = (120, 4.0)
sample_size = 100
treatment_times, control_times = [], []
for s in range(sample_size):
    treatment_times.append(random.gauss(treatment_dist[0],
                                        treatment_dist[1]))
    control_times.append(random.gauss(control_dist[0],
                                      control_dist[1]))

control_mean = round(sum(control_times)/len(control_times), 2)
treatment_mean = round(sum(treatment_times)/len(treatment_times), 2)
print("Treatment mean - control mean =",
      round(treatment_mean - control_mean, 2), "minutes")
two_sample_test = scipy.stats.ttest_ind(treatment_times,
                                        control_times,
                                        equal_var=False)
print("The t-statistic from two-sample test is",
      round(two_sample_test[0], 2))
print("The p-value from two-sample test is",
      round(two_sample_test[1], 2))

# Running the above code results in:
# Treatment mean - control mean = -1.38 minutes
# The t-statistic from two-sample test is -2.11
# The p-value from two-sample test is 0.04
