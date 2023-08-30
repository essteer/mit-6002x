# -*- coding: utf-8 -*-
import random
import numpy as np
import matplotlib.pyplot as plt
import scipy

num_hyps = 50
sample_size = 200
population = []
for i in range(5000):  # Create large population
    population.append(random.gauss(0, 1))
sample1s, sample2s = [], []
# Generate many pairs of small samples
for i in range(num_hyps):
    sample1s.append(random.sample(population, sample_size))
    sample2s.append(random.sample(population, sample_size))
# Check pair for statistically significant difference
numSig = 0
for i in range(num_hyps):
    if scipy.stats.ttest_ind(sample1s[i], sample2s[i])[1] < 0.05:
        numSig += 1
print("# of statistically significantly different (p < 0.05) pairs =",
      numSig)
