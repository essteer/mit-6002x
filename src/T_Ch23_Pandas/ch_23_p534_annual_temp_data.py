# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_rows', 6)
pd.set_option('display.max_columns', 5)
temperatures = pd.read_csv('US_temperatures.csv')


def get_dict(temperatures, labels):
    """temperatures a DataFrame. Its indices are ints
        representing dates of the form yyyymmdd
       labels a list of column labels
       returns a dict with strs representing years as keys, 
          the values dicts with the columns as keys, and 
          a list of the daily temperatures in that column for
          that year as values
    """
    year_dict = {}
    for index, row in temperatures.iterrows():
        year = str(index)[0:4]
        try:
            for col in labels:
                year_dict[year][col].append(row[col])
        except:
            year_dict[year] = {col: [] for col in labels}
            for col in labels:
                year_dict[year][col].append(row[col])
    return year_dict


temperatures.set_index('Date', drop=True, inplace=True)
temperatures['Mean T'] = round(temperatures.mean(axis='columns'), 2)
temperatures['Max T'] = temperatures.max(axis='columns')
temperatures['Min T'] = temperatures.min(axis='columns')
yearly_dict = get_dict(temperatures, ['Max T', 'Min T', 'Mean T'])

years, mins, maxes, means = [], [], [], []
for y in yearly_dict:
    years.append(y)
    mins.append(min(yearly_dict[y]['Min T']))
    maxes.append(max(yearly_dict[y]['Max T']))
    means.append(round(np.mean(yearly_dict[y]['Mean T']), 2))

yearly_temps = pd.DataFrame({'Year': years, 'Min T': mins,
                             'Max T': maxes, 'Mean T': means})

# print(yearly_temps)

# plt.figure(0)
# plt.plot(yearly_temps['Year'], yearly_temps['Mean T'])
# plt.title('Mean Annual Temp in 21 U.S. Cities')
# plt.figure(1)
# plt.plot(yearly_temps['Year'], yearly_temps['Min T'])
# plt.title('Min Annual Temp in 21 U.S. Cities')
# for i in range(2):
#     plt.figure(i)
#     plt.xticks(range(0, len(yearly_temps), 4),
#                rotation = 'vertical', size = 'large')
#     plt.ylabel('Degrees C')


def r_squared(measured, predicted):
    """Assumes measured a one-dimensional array of measured values
               predicted a one-dimensional array of predicted values
       Returns coefficient of determination"""
    estimated_error = ((predicted - measured)**2).sum()
    mean_of_measured = measured.sum()/len(measured)
    variability = ((measured - mean_of_measured)**2).sum()
    return 1 - estimated_error/variability


# Rolling average
num_years = 7
for label in ['Min T', 'Max T', 'Mean T']:
    yearly_temps[label] = yearly_temps[label].rolling(num_years).mean()
yearly_temps['Year'] = yearly_temps['Year'].apply(int)
# print(yearly_temps.corr())


indices = np.isfinite(yearly_temps['Mean T'])
model = np.polyfit(list(yearly_temps['Year'][indices]),
                   list(yearly_temps['Mean T'][indices]), 1)
print(r_squared(yearly_temps['Mean T'][indices],
      np.polyval(model, yearly_temps['Year'][indices])))
