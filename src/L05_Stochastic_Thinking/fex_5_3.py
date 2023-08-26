import random

# Exercise 5-3-1

# Write a deterministic program, deterministic_number, that returns an even number between 9 and 21.


def deterministic_number():
    """
    Deterministically generates and returns an even number between 9 and 21
    """
    return 14


# Exercise 5-3-2

# Write a uniformly distributed stochastic program, stochasticNumber, that returns an even number between 9 and 21.

def stochastic_number():
    """
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    """
    return random.randrange(10, 21, 2)
