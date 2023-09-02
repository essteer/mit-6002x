# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


def minkowski_distance(v1, v2, p):
    """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p betweeen v1 and v2"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1/p)


class Example(object):

    def __init__(self, name, features, label=None):
        # Assumes features is an array of floats
        self.name = name
        self.features = features
        self.label = label

    def dimensionality(self):
        return len(self.features)

    def set_label(self, label):
        self.label = label

    def get_features(self):
        return self.features[:]

    def get_label(self):
        return self.label

    def get_name(self):
        return self.name

    def distance(self, other):
        return minkowski_distance(self.features, other.get_features(), 2)

    def __str__(self):
        return '{}:{}:{}'.format(self.name, self.features, self.label)


class Cluster(object):
    def __init__(self, examples):
        """Assumes examples a non-empty list of Examples"""
        self.examples = examples
        self.centroid = self.compute_centroid()

    def update(self, examples):
        """Assume examples is a non-empty list of Examples
           Replace examples; return amount centroid has changed"""
        old_centroid = self.centroid
        self.examples = examples
        self.centroid = self.compute_centroid()
        return old_centroid.distance(self.centroid)

    def compute_centroid(self):
        vals = np.array([0.0]*self.examples[0].dimensionality())
        for e in self.examples:  # compute mean
            vals += e.get_features()
        centroid = Example('centroid', vals/len(self.examples))
        return centroid

    def get_centroid(self):
        return self.centroid

    def variability(self):
        tot_dist = 0.0
        for e in self.examples:
            tot_dist += (e.distance(self.centroid))**2
        return tot_dist

    def members(self):
        for e in self.examples:
            yield e

    def __str__(self):
        names = []
        for e in self.examples:
            names.append(e.get_name())
        names.sort()
        result = ('Cluster with centroid '
                  + str(self.centroid.get_features()) + ' contains:\n  ')
        for e in names:
            result = result + e + ', '
        return result[:-2]  # remove trailing comma and space
