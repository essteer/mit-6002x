import random
import numpy as np
import matplotlib.pyplot as plt
import scipy


def plot_means(num_dice_per_trial, num_dice_thrown, num_bins, legend, color, style):
    means = []
    num_trials = num_dice_thrown//num_dice_per_trial
    for i in range(num_trials):
        vals = 0
        for j in range(num_dice_per_trial):
            vals += 5*random.random()
        means.append(vals/num_dice_per_trial)
    plt.hist(means, num_bins, color=color, label=legend,
             weights=np.array(len(means)*[1])/len(means), hatch=style)
    return sum(means)/len(means), np.var(means)


mean, var = plot_means(1, 1000000, 11, '1 die', 'y', '*')
print('Mean of rolling 1 die =', round(mean, 4), 'Variance =', round(var, 4))
mean, var = plot_means(100, 1000000, 11, 'Mean 100 dice', 'c', '//')
print('Mean of rolling 100 dice =', round(
    mean, 4), 'Variance =', round(var, 4))
plt.title('Rolling Continuous Dice')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.legend(loc='upper left')
