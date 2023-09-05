# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_rows', 6)
pd.set_option('display.max_columns', 5)
temperatures = pd.read_csv('US_temperatures.csv')

temperatures.drop('Date', axis='columns', inplace=True)
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
