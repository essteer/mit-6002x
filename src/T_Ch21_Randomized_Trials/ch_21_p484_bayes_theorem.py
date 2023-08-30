# -*- coding: utf-8 -*-
import math
import scipy.stats
from statistics import NormalDist

# Bayes' Theorem:
# P(A|B) = (P(A) * P(B|A)) / P(B)

# Suppose that an asymptomatic woman in her forties goes for a mammogram and receives bad news:
# the mammogram is "positive".
# The probability a woman with breast cancer will get a true positive = 0.9.
# The probability a woman without breast cancer will get a false positive = 0.07.
p_true_pos = 0.9  # P(TP | canc) = 0.9
p_false_pos = 0.07  # P(FP | not canc) = 0.07
# The probability a woman in her forties has breast cancer is 0.008 (8/1000).
# The fraction who do not is therefore 0.992 (992/1000).
p_canc_40s = 0.008  # P(canc | woman in her 40s) = 0.008
p_not_canc_40s = 1 - p_canc_40s  # P(not canc | woman in her 40s) = 0.992

p_pos_test = (p_true_pos * p_canc_40s) + (p_false_pos * p_not_canc_40s)
print(f"Probability of a positive test = {100*p_pos_test:.2f}%.")

p_canc_given_pos = (p_canc_40s * p_true_pos) / \
    ((p_canc_40s * p_true_pos) + (p_not_canc_40s * p_false_pos))
print(
    f"Probability of cancer given a positive test = {100*p_canc_given_pos:.2f}%.")

print(
    f"Probability of not having cancer given a positive test = {100*(1 - p_canc_given_pos):.2f}%.")

# Probability of a positive test = 7.66%.
# Probability of cancer given a positive test = 9.39%.
# Probability of not having cancer given a positive test = 90.61%.

# This passes the sense check - since if 7% of women without cancer will have a false positive:
# 992 * 0.07 = 69.44 women
# and of the 0.8% of women who do have cancer, only 90% of them will have a true positive:
# 8 * 0.9 = 7.2 women
# 7.2 / (7.2 + 69.44) = ~9.39%
