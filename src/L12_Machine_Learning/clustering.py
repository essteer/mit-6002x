# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import numpy as np

# set line width
plt.rcParams['lines.linewidth'] = 4
# set font size for titles
plt.rcParams['axes.titlesize'] = 20
# set font size for labels on axes
plt.rcParams['axes.labelsize'] = 20
# set size of numbers on x-axis
plt.rcParams['xtick.labelsize'] = 16
# set size of numbers on y-axis
plt.rcParams['ytick.labelsize'] = 16
# set size of ticks on x-axis
plt.rcParams['xtick.major.size'] = 7
# set size of ticks on y-axis
plt.rcParams['ytick.major.size'] = 7
# set size of markers
plt.rcParams['lines.markersize'] = 10
# set number of examples shown in legends
plt.rcParams['legend.numpoints'] = 1


def minkowski_distance(v1, v2, p):
    """
    Assumes v1 and v2 are equal-length arrays of numbers
    Returns Minkowski distance of order p between v1 and v2
    """
    distance = 0.0

    for i in range(len(v1)):
        distance += abs(v1[i] - v2[i])**p

    return distance**(1/p)


class Example(object):

    def __init__(self, name, features):
        # Assumes features is an array of floats
        self.name = name
        self.features = features

    def get_features(self):
        return self.features[:]

    def get_name(self):
        return self.name

    def dimensionality(self):
        return len(self.features)

    def set_color(self, color):
        self.color = color

    def distance(self, other):
        return minkowski_distance(self.features, other.get_features(), 2)


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
        self.old_centroid = old_centroid
        return old_centroid.distance(self.centroid)

    def compute_centroid(self):
        vals = np.array([0.0]*self.examples[0].dimensionality())
        for e in self.examples:  # compute mean
            vals += e.get_features()
        centroid = Example('centroid', vals/len(self.examples))
        return centroid

    def get_centroid(self):
        return self.compute_centroid()

    def variability(self):
        total_distance = 0.0
        for e in self.examples:
            total_distance += (e.distance(self.centroid))**2
        return total_distance

    def members(self):
        for e in self.examples:
            yield e

    def plot_cluster(self, color):
        xVals, yVals = [], []
        for e in self.examples:
            xVals.append(e.get_features()[0])
            yVals.append(e.get_features()[1])
        plt.plot(xVals, yVals, color + 'o')
        plt.plot([self.old_centroid.get_features()[0]],
                 [self.old_centroid.get_features()[1]],
                 color + '*', markersize=20)

    def __str__(self):
        names = []
        for e in self.examples:
            names.append(e.get_name())
        names.sort()
        result = 'Cluster with centroid '\
            + str(self.centroid.get_features()) + ' contains:\n  '
        for e in names:
            result = result + e + ', '
        return result[:-2]  # remove trailing comma and space


def k_means(examples, k, verbose=False):
    # Get k randomly chosen initial centroids, create cluster for each
    initial_centroids = random.sample(examples, k)
    clusters = []
    for e in initial_centroids:
        clusters.append(Cluster([e]))

    # Iterate until centroids do not change
    converged = False
    num_iterations = 0
    while not converged:
        num_iterations += 1
        # Create a list containing k distinct empty lists
        new_clusters = []
        for i in range(k):
            new_clusters.append([])

        # Associate each example with closest centroid
        for e in examples:
            # Find the centroid closest to e
            smallest_distance = e.distance(clusters[0].get_centroid())
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].get_centroid())
                if distance < smallest_distance:
                    smallest_distance = distance
                    index = i
            # Add e to the list of examples for appropriate cluster
            new_clusters[index].append(e)

        for c in new_clusters:  # Avoid having empty clusters
            if len(c) == 0:
                raise ValueError('Empty Cluster')

        # Update each cluster; check if a centroid has changed
        converged = True
        for i in range(k):
            if clusters[i].update(new_clusters[i]) > 0.0:
                converged = False
        if verbose:
            colors = ['b', 'r', 'k', 'm', 'y']
            color = 0
            plt.figure()
            print('Iteration #' + str(num_iterations))
            for c in clusters:
                print('Cluster color =', color)
                print(c)
                c.plot_cluster(colors[color])
                color += 1
            print('')  # add blank line
    return clusters


centers = [(2, 3), (4, 6), (7, 4), (7, 7)]
examples = []
random.seed(0)
for c in centers:
    for i in range(5):
        xVal = (c[0] + random.gauss(0, .5))
        yVal = (c[1] + random.gauss(0, .5))
        name = str(c) + '-' + str(i)
        example = Example(name, np.array([xVal, yVal]))
        examples.append(example)

xVals, yVals = [], []
for e in examples:
    xVals.append(e.get_features()[0])
    yVals.append(e.get_features()[1])

random.seed(2)
k_means(examples, 4, True)
