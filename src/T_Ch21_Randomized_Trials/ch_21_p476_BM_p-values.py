# -*- coding: utf-8 -*-
import random
import numpy as np
import matplotlib.pyplot as plt
import scipy


def get_BM_data(filename):
    """Read the contents of the given file. Assumes the file is in
    a comma-separated format, with 6 elements in each entry:
    0. Name (string), 1. Gender (string), 2. Age (int), 
    3. Division (int), 4. Country (string), 5. Overall time (float)
    Returns: dict containing a list for each of the 6 variables"""

    data = {}
    with open(filename, 'r') as f:
        f.readline()  # discard the first line
        line = f.readline()
        for k in ('name', 'gender', 'age', 'division', 'country', 'time'):
            data[k] = []
        while line != '':
            split = line.split(',')
            data['name'].append(split[0])
            data['gender'].append(split[1])
            data['age'].append(int(split[2]))
            data['division'].append(int(split[3]))
            data['country'].append(split[4])
            data['time'].append(float(split[5][:-1]))  # remove \n
            line = f.readline()
        return data


data = get_BM_data('bm_results2012.csv')
countries_to_compare = ['BEL', 'BRA', 'FRA', 'JPN', 'ITA']

# Build mapping from country to list of female finishing times
country_times = {}
for i in range(len(data['name'])):  # for each racer
    if (data['country'][i] in countries_to_compare and
            data['gender'][i] == 'F'):
        try:
            country_times[data['country'][i]].append(data['time'][i])
        except KeyError:
            country_times[data['country'][i]] = [data['time'][i]]

# Compare finishing times of countries
for c1 in countries_to_compare:
    for c2 in countries_to_compare:
        if c1 < c2:  # rather than != so each pair examined once
            pVal = scipy.stats.ttest_ind(country_times[c1],
                                         country_times[c2],
                                         equal_var=False)[1]
            if pVal < 0.05:
                print(c1, "and", c2,
                      "have significantly different means,",
                      "p-value =", round(pVal, 4))
