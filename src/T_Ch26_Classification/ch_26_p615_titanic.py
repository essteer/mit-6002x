# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import sklearn.linear_model as sklm
import sklearn.metrics as skm


def minkowski_distance(v1, v2, p):
    """
    Assumes v1 and v2 are equal-length arrays of numbers
    Returns Minkowski distance of order p between v1 and v2
    """
    distance = 0.0

    for i in range(len(v1)):
        distance += abs(v1[i] - v2[i])**p

    return distance**(1/p)


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


class Passenger(object):
    features = ("1st Class", "2nd Class", "3rd Class", "age", "male")

    def __init__(self, p_class, age, gender, survived, name):
        self.name = name
        self.feature_vec = [0, 0, 0, age, gender]
        self.feature_vec[p_class - 1] = 1
        self.label = survived
        self.cabin_class = p_class

    def distance(self, other):
        return minkowski_distance(self.feature_vec, other.feature_vec, 2)

    def get_class(self):
        return self.cabin_class

    def get_age(self):
        return self.feature_vec[3]

    def get_gender(self):
        return self.feature_vec[4]

    def get_name(self):
        return self.name

    def get_features(self):
        return self.feature_vec[:]

    def get_label(self):
        return self.label


def build_titanic_examples():
    manifest = pd.read_csv("TitanicPassengers.csv")
    examples = []
    for index, row in manifest.iterrows():
        p = Passenger(row["Class"], row["Age"],
                      1 if row["Gender"] == "M" else 0,
                      row["Survived"],
                      row["Last Name"] + row["Other Names"])
        examples.append(p)
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


def apply_model(model, test_set, label, prob=0.5):
    # Create vector containing feature vectors for all test examples
    test_feature_vecs = [e.get_features() for e in test_set]
    probs = model.predict_proba(test_feature_vecs)
    true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
    for i in range(len(probs)):
        if probs[i][1] > prob:
            if test_set[i].get_label() == label:
                true_pos += 1
            else:
                false_pos += 1
        else:
            if test_set[i].get_label() != label:
                true_neg += 1
            else:
                false_neg += 1
    return true_pos, false_pos, true_neg, false_neg


def build_ROC(model, test_set, label, title, plot=True):
    x_vals, y_vals = [], []
    for p in np.arange(0, 1, 0.01):
        true_pos, false_pos, true_neg, false_neg = apply_model(
            model, test_set, label, p)
        x_vals.append(1.0 - specificity(true_neg, false_pos))
        y_vals.append(sensitivity(true_pos, false_neg))

    auroc = skm.auc(x_vals, y_vals)

    if plot:
        plt.plot(x_vals, y_vals)
        plt.plot([0, 1], [0, 1], "--")
        plt.title(f"{title} (AUROC = {str(round(auroc, 3))})")
        plt.xlabel("1 - Specificity")
        plt.ylabel("Sensitivity")

    return auroc


def test_models(examples, num_trials, print_stats, print_weights):
    stats, weights = [], [[], [], [], [], []]

    for i in range(num_trials):
        training, test_set = divide_80_20(examples)
        x_vals, y_vals = [], []

        for e in training:
            x_vals.append(e.get_features())
            y_vals.append(e.get_label())

        x_vals = np.array(x_vals)
        y_vals = np.array(y_vals)
        model = sklm.LogisticRegression().fit(x_vals, y_vals)

        for i in range(len(Passenger.features)):
            weights[i].append(model.coef_[0][i])

        true_pos, false_pos, true_neg, false_neg = apply_model(
            model, test_set, 1, 0.5)

        auroc = build_ROC(model, test_set, 1, None, False)
        tmp = get_stats(true_pos, false_pos, true_neg, false_neg, False)
        stats.append(tmp + (auroc,))

    print(f"Averages for {num_trials} trials")

    if print_weights:
        for feature in range(len(weights)):
            feature_mean = round(sum(weights[feature]) / num_trials, 3)
            feature_std = np.std(weights[feature])
            print(
                f" Mean weight {Passenger.features[feature]} = {str(feature_mean)}, 95% conf. int. = {round(feature_mean - 1.96*feature_std, 3)} to {round(feature_mean + 1.96*feature_std, 3)}")

    if print_stats:
        summarize_stats(stats)


def summarize_stats(stats):
    """
    assumes stats a list of 5 floats: accuracy, sensitivity, 
    specificity, pos. pred. val, ROC
    """
    def print_stat(X, name):
        mean = round(sum(X)/len(X), 3)
        std = np.std(X)
        print(
            f" Mean {name} = {str(mean)}, 95% conf. int. = {round(mean - 1.96*std, 3)} to {round(mean + 1.96*std, 3)}")

    accs, sens, specs, ppvs, aurocs = [], [], [], [], []

    for stat in stats:
        accs.append(stat[0])
        sens.append(stat[1])
        specs.append(stat[2])
        ppvs.append(stat[3])
        aurocs.append(stat[4])

    print_stat(accs, "accuracy")
    print_stat(sens, "sensitivity")
    print_stat(accs, "specificity")


test_models(build_titanic_examples(), 100, True, False)
