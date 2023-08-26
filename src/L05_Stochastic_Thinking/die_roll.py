# An example of nondeterminism with die rolls

import random


def roll_die():
    """returns a random in between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6])


def test_roll(n=10):
    """
    n, an int
    calls the roll_die() function n number of times
    prints the result of each call to roll_die()
    """
    result = ""
    for i in range(n):
        result = result + str(roll_die())
    print(result)


# test_roll()

# The use of a predetermined random.seed(0) means the below function is not stochastic!
random.seed(0)


def run_sim(goal, numTrials):
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(roll_die())
        if result == goal:
            total += 1
    print('Actual probability =',
          round(1/(6**len(goal)), 8))
    estProbability = round(total/numTrials, 8)
    print('Estimated Probability  =',
          round(estProbability, 8))

# runSim('11111', 1000) # unlikely to emerge within such a small sample size
# runSim('11111', 1000000) # more likely to appear here

# random.seed(0) (or another number) can be useful for debugging in certain circumstances.


def frac_double_sixes(num_tests):
    """
    num_tests, an int
    runs num_tests number of two calls to roll_die()
    returns a float 0 <= x <= 1 of the proportion of rolls that both result in sixes"""
    numBoxCars = 0.0
    for i in range(num_tests):
        if roll_die() == 6 and roll_die() == 6:
            numBoxCars += 1
    return numBoxCars/num_tests


print('Frequency of double 6 =',
      str(frac_double_sixes(100000)*100) + '%')
