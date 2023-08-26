# Exercise 5-2

# How would you randomly generate an even number x, 0 <= x < 100?
# Fill out the definition for the function genEven().
# Please generate a uniform distribution over the even numbers between 0 and 100 (not including 100).

import random


def gen_even():
    """
    Returns a random number x, where 0 <= x < 100
    """
    return random.randrange(0, 100, 2)


def test_gen_even(n=10):
    """
    n, an int
    calls the gen_even() function n number of times
    prints the result of each call to gen_even()
    """
    for i in range(n):
        print(gen_even())


test_gen_even(15)
