import random
import numpy as np
import matplotlib.pyplot as plt
import scipy


def get_BM_data(filename):
    """Read the contents of the given file. Assumes the file is in
    comma-separated value (CSV) format, with 6 elements in each entry:
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


def make_hist(data, bins, title, xLabel, yLabel):
    plt.hist(data, bins)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    mean = sum(data)/len(data)
    std = np.std(data)
    plt.annotate('Mean = ' + str(round(mean, 2)) + '\nSD = ' + str(round(std, 2)),
                 fontsize=14, xy=(0.65, 0.75), xycoords='axes fraction')


times = get_BM_data('bm_results2012.csv')['time']
# make_hist(times, 20, '2012 Boston Marathon', 'Minutes to Complete Race', 'Number of Runners')


def sample_times(times, num_examples):
    """Assumes times is a list of floats representing finishing
       times of all runners. num_examples is an int
       Generates a random sample of size num_examples, and produces
       a histogram showing the distribution along with its mean and
       standard deviation"""
    sample = random.sample(times, num_examples)
    make_hist(sample, 10, 'Sample of Size ' + str(num_examples),
              'Minutes to Complete Race', 'Number of Runners')

# sample_size = 40
# sample_times(times, sample_size)

# mean_of_means, std_of_means = [], []
# sample_sizes = range(100, 1501, 200)
# for sample_size in sample_sizes:
#     sample_means = []
#     for t in range(200):
#         sample = random.sample(times, sample_size)
#         sample_means.append(sum(sample)/sample_size)
#     mean_of_means.append(sum(sample_means)/len(sample_means))
#     std_of_means.append(np.std(sample_means))

# plt.errorbar(sample_sizes, mean_of_means, color = 'c', yerr = 1.96*np.array(std_of_means), label = 'Estimated mean and 95% CI')
# plt.axhline(sum(times)/len(times), linestyle = '--', color = 'k', label = 'Population mean')
# plt.title('Estimates of Mean Finishing Time')
# plt.xlabel('Sample Size')
# plt.ylabel('Finishing Time (minutes)')
# plt.legend(loc = 'best')

# times = get_BM_data('bm_results2012.csv')['time']
# pos_std = np.std(times)
# sample_sizes = range(2, 200, 2)
# diffs_means= []
# for sample_size in sample_sizes:
#     diffs = []
#     for t in range(100):
#         diffs.append(abs(pos_std - np.std(random.sample(times, sample_size))))
#         diffs_means.append(sum(diffs)/len(diffs))

# plt.plot(sample_sizes, diffs_means)
# plt.xlabel('Sample Size')
# plt.ylabel('Abs(Pop. Std - Sample Std')
# plt.title('Error in Sample SD vs. Sample Size')


times = get_BM_data('bm_results2012.csv')['time']
pop_mean = sum(times)/len(times)
sample_size = 200
num_bad = 0
for t in range(10000):
    sample = random.sample(times, sample_size)
    sample_mean = sum(sample)/sample_size
    se = np.std(sample)/sample_size**0.5
    if abs(pop_mean - sample_mean) > 1.96*se:
        num_bad += 1
print('Fraction outside 95% confidence interval =', num_bad/10000)
