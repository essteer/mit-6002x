# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_rows', 6)
pd.set_option('display.max_columns', 5)
emissions = pd.read_csv('global-fossil-fuel-consumption.csv')
# print(emissions)

emissions['Fuels'] = emissions.sum(axis='columns')
emissions.drop(['Coal', 'Crude Oil', 'Natural Gas'],
               axis='columns', inplace=True)
num_years = 5
emissions['Roll F'] =\
    emissions['Fuels'].rolling(num_years).mean()
emissions = emissions.round()

plt.plot(emissions['Year'], emissions['Fuels'],
         label='Consumption')
plt.plot(emissions['Year'], emissions['Roll F'],
         label=str(num_years) + ' Year Rolling Ave.')
plt.legend()
plt.title('Consumption of Fossil Fuels')
plt.xlabel('Year')
plt.ylabel('Consumption')

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
# temperatures.drop('Date', axis='columns', inplace=True)
means = round(temperatures.mean(), 2)
maxes = temperatures.max()
mins = temperatures.min()
city_temps = pd.DataFrame({'Min T': mins, 'Max T': maxes,
                           'Mean T': means})
city_temps = city_temps.apply(lambda x: 1.8*x + 32)
city_temps['Max-Min'] = city_temps['Max T'] - city_temps['Min T']

# print(city_temps.sort_values('Mean T', ascending=False).to_string())

plt.figure()
plt.plot(city_temps.sort_values('Max-Min', ascending=False)['Min T'],
         'b^', label='Min T')
plt.plot(city_temps.sort_values('Max-Min', ascending=False)['Max T'],
         'kx', label='Max T')
plt.plot(city_temps.sort_values('Max-Min', ascending=False)['Mean T'],
         'ro', label='Mean T')
plt.xticks(rotation='vertical')
plt.legend()
plt.title('Variation in Extremal Daily\nTemperature 1961-2015')
plt.ylabel('Degrees F')

yearly_temps['Year'] = yearly_temps['Year'].astype(int)
merged_df = pd.merge(yearly_temps, emissions,
                     left_on='Year', right_on='Year')
print(merged_df)
