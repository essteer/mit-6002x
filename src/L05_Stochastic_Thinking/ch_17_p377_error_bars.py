import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate


def variance(X):
    """Assumes that X is a list of numbers.
       Returns the variance of X"""
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return tot/len(X)


def std_dev(X):
    """Assumes that X is a list of numbers.
       Returns the standard deviation of X"""
    return variance(X)**0.5


def flip(num_flips):
    """Assumes num_flips a positive int"""
    heads = 0
    for i in range(num_flips):
        if random.choice(("H", "T")) == "H":
            heads += 1
    return heads/num_flips


def flip_sim(num_flips_per_trial, num_trials):
    frac_heads = []
    for i in range(num_trials):
        frac_heads.append(flip(num_flips_per_trial))
    mean = sum(frac_heads)/len(frac_heads)
    sd = std_dev(frac_heads)
    return (frac_heads, mean, sd)


def show_error_bars(min_exp, max_exp, num_trials):
    """Assumes min_exp and max_exp positive ints; min_exp < max_exp
       num_trials a positive integer
       Plots mean fraction of heads with error bars"""
    means, sds, x_vals = [], [], []
    for exp in range(min_exp, max_exp + 1):
        x_vals.append(2**exp)
        frac_heads, mean, sd = flip_sim(2**exp, num_trials)
        means.append(mean)
        sds.append(sd)
    plt.errorbar(x_vals, means, yerr=1.96*np.array(sds))
    plt.semilogx()
    plt.title("Mean Fraction of Heads (" + str(num_trials) + " trials)")
    plt.xlabel("Number of flips per trial")
    plt.ylabel("Fraction of heads & 95% confidence")


show_error_bars(3, 10, 100)
