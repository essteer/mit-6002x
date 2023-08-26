import random
import numpy as np
import matplotlib.pyplot as plt
# import scipy.integrate


def flip(num_flips):
    """Assumes num_flips a positive int"""
    heads = 0
    for i in range(num_flips):
        if random.choice(("H", "T")) == "H":
            heads += 1
    return heads/num_flips


def flip_sim(num_flips_per_trial, num_trials):
    """Assumes num_flips_per_trial and num_trials positive ints"""
    frac_heads = []
    for i in range(num_trials):
        frac_heads.append(flip(num_flips_per_trial))
    mean = sum(frac_heads)/len(frac_heads)
    return mean


print(flip_sim(100, 1000))
