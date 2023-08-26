import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate


def collision_prob(n, k):
    prob = 1.0
    for i in range(1, k):
        prob = prob * ((n - i) / n)
    return 1 - prob

# print(collision_prob(1000, 50))


def sim_insertions(num_indices, num_insertions):
    """Assumes num_indices and num_insertions are positive ints.
       Returns 1 if there is a collision; 0 otherwise."""
    choices = range(num_indices)  # list of possible indices
    used = []
    for i in range(num_insertions):
        hash_val = random.choice(choices)
        if hash_val in used:  # there is a collision
            return 1
        else:
            used.append(hash_val)
    return 0


def find_prob(num_indices, num_insertions, num_trials):
    collisions = 0
    for t in range(num_trials):
        collisions += sim_insertions(num_indices, num_insertions)
    return collisions/num_trials


print("Actual probability of a collision =", collision_prob(1000, 50))
print("Est. probability of a collision =", find_prob(1000, 50, 10000))
print("Actual probability of a collision =", collision_prob(1000, 200))
print("Est. probability of a collision =", find_prob(1000, 200, 10000))

# print(
#     f"Est. probability two people share the same birthday = {find_prob(365, 2, 1000000)}")
