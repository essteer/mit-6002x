import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate


def successful_starts(success_prob, num_trials):
    """Assumes success_prob is a float representing probability of a
       single attempt being successful. num_trials a positive int
       Returns a list of the number of attempts needed before a
       success for each trial."""
    tries_before_success = []
    for t in range(num_trials):
        consec_failures = 0
        while random.random() > success_prob:
            consec_failures += 1
        tries_before_success.append(consec_failures)
    return tries_before_success


prob_of_success = 0.5
num_trials = 5000
distribution = successful_starts(prob_of_success, num_trials)
plt.hist(distribution, bins=14)
plt.xlabel("Tries Before Success")
plt.ylabel("Number of Occurrences Out of " + str(num_trials))
plt.title("Probability of Starting Each Try = " + str(prob_of_success))
