import random
import numpy as np


def roll_die():
    return random.choice([1, 2, 3, 4, 5, 6])


def check_pascal(num_trials, rolls_per_trial):
    """Assumes num_trials is an int > 0
       Prints an estimate of the probability of winning"""
    num_wins = 0
    for i in range(num_trials):
        for j in range(rolls_per_trial):
            d1 = roll_die()
            d2 = roll_die()
            if d1 == 6 and d2 == 6:
                num_wins += 1
                break
    print("Probability of winning =", num_wins/num_trials)


rolls_per_trial = 24

check_pascal(1000000, rolls_per_trial)
