# -*- coding: utf-8 -*-

# The notation P(A|B) stands for the probability of A being true
# under the assumption that B is true.
# It is often read as "the probability of A, given B."
# Therefore, the formula:
# P(male) * P(weight > 197 | male)
# expresses exactly the probability we are looking for.

# In general, if P(B) != 0:
# P(A|B) = P(A and B) / P(B)

import math
import scipy.stats
from statistics import NormalDist

# Estimate the probability that a randomly chosen American is both male
# and weighs more than 197 pounds. Assume that 50% of the population is male,
# and that the weights of the male population are normally distributed with
# a mean of 210 pounds and a standard deviation of 30 pounds.
# Hint: think about using the empirical rule.

# Empirical Rule
# - ~68% of data lies within 1 standard deviation of the mean.
# - ~95% of data lies within 2 standard deviations of the mean.
# - ~99.7% of data lies within 3 standard deviations of the mean.

# Simple working using the empirical rule:
# 210 - 30 = 180
# 180 < 197 < 210, therefore 197 is within 1 standard deviation
# 197 is therefore within ~68% of data
# 0.68 * 0.5 (prob of being male) = 0.34 = 34%
# This is close to the more precise values calculated by Python and SciPy.

p_male = 0.5
male_weight_mean = 210
male_weight_SD = 30  # 30lbs for 1 standard deviation
test_weight = 197


# Using Python's built-in statistics module:
# formula uses "1 - ..." because cdf gives probability x is lower than test_weight
python_calc = NormalDist(male_weight_mean, male_weight_SD).cdf(test_weight)
p_gt_test_weight = 1 - python_calc

p_male_gt_test_weight = p_gt_test_weight * p_male
answer = p_male_gt_test_weight

print("")
print("Calculation using Python's statistics.NormalDist:")
print(
    f"Probability a randomly chosen American is male & weighs > {test_weight}lbs:")
print(f"{(100*answer):.2f}%")


# Using SciPy's Stats module:
scipy_calc = scipy.stats.norm.cdf(197, 210, 30)
# this can also be written as:
# scipy.stats.norm(210, 30).cdf(197)
p_gt_test_weight = 1 - scipy_calc

p_male_gt_test_weight = p_gt_test_weight * p_male
answer = p_male_gt_test_weight

print("")
print("Calculation using SciPy's stats.norm.cdf:")
print(
    f"Probability a randomly chosen American is male & weighs > {test_weight}lbs:")
print(f"{(100*answer):.2f}%")


# Using a z-score table
z_score = (test_weight - male_weight_mean) / male_weight_SD
# = -13/30 = -0.4333
# z-score for -0.43 is 0.3336
z_score_m043 = 0.3336
# 1 - 0.3336 = 0.6664 = 67.64%
z_score_cdf = 1 - z_score_m043
# multiplied by 50% chance of being male = 0.3332 = 33.32% chance of being male and > 197.
z_score_prob = z_score_cdf * p_male
# 33.32% is not far from the library module results
answer = z_score_prob

print("")
print("Calculation using z-score table:")
print(
    f"Probability a randomly chosen American is male & weighs > {test_weight}lbs:")
print(f"{(100*answer):.2f}%")
