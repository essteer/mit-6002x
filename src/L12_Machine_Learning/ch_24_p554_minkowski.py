# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


def minkowski_distance(v1, v2, p):
    """
    Assumes v1 and v2 are equal-length arrays of numbers
    Returns Minkowski distance of order p between v1 and v2
    """
    distance = 0.0

    for i in range(len(v1)):
        distance += abs(v1[i] - v2[i])**p

    return distance**(1/p)
