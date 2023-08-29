import random
import pylab


def get_mean_and_std(num_list):
    """
    Takes num_list, a list / array of numbers
    Returns a tuple of the mean and standard deviation of num_list
    """
    mean = sum(num_list) / float(len(num_list))
    total = 0.0

    for x in num_list:
        total += (x - mean)**2
    standard_deviation = (total / len(num_list))**0.5

    return mean, standard_deviation


L = [1, 1, 1, 1, 2]
pylab.hist(L)
factor = pylab.array(len(L)*[1])/len(L)
print(factor)
pylab.figure()
pylab.hist(L, weights=factor)


def plotMeans(numDice, numRolls, numBins, legend, color, style):
    means = []
    for i in range(numRolls//numDice):
        vals = 0
        for j in range(numDice):
            vals += 5*random.random()
        means.append(vals/float(numDice))
    pylab.hist(means, numBins, color=color, label=legend,
               weights=pylab.array(len(means)*[1])/len(means),
               hatch=style)
    return get_mean_and_std(means)


mean, std = plotMeans(1, 1000000, 19, '1 die', 'b', '*')
print('Mean of rolling 1 die =', str(mean) + ',', 'Std =', std)

mean, std = plotMeans(50, 1000000, 19, 'Mean of 50 dice', 'r', '//')
print('Mean of rolling 50 dice =', str(mean) + ',', 'Std =', std)

pylab.title('Rolling Continuous Dice')
pylab.xlabel('Value')
pylab.ylabel('Probability')
pylab.legend()
