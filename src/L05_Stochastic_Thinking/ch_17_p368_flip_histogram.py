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


def label_plot(num_flips, num_trials, mean, sd):
    plt.title(str(num_trials) + " trials of " + str(num_flips) + " flips each")
    plt.xlabel("Fraction of Heads")
    plt.ylabel("Number of Trials")
    plt.annotate("Mean = " + str(round(mean, 4)) + "\nSD = " + str(round(sd, 4)),
                 size="x-large", xycoords="axes fraction", xy=(0.67, 0.5))


def make_plots(num_flips1, num_flips2, num_trials):
    val1, mean1, sd1 = flip_sim(num_flips1, num_trials)
    plt.hist(val1, bins=20)
    x_min, x_max = plt.xlim()
    label_plot(num_flips1, num_trials, mean1, sd1)
    plt.figure()
    val2, mean2, sd2 = flip_sim(num_flips2, num_trials)
    plt.hist(val2, bins=20, ec="k")
    plt.xlim(x_min, x_max)
    label_plot(num_flips2, num_trials, mean2, sd2)


make_plots(100, 1000, 100000)
