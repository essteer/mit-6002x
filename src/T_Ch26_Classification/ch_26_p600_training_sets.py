# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import sklearn.linear_model as sklm
import sklearn.metrics as skm


def accuracy(true_pos, false_pos, true_neg, false_neg):
    numerator = true_pos + true_neg
    denominator = true_pos + true_neg + false_pos + false_neg
    return numerator/denominator


def sensitivity(true_pos, false_neg):
    try:
        return true_pos/(true_pos + false_neg)
    except ZeroDivisionError:
        return float('nan')


def specificity(true_neg, false_pos):
    try:
        return true_neg/(true_neg + false_pos)
    except ZeroDivisionError:
        return float('nan')


def pos_pred_val(true_pos, false_pos):
    try:
        return true_pos/(true_pos + false_pos)
    except ZeroDivisionError:
        return float('nan')


def neg_pred_val(true_neg, false_neg):
    try:
        return true_neg/(true_neg + false_neg)
    except ZeroDivisionError:
        return float('nan')


def get_stats(true_pos, false_pos, true_neg, false_neg,
              toPrint=True):
    accur = accuracy(true_pos, false_pos, true_neg, false_neg)
    sens = sensitivity(true_pos, false_neg)
    spec = specificity(true_neg, false_pos)
    ppv = pos_pred_val(true_pos, false_pos)
    if toPrint:
        print(' Accuracy =', round(accur, 3))
        print(' Sensitivity =', round(sens, 3))
        print(' Specificity =', round(spec, 3))
        print(' Pos. Pred. Val. =', round(ppv, 3))
    return (accur, sens, spec, ppv)


class Runner(object):
    def __init__(self, name, gender, age, time):
        self._name = name
        self._feature_vec = np.array([age, time])
        self._label = gender

    def feature_dist(self, other):
        return ((self._feature_vec-other._feature_vec)**2).sum()**0.5

    def get_time(self):
        return self._feature_vec[1]

    def get_age(self):
        return self._feature_vec[0]

    def get_label(self):
        return self._label

    def get_features(self):
        return self._feature_vec

    def __str__(self):
        return (f'{self._name}: {self.get_age()}, ' +
                f'{self.get_time()}, {self._label}')


def build_marathon_examples(file_name):
    df = pd.read_csv(file_name)
    examples = []
    for index, row in df.iterrows():
        a = Runner(row['Name'], row['Gender'], row['Age'], row['Time'])
        examples.append(a)
    return examples


def divide_80_20(examples):
    sample_indices = random.sample(range(len(examples)),
                                   len(examples)//5)
    training_set, test_set = [], []
    for i in range(len(examples)):
        if i in sample_indices:
            test_set.append(examples[i])
        else:
            training_set.append(examples[i])
    return training_set, test_set


def find_k_nearest(example, example_set, k):
    k_nearest, distances = [], []
    # Build lists containing first k examples and their distances
    for i in range(k):
        k_nearest.append(example_set[i])
        distances.append(example.feature_dist(example_set[i]))
    max_dist = max(distances)  # Get maximum distance
    # Look at the examples not yet considered
    for e in example_set[k:]:
        dist = example.feature_dist(e)
        if dist < max_dist:
            # replace father neighbour by this one
            max_index = distances.index(max_dist)
            k_nearest[max_index] = e
            distances[max_index] = dist
            max_dist = max(distances)
    return k_nearest, distances


def k_nearest_classify(training_set, test_set, label, k):
    """Assumes training set & test_set lists of examples, k and int
       Uses a k-nearest neighbour classifier to predict
        whether each example in test_set has the given label
       Returns number of true positives, false positives,
          true negatives, and false negatives"""
    true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
    for e in test_set:
        print('Classifying', e)
        nearest, distances = find_k_nearest(e, training_set, k)
        # conduct vote
        num_match = 0
        for i in range(len(nearest)):
            if nearest[i].get_label() == label:
                num_match += 1
        if num_match > k//2:  # guess label
            if e.get_label() == label:
                true_pos += 1
            else:
                false_pos += 1
        else:  # guess not label
            if e.get_label() != label:
                true_neg += 1
            else:
                false_neg += 1
    return true_pos, false_pos, true_neg, false_neg

# examples = build_marathon_examples('bm_results2012.csv')
# training, test_set = divide_80_20(examples)
# true_pos, false_pos, true_neg, false_neg =\
#     k_nearest_classify(training, test_set, 'M', 9)
# get_stats(true_pos, false_pos, true_neg, false_neg)


def prevalence_classify(training_set, test_set, label):
    """Assumes training_set & test_set lists of examples
       Uses a prevalence-based classifier to predict
        whether each example in test_set is of class label
       Returns number of true positives, false positives, 
        true negatives, false negatives"""
    num_with_label = 0
    for e in training:
        if e.get_label() == label:
            num_with_label += 1
    prob_label = num_with_label/len(training_set)
    true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
    for e in test_set:
        if random.random() < prob_label:  # guess label
            if e.get_label() == label:
                true_pos += 1
            else:
                false_pos += 1
        else:  # guess not label
            if e.get_label() != label:
                true_neg += 1
            else:
                false_neg += 1
    return true_pos, false_pos, true_neg, false_neg


examples = build_marathon_examples('bm_results2012.csv')
training, test_set = divide_80_20(examples)
true_pos, false_pos, true_neg, false_neg =\
    prevalence_classify(training, test_set, 'M')
# get_stats(true_pos, false_pos, true_neg, false_neg)

# reduced_training = random.sample(training, len(training)//10)
# true_pos, false_pos, true_neg, false_neg =\
#     k_nearest_classify(reduced_training, test_set, 'M', 9)
# get_stats(true_pos, false_pos, true_neg, false_neg)


def find_k(training_set, min_k, max_k, num_folds, label):
    # Find average accuracy for range of odd values of k
    accuracies = []
    for k in range(min_k, max_k + 1, 2):
        score = 0.0
        for i in range(num_folds):
            # downsample to reduce computation time
            fold = random.sample(training_set,
                                 min(5000, len(training_set)))
            examples, test_set = divide_80_20(fold)
            true_pos, false_pos, true_neg, false_neg =\
                k_nearest_classify(examples, test_set, label, k)
            score += accuracy(true_pos, false_pos, true_neg, false_neg)
        accuracies.append(score/num_folds)
    plt.plot(range(min_k, max_k + 1, 2), accuracies)
    plt.title('Average Accuracy vs k (' + str(num_folds)
              + ' folds)')
    plt.xlabel('k')
    plt.ylabel('Accuracy')

# find_k(training, 1, 21, 5, 'M')


# Build training sets for men and women
age_m, age_w, time_m, time_w = [], [], [], []
for e in training:
    if e.get_label() == 'M':
        age_m.append(e.get_age())
        time_m.append(e.get_time())
    else:
        age_w.append(e.get_age())
        time_w.append(e.get_time())
# Downsample to make plot of examples readable
ages, times = [], []
for i in random.sample(range(len(age_m)), 300):
    ages.append(age_m[i])
    times.append(time_m[i])
# Produce scatter plot of examples
plt.plot(ages, times, 'yo', markersize=6, label='Men')
ages, times = [], []
for i in random.sample(range(len(age_w)), 300):
    ages.append(age_w[i])
    times.append(time_w[i])
plt.plot(ages, times, 'k^', markersize=6, label='Women')
# Learn two first-degree linear regression models
m_model = np.polyfit(age_m, time_m, 1)
f_model = np.polyfit(age_w, time_w, 1)
# Plot lines corresponding to models
xmin, xmax = 15, 85
plt.plot((xmin, xmax), (np.polyval(m_model, (xmin, xmax))),
         'k', label='Men')
plt.plot((xmin, xmax), (np.polyval(f_model, (xmin, xmax))),
         'k--', label='Women')
plt.title('Linear Regression Models')
plt.xlabel('Age')
plt.ylabel('Finishing time (minutes)')
plt.legend()

true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
for e in test_set:
    age = e.get_age()
    time = e.get_time()
    if (abs(time - np.polyval(m_model, age)) <
            abs(time - np.polyval(f_model, age))):
        if e.get_label() == 'M':
            true_pos += 1
        else:
            false_pos += 1
    else:
        if e.get_label() == 'F':
            true_neg += 1
        else:
            false_neg += 1
get_stats(true_pos, false_pos, true_neg, false_neg)
