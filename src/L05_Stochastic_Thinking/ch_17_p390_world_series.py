import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate


def play_series(num_games, team_prob):
    numWon = 0
    for game in range(num_games):
        if random.random() <= team_prob:
            numWon += 1
    return (numWon > num_games//2)


def fraction_won(team_prob, num_series, series_len):
    won = 0
    for series in range(num_series):
        if play_series(series_len, team_prob):
            won += 1
    return won/float(num_series)


def sim_series(num_series):
    prob = 0.5
    fracsWon, probs = [], []
    while prob <= 1.0:
        fracsWon.append(fraction_won(prob, num_series, 7))
        probs.append(prob)
        prob += 0.01
    plt.axhline(0.95)  # draw line at 95%
    plt.plot(probs, fracsWon, "k", linewidth=5)
    plt.xlabel("Probability of Winning a Game")
    plt.ylabel("Probability of Winning a Series")
    plt.title(str(num_series) + " Seven-Game Series")


sim_series(400)
