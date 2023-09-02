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


class Animal(object):
    def __init__(self, name, features):
        """Assumes name a string; features a list of numbers"""
        self.name = name
        self.features = np.array(features)

    def get_name(self):
        return self.name

    def get_features(self):
        return self.features

    def distance(self, other):
        """Assumes other is an Animal
           Returns the Euclidian distance between feature vectors 
           of self and other"""
        return minkowski_distance(self.get_features(), other.get_features(), 2)


def compare_animals(animals, precision):
    """Assumes animals is a list of animals, precision an int >= 0
       Builds a table of distances between each animal"""
    # Get labels for columns and rows
    column_labels = [a.get_name() for a in animals]
    row_labels = column_labels[:]
    table_vals = []
    # Get distances between pairs of animals
    # For each row
    for a1 in animals:
        row = []
        # For each column
        for a2 in animals:
            distance = a1.distance(a2)
            row.append(str(round(distance, precision)))
        table_vals.append(row)
    # Produce table
    table = plt.table(rowLabels=row_labels,
                      colLabels=column_labels,
                      cellText=table_vals,
                      cellLoc='center',
                      loc='center',
                      colWidths=[0.2]*len(animals))
    plt.axis('off')
    table.scale(1, 2.5)


rattlesnake = Animal('rattlesnake', [1, 1, 1, 1, 0])
boa = Animal('boa', [0, 1, 0, 1, 0])
dart_frog = Animal('dart frog', [1, 0, 1, 0, 4])
animals = [rattlesnake, boa, dart_frog]
alligator = Animal('alligator', [1, 1, 0, 1, 4])
animals.append(alligator)
compare_animals(animals, 3)
