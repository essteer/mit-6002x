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


def regress_to_mean(num_flips, num_trials):
    # Get fraction of heads for each trial of num_flips
    frac_heads = []
    for t in range(num_trials):
        frac_heads.append(flip(num_flips))
    # Find trials with extreme results and for each the next trial
    extremes, next_trials = [], []
    for i in range(len(frac_heads) - 1):
        if frac_heads[i] < 0.33 or frac_heads[i] > 0.66:
            extremes.append(frac_heads[i])
            next_trials.append(frac_heads[i+1])
    # Plot results
    plt.plot(range(len(extremes)), extremes, "ko", label="Extreme")
    plt.plot(range(len(next_trials)), next_trials, "k^", label="Next Trial")
    plt.axhline(0.5)
    plt.ylim(0, 1)
    plt.xlim(-1, len(extremes) + 1)
    plt.xlabel("Extreme Example and Next Trial")
    plt.ylabel("Fraction Heads")
    plt.title("Regression to the Mean")
    plt.legend(loc="best")


regress_to_mean(15, 50)
