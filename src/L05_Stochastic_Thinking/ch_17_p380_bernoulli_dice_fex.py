import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
import math

# test = math.comb(10, 2) * (1/6)**2 * (5/6)**8
# print(
#     f"The probability of rolling exactly two 3's out of 10 rolls is {round(test, 4)}")
# print("")


def bernoulli_dice(k=2):
    """Calculates the probability of rolling exactly two 3's
        in k rolls of a fair die"""
    return math.comb(k, 2) * (1/6)**2 * (5/6)**(k-2)


# print(bernoulli_dice(20))

def bernoulli_plot(min_k, max_k):
    """
    min_k and max_k are ints
    calls bernoulli_dice() for the range(min_k, max_k + 1)
    plots a chart of the probabilities of rolling two 3s in k rolls of a fair die
    """
    probs, k_vals = [], []

    for k in range(min_k, max_k + 1):
        k_vals.append(k)
        probs.append(bernoulli_dice(k))

    plt.figure()
    plt.clf()
    plt.plot(k_vals, probs, 'r--', label='probability', linewidth=2.0)
    plt.xlabel("Number of Dice Rolls")
    plt.ylabel("Probability of Success")
    plt.legend()
    plt.title(
        f"Probability of Rolling Exactly Two 3s in {min_k} to {max_k} Dice Rolls")


bernoulli_plot(2, 50)
