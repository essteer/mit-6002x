# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Finger exercise: it is sometimes illuminating to plot things relative to a baseline.
# Modify plot_housing to produce such plots.
# The bars below the baseline should be in red.
# Hint: use the "bottom" keyword argument to plt.bar


def plot_housing(impression):
    """Assumes impression a str. Must be one of 'flat',
       'volatile', and 'fair'
       Produce bar chart of housing prices over time"""
    labels, prices = [], []
    with open('midWestHousingPrices.csv', 'r') as f:
        # Each line of file contains year quarter price
        # for Midwest region of US
        for line in f:
            year, quarter, price = line.split(',')
            label = year[2:4] + '\n Q' + quarter[1]
            labels.append(label)
            prices.append(int(price)/1000)
    quarters = np.arange(len(labels))  # x coords of bars
    width = 0.8  # Width of bars

    baseline = 200  # set the baseline at US$200,000
    baseline_prices = [x - baseline for x in prices]
    colors = ["b" if price >= 0 else "r" for price in baseline_prices]
    # Alternative method:
    # cc = [('tab:purple' if price < 0 else 'tab:olive') for price in baseline_prices]

    plt.bar(quarters, baseline_prices, width, color=colors, bottom=baseline)
    # Alternative method:
    # plt.bar(quarters, baseline_prices, width, color=cc, bottom=baseline)
    plt.xticks(quarters+width/2, labels)
    plt.title("Housing Prices in US Midwest")
    plt.xlabel("Quarter")
    plt.ylabel("Average Price ($1,000\'s)")
    if impression == "flat":
        plt.ylim(1, 500)
    elif impression == "volatile":
        plt.ylim(180, 220)
    elif impression == "fair":
        plt.ylim(150, 250)
    else:
        raise ValueError

    plt.axhline(y=baseline, color="k")


# plot_housing("flat")
# plt.figure()
# plot_housing("volatile")
plt.figure()
plot_housing("fair")
