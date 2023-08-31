# -*- coding: utf-8 -*-
import numpy


def r_squared(observed, predicted):
    error = ((predicted - observed)**2).sum()
    mean_error = error/len(observed)
    return 1 - (mean_error/numpy.var(observed))
