# -*- coding: utf-8 -*-
import pandas as pd
wwc = pd.read_csv('wwc2019_q-f.csv')
# print(wwc)

# for i in wwc.index:
#     print(i)

# print(wwc.columns)
# for c in wwc.columns:
#     print(c)

# print(wwc.values)

# print(wwc['Winner'])

winners = ''
for w in wwc['Winner']:
    winners += w + ','
# print(winners)

wGoals, lGoals = 0, 0
for goal in wwc['W Goals']:
    wGoals += goal
for goal in wwc['L Goals']:
    lGoals += goal
# print(f"The winners scored a total of {wGoals} goals, and the losers scored a total of {lGoals} goals.")

# print(wwc[['Winner', 'Loser']])

# print(wwc.loc[3])

# print(wwc.loc[[1, 3, 5]])

# print(wwc.loc[::2])

# print(wwc.loc[0:2, 'Round':'L Goals':2])

# print(wwc.loc[1:2])

# print(wwc.groupby(['Loser', 'Round']).mean())

# print(wwc.loc[wwc['Winner'] == 'Sweden'])
# print(wwc.loc[(wwc['Winner'] == 'Sweden') | (wwc['Loser'] == 'Sweden')])
# print(wwc.loc[((wwc['Winner'] == 'USA') & (wwc['Loser'] != 'France')) | ((wwc['Loser'] == 'USA') & (wwc['Winner'] != 'France'))])


def get_country(df, country):
    """df a DataFrame with series labeled Winner and Loser
       country a str
       returns a DataFrame with all rows in which country appears
       in either the Winner or Loser column"""
    return df.loc[(df['Winner'] == country) | (df['Loser'] == country)]

# print(get_country(get_country(wwc, 'Sweden'), 'Germany'))


def get_games(df, countries):
    return df[(df['Winner'].isin(countries)) |
              (df['Loser'].isin(countries))]

# print(get_games(wwc, ['USA', 'England']))

# print(get_games(wwc, ['Sweden']))


print(get_games(get_country(wwc, 'Sweden'), ['Germany', 'Netherlands']))
