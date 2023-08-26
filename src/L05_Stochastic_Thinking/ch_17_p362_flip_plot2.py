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


def make_plot(x_vals, y_vals, title, x_label, y_label, style, log_x=False, log_y=False):
    plt.figure()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x_vals, y_vals, style)
    if log_x:
        plt.semilogx()
    if log_y:
        plt.semilogy()


def run_trial(num_flips):
    num_heads = 0
    for n in range(num_flips):
        if random.choice(("H", "T")) == "H":
            num_heads += 1
    num_tails = num_flips - num_heads
    return (num_heads, num_tails)


def CV(X):
    mean = sum(X)/len(X)
    try:
        return std_dev(X)/mean
    except ZeroDivisionError:
        return float("nan")


def flip_plot2(min_exp, max_exp, num_trials):
    """Assumes min_exp, max_exp, num_trials ints >0; min_exp < max_exp
       Plots summaries of results of num_trials trials of
       2**min_exp to 2**max_exp coin flips"""
    ratios_means, diffs_means, ratios_SDs, diffs_SDs = [], [], [], []
    ratios_CVs, diffs_CVs, x_axis = [], [], []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2**exp)
    for num_flips in x_axis:
        ratios, diffs = [], []
        for t in range(num_trials):
            num_heads, num_tails = run_trial(num_flips)
            ratios.append(num_heads/num_tails)
            diffs.append(abs(num_heads - num_tails))
        ratios_means.append(sum(ratios)/num_trials)
        diffs_means.append(sum(diffs)/num_trials)
        ratios_SDs.append(std_dev(ratios))
        diffs_SDs.append(std_dev(diffs))
        ratios_CVs.append(CV(ratios))
        diffs_CVs.append(CV(diffs))
    num_trials_str = " (" + str(num_trials) + " Trials)"
    title = f"Mean Heads/Tails Ratios ({num_trials} Trials)"
    make_plot(x_axis, ratios_means, title, "Number of Flips",
              "Mean Heads/Tails", "ko", log_x=True)
    title = "SD Heads/Tails Ratios" + num_trials_str
    make_plot(x_axis, ratios_SDs, title, "Number of Flips",
              "Standard Deviation", "ko", log_x=True, log_y=True)

    title = "Mean abs(#Heads - #Tails)" + num_trials_str
    make_plot(x_axis, diffs_means, title, "Number of Flips",
              "Mean abs(#Heads - #Tails)", "ko", log_x=True, log_y=True)
    title = "SD abs(#Heads - #Tails)" + num_trials_str
    make_plot(x_axis, diffs_SDs, title, "Number of Flips",
              "Standard Deviation", "ko", log_x=True, log_y=True)

    title = "Coeff. of Var. abs(#Heads - #Tails)" + num_trials_str
    make_plot(x_axis, diffs_CVs, title, "Number of Flips",
              "Coeff. of Var.", "ko", log_x=True)
    title = "Coeff. of Var. Heads/Tails Ratio" + num_trials_str
    make_plot(x_axis, ratios_CVs, title, "Number of Flips",
              "Coeff. of Var.", "ko", log_x=True, log_y=True)


flip_plot2(4, 20, 20)
