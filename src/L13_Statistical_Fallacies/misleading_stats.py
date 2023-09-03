# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt

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

random.seed(0)
num_cases_per_year = 36000
num_years = 3
state_size = 10000
community_size = 10
num_communities = state_size//community_size
num_trials = 100
num_greater = 0
for t in range(num_trials):
    locs = [0]*num_communities
    for i in range(num_years*num_cases_per_year):
        locs[random.choice(range(num_communities))] += 1
    if max(locs) >= 143:
        num_greater += 1
prob = round(num_greater/num_trials, 4)
print('Est. probability of at least one region having \
at least 143 cases =', prob)


# print('Average number of cases per community =',
#      (num_years*num_cases_per_year)/num_communities)
# print('Maximum number of cases in community X =',
#      max(locs))
# plt.hist(locs)
# plt.xlabel('Region')
# plt.ylabel('Number of New Cancer Cases')
