# You have a bucket with 3 red balls and 3 green balls.
# Assume that once you draw a ball out of the bucket, you don't replace it.
# What is the probability of drawing 3 balls of the same color?

# Write a Monte Carlo simulation to solve the above problem.
# Feel free to write a helper function if you wish.

import random


def no_replacement_simulation(num_trials):
    """
    Runs num_trials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. 
    Balls are not replaced once
    drawn. 
    Returns a decimal - the fraction of times 3 
    balls of the same color were drawn.
    """

    def ball_draws(bucket):
        """
        Draws 3 balls from a bucket at random without replacing each time.
        Returns true if all the same colour, false otherwise.
        """
        draws = []
        draws.append(bucket.pop())

        for i in range(2):
            # ball = bucket.pop()
            # draws.append(ball)
            random.shuffle(bucket)
            draws.append(bucket.pop())

        if draws[0] == draws[1] == draws[2]:
            return True
        else:
            return False

    count_true, count_false, trials = 0, 0, 0

    while trials < num_trials:

        trials += 1
        bucket = ["R", "G", "R", "G", "R", "G"]
        random.shuffle(bucket)

        if ball_draws(bucket):
            count_true += 1
        else:
            count_false += 1

    return float(count_true/num_trials)


random.seed(0)
print(no_replacement_simulation(1000000))
