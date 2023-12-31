# -*- coding: utf-8 -*-
import pylab

# set line width
pylab.rcParams['lines.linewidth'] = 4
# set font size for titles
pylab.rcParams['axes.titlesize'] = 20
# set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
# set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
# set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
# set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
# set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
# set size of markers
pylab.rcParams['lines.markersize'] = 10
# set number of examples shown in legends
pylab.rcParams['legend.numpoints'] = 1


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
        self.features = pylab.array(features)

    def get_name(self):
        return self.name

    def get_features(self):
        return self.features

    def distance(self, other):
        """Assumes other an Animal
           Returns the Euclidean distance between feature vectors
              of self and other"""
        return minkowski_distance(self.get_features(),
                                  other.get_features(), 2)

    def __str__(self):
        return self.name


# In this iteration, number of legs is given undue weight versus the other features
cobra = Animal('cobra', [1, 1, 1, 1, 0])
rattlesnake = Animal('rattlesnake', [1, 1, 1, 1, 0])
boa = Animal('boa\nconstrictor', [0, 1, 0, 1, 0])
chicken = Animal('chicken', [1, 1, 0, 1, 2])
alligator = Animal('alligator', [1, 1, 0, 1, 4])
dartFrog = Animal('dart frog', [1, 0, 1, 0, 4])
zebra = Animal('zebra', [0, 0, 0, 0, 4])
python = Animal('python', [1, 1, 0, 1, 0])
guppy = Animal('guppy', [0, 1, 0, 0, 0])
animals = [cobra, rattlesnake, boa, chicken, guppy,
           dartFrog, zebra, python, alligator]

# In this iteration, number of legs has been made binary (has legs) to equalise it with other features
# cobra = Animal('cobra', [1,1,1,1,0])
# rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
# boa = Animal('boa\nconstrictor', [0,1,0,1,0])
# chicken = Animal('chicken', [1,1,0,1,2])
# alligator = Animal('alligator', [1,1,0,1,1])
# dartFrog = Animal('dart frog', [1,0,1,0,1])
# zebra = Animal('zebra', [0,0,0,0,1])
# python = Animal('python', [1,1,0,1,0])
# guppy = Animal('guppy', [0,1,0,0,0])
# animals = [cobra, rattlesnake, boa, chicken, guppy,
#           dartFrog, zebra, python, alligator]


def compare_animals(animals, precision):
    """Assumes animals is a list of animals, precision an int >= 0
       Builds a table of Euclidean distance between each animal"""
    # Get labels for columns and rows
    column_labels = []
    for a in animals:
        column_labels.append(a.get_na())
    row_labels = column_labels[:]
    table_vals = []
    # Get distances between pairs of animals
    # For each row
    for a1 in animals:
        row = []
        # For each column
        for a2 in animals:
            if a1 == a2:
                row.append('--')
            else:
                distance = a1.distance(a2)
                row.append(str(round(distance, precision)))
        table_vals.append(row)
    # Produce table
    table = pylab.table(row_labels=row_labels,
                        colLabels=column_labels,
                        cellText=table_vals,
                        cellLoc='center',
                        loc='center',
                        colWidths=[0.138]*len(animals))
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    help(table.scale)
    table.scale(1, 2.5)
    pylab.axis('off')
    pylab.savefig('distances')


compare_animals(animals, 3)
