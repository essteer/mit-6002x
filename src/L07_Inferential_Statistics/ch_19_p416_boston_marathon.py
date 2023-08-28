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
make_hist(times, 20, '2012 Boston Marathon',
          'Minutes to Complete Race', 'Number of Runners')
