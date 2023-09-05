# -*- coding: utf-8 -*-
import pandas as pd
wwc = pd.read_csv('wwc2019_q-f.csv')


def get_country(df, country):
    """df a DataFrame with series labeled Winner and Loser
       country a str
       returns a DataFrame with all rows in which country appears
       in either the Winner or Loser column"""
    return df.loc[(df['Winner'] == country) | (df['Loser'] == country)]


def get_games(df, countries):
    return df[(df['Winner'].isin(countries)) |
              (df['Loser'].isin(countries))]

# print(2*wwc['W Goals'])
# print(wwc['W Goals'].sum())

# print(wwc[wwc['Winner'] == 'Sweden']['W Goals'].sum() +
    # wwc[wwc['Winner'] == 'Sweden']['L Goals'].sum())

# print((wwc['W Goals'].sum() - wwc['L Goals'].sum())/len(wwc['W Goals']))

# print(wwc['W Goals'].sum() + wwc['L Goals'].sum())

# print(wwc[wwc['Round'] == 'Quarters']['L Goals'].sum())

# Adding a column for goal difference
wwc['G Diff'] = wwc['W Goals'] - wwc['L Goals']

# Adding a row of totals
new_row_dict = {'Round': ['Total'],
                'W Goals': [wwc['W Goals'].sum()],
                'L Goals': [wwc['L Goals'].sum()],
                'G Diff': [wwc['G Diff'].sum()]}
# Create new DataFrame containing only that row from dict
# then pass to concat with main DataFrame
new_row = pd.DataFrame(new_row_dict)
wwc = pd.concat([wwc, new_row], sort=False).reset_index(drop=True)
print(wwc)
print("")

# print(wwc.loc[wwc['Round'] != 'Total'].corr(method='pearson'))
