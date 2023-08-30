# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import random

# Finger exercise: An investigative reporter discovered that not only was Lyndsay employing
# dubious statistical methods, she was applying them to data she had merely made up.
# In fact, John had defeated Lyndsay 479 times and lost 443 times.
# At what level is this difference statistically significant?

# Using a significance level of α = 0.05, we accept the null hypothesis
# because the p-value is around 0.2359, well above α.
# To find the difference statistically significant, we would need to use
# a value of α as high as approximately 0.25, five times above the standard.

# two-tailed one-sample test
num_games = 479 + 443  # = 992
john_wins = 479
outcomes = [1.0]*john_wins + [0.0]*(num_games - john_wins)
print("The p-value from a one-sample test is",
      scipy.stats.ttest_1samp(outcomes, 0.5)[1])

# Monte-Carlo simulation
num_games = 479 + 443  # = 992
john_wins = 479
num_trials = 10000
at_least = 0

for t in range(num_trials):
    l_wins, j_wins = 0, 0
    for g in range(num_games):
        if random.random() < 0.5:
            l_wins += 1
        else:
            j_wins += 1
    if l_wins >= john_wins or j_wins >= john_wins:
        at_least += 1

print("Probability of result at least this",
      "extreme by accident =", at_least/num_trials)
