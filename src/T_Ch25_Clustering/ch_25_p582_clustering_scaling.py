# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random
import numpy as np
import pandas as pd


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
        """
        Returns Euclidian (Minkowski) distance between two examples
        """
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

        for c in new_clusters:  # Avoid having empty cluster
            if len(c) == 0:
                raise ValueError('Empty Cluster')

        # Update each cluster; check if a centroid has changed
        converged = True
        for i in range(k):
            if clusters[i].update(new_clusters[i]) > 0.0:
                converged = False
        if verbose:
            print('Iteration #' + str(num_iterations))
            for c in clusters:
                print(c)
            print('')  # add blank line
    return clusters


def dissimilarity(clusters):
    tot_dist = 0.0
    for c in clusters:
        tot_dist += c.variability()
    return tot_dist


def try_k_means(examples, num_clusters, num_trials, verbose=False):
    """Calls k_means num_trials times and returns the result with the
       lowest dissimilarity"""
    best = k_means(examples, num_clusters, verbose)
    min_dissimilarity = dissimilarity(best)
    trial = 1
    while trial < num_trials:
        try:
            clusters = k_means(examples, num_clusters, verbose)
        except ValueError:
            continue  # If failed, try again
        curr_dissimilarity = dissimilarity(clusters)
        if curr_dissimilarity < min_dissimilarity:
            best = clusters
            min_dissimilarity = curr_dissimilarity
        trial += 1
    return best


def gen_distribution(x_mean, x_sd, y_mean, y_sd, n, name_prefix):
    samples = []
    for s in range(n):
        x = random.gauss(x_mean, x_sd)
        y = random.gauss(y_mean, y_sd)
        samples.append(Example(name_prefix+str(s), [x, y]))
    return samples


def plot_samples(samples, marker):
    x_vals, y_vals = [], []
    for s in samples:
        x = s.get_features()[0]
        y = s.get_features()[1]
        plt.annotate(s.get_name(), xy=(x, y),
                     xytext=(x+0.13, y-0.07),
                     fontsize='x-large')
        x_vals.append(x)
        y_vals.append(y)
    plt.plot(x_vals, y_vals, marker)


def read_mammal_data(fName, scale_method=None):
    """fName a CSV file describing dentition of mammals
       returns a dict mapping species to feature vectors
    """
    df = pd.read_csv(fName, comment='#')
    df = df.set_index('Name')
    if scale_method != None:
        for c in df.columns:
            df[c] = scale_method(df[c])
    feature_vector_list = [np.array(df.loc[i].values)
                           for i in df.index]
    species_names = list(df.index)
    return {species_names[i]: feature_vector_list[i]
            for i in range(len(species_names))}


def build_mammal_examples(species_dict):
    examples = []
    for i in species_dict:
        example = Example(i, species_dict[i])
        examples.append(example)
    return examples


def test_teeth(file_name, num_clusters, num_trials,
               scale_method=None):
    def print_clustering(clustering):
        for c in clustering:
            names = ''
            for p in c.members():
                names += p.get_name() + ', '
            print('\n' + names[:-2])  # remove trailing comma and space
    species_dict = read_mammal_data(file_name, scale_method)
    examples = build_mammal_examples(species_dict)
    print_clustering(try_k_means(examples, num_clusters, num_trials))

# test_teeth('dentalFormulas.csv', 3, 40)


def z_scale(vals):
    """Assumes vals is a sequence of floats"""
    result = np.array(vals) - np.array(vals).mean()
    return (result/np.std(result)).round(4)


def linear_scale(vals):
    """Assumes vals is a sequence of floats"""
    vals = np.array(vals)
    vals -= vals.min
    return (vals/vals.max()).round(4)

# test_teeth('dentalFormulas.csv', 3, 40, z_scale)


def add_labels(examples, label_file):
    df = pd.read_csv(label_file, comment='#')
    df = df.set_index('Name')
    for e in examples:
        if e.get_name() in df.index:
            e.set_label(df.loc[e.get_name()]['Diet'])


def check_diet(cluster):
    herbivores, carnivores, omnivores = 0, 0, 0
    for m in cluster.members():
        if m.get_label() == 0:
            herbivores += 1
        elif m.get_label() == 1:
            carnivores += 1
        else:
            omnivores += 1
    print('   ', herbivores, 'herbivores,', carnivores,
          'carnivores,', omnivores, 'omnivores\n')


def test_teeth_diet(features_file, labels_file, num_clusters,
                    num_trials, scale_method=None):
    def print_clustering(clustering):
        for c in clustering:
            names = ''
            for p in c.members():
                names += p.get_name() + ', '
            print(names[:-2])
            check_diet(c)
    species_dict = read_mammal_data(features_file, scale_method)
    examples = build_mammal_examples(species_dict)
    add_labels(examples, labels_file)
    print_clustering(try_k_means(examples, num_clusters, num_trials))


test_teeth_diet('dentalFormulas.csv', 'diet.csv', 3, 40, z_scale)
