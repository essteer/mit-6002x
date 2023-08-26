import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate


def clear(n, p, steps):
    """Assumes n & steps postive ints, p a float
       n: the initial number of molecules
       p: the probability of a molecule being cleared
       steps: the length of the simulation"""
    num_remaining = [n]
    for t in range(steps):
        num_remaining.append(n*((1-p)**t))
    plt.plot(num_remaining)
    plt.xlabel("Time")
    plt.ylabel("Molecules Remaining")
    plt.semilogy()  # enable for linear plot on y axis
    plt.title("Clearance of Drug")


clear(1000, 0.01, 1000)
