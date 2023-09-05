# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 6)
pd.set_option('display.max_columns', 5)
temperatures = pd.read_csv('US_temperatures.csv')
# print(temperatures)

# Return the temperatures for New York and Tampa on 12 August 1979
# print(temperatures.loc[temperatures['Date']==19790812][['New York', 'Tampa']])

# Return True or False for whether Phoenix was hotter than Tampa on 31 October 2000
# print((temperatures.loc[temperatures['Date']==20001031]['Phoenix']) > (temperatures.loc[temperatures['Date']==20001031]['Tampa']))

# Find the date on which Phoenix recorded a temp of 41.4
# print(temperatures.loc[temperatures['Phoenix']==41.4]['Date'])

# temperatures['Max T'] = temperatures.max(axis = 'columns')
# temperatures['Min T'] = temperatures.min(axis = 'columns')
# temperatures['Mean T'] = round(temperatures.mean(axis = 'columns'), 2)
# print(temperatures.loc[temperatures['Date']==20000704])

temperatures.set_index('Date', drop=True, inplace=True)
temperatures['Max'] = temperatures.max(axis='columns')
temperatures['Min'] = temperatures.min(axis='columns')
temperatures['Mean T'] = round(temperatures.mean(axis='columns'), 2)
# print(temperatures.loc[20000704:20000704])

# plt.figure(figsize = (14, 3)) # set aspect ratio for figure
# plt.plot(list(temperatures['Mean T']))
# plt.title('Mean Temp Across 21 US Cities')
# plt.xlabel('Days Since 1/1/1961')
# plt.ylabel('Degrees C')

plt.figure(figsize=(14, 3))  # set aspect ratio for figure
plt.plot(list(temperatures['Mean T'])[0:3*365])
plt.title('Mean Temp Across 21 US Cities')
plt.xlabel('Days Since 1/1/1961')
plt.ylabel('Degrees C')
