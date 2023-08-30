# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import random

# two-tailed one-sample test
num_games = 1273
lyndsay_wins = 666
outcomes = [1.0]*lyndsay_wins + [0.0]*(num_games - lyndsay_wins)
print("The p-value from a one-sample test is",
      scipy.stats.ttest_1samp(outcomes, 0.5)[1])

# Monte-Carlo simulation
num_games = 1273
lyndsay_wins = 666
num_trials = 10000
at_least = 0

for t in range(num_trials):
    l_wins, j_wins = 0, 0
    for g in range(num_games):
        if random.random() < 0.5:
            l_wins += 1
        else:
            j_wins += 1
    if l_wins >= lyndsay_wins or j_wins >= lyndsay_wins:
        at_least += 1

print("Probability of result at least this",
      "extreme by accident =", at_least/num_trials)
