# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


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
    plt.bar(quarters, prices, width)
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


plot_housing("flat")
plt.figure()
plot_housing("volatile")
plt.figure()
plot_housing("fair")
