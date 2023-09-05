# -*- coding: utf-8 -*-
import pandas as pd

# Creates an empty DataFrame
# print(pd.DataFrame())

# Pass a list to create a new non-empty DataFrame
rounds = ['Semis', 'Semis', '3rd Place', 'Championship']
teams = ['USA', 'Netherlands', 'Sweden', 'USA']
# print(pd.DataFrame(rounds))

# Passing as a dict instead of list, will add descriptive "Rounds" heading to column
# print(pd.DataFrame({'Round':rounds}))

# Creating a new DataFrame with multiple columns, labeled
df = pd.DataFrame({'Round': rounds, 'Winner': teams})
# print(df)

# mutate df to add extra column "W Goals"
df['W Goals'] = [2, 1, 0, 0]
# print(df)

# replace values under "W Goals" column
df['W Goals'] = [2, 1, 2, 2]
# print(df)

# delete a column
# without specifying "axis='columns'" it would default to rows, axis=0
print(df.drop('Winner', axis='columns'))
# print("")

# use inplace to mutate df rather than returning a copied DataFrame (more efficient)
df.drop('Winner', axis='columns', inplace=True)
# print(df)
# print("")

quarters_dict = {'Round': ['Quarters']*4,
                 'Winner': ['England', 'USA', 'Netherlands', 'Sweden'],
                 'W Goals': [3, 2, 2, 2]}

df = pd.concat([pd.DataFrame(quarters_dict), df], sort=False)
# print(df.reset_index(drop = True))
