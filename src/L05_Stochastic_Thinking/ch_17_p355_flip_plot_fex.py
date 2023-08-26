import random
import numpy as np
import matplotlib.pyplot as plt
# import scipy.integrate


def flip_plot(min_exp, max_exp):
    """Assumes min_exp and max_exp positive ints; min_exp < max_exp
       Plots results of 2**min_exp to 2**max_exp coin flips"""
    ratios, diffs, xAxis = [], [], []
    for exp in range(min_exp, max_exp + 1):
        xAxis.append(2**exp)
    for num_flips in xAxis:
        num_heads = 0
        for n in range(num_flips):
            if random.choice(("H", "T")) == "H":
                num_heads += 1
        num_tails = num_flips - num_heads
        try:
            ratios.append(num_heads / num_tails)
            diffs.append(abs(num_heads - num_tails))
        except ZeroDivisionError:
            continue
    plt.title("Difference Between Heads and Tails")
    plt.xlabel("Number of Flips")
    plt.ylabel("Abs(#Heads - #Tails)")
    plt.xticks(rotation="vertical")
    # Apply logarithmic scale to both x and y axes
    plt.xscale("log")
    plt.yscale("log")
    plt.plot(xAxis, diffs, "ko")
    plt.figure()
    plt.title("Heads/Tails Ratios")
    plt.xlabel("Number of Flips")
    plt.ylabel("#Heads/#Tails")
    plt.xticks(rotation="vertical")
    # Apply logarithmic scale to x axis only
    plt.xscale("log")
    plt.plot(xAxis, ratios, "ko")


# generate the same sequence of pseudorandom numbers with each execution
random.seed(0)
flip_plot(4, 20)
