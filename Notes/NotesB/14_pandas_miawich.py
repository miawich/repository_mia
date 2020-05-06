import random
from builtins import type, range

import pandas as pd

d = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data=d)
print(df['col1'])

print(df.describe())

# list > dicts > series / dataframes
s = [random.randrange(100) for x in range(10)]
my_series = pd.Series(s)
print(type(my_series))
print(my_series)

# Pandas DataFrame

d = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data=d)
print(df)


d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
cols = ["a", "b", "c"]
df2 = pd.DataFrame(data=d, columns=cols)
print(df2)

# make a df from a csv
df3 = pd.read_csv('Beach_Weather_Stations_-_Automated_Sensors.csv')
print(type(df3))

print(df3.head())  # first five rows in df
print(df3.tail(10))
print(df3.info())
print(df3.describe())

print(df3.index)
print(df3.columns)
print(df3.dtypes)

locations = (df3['Location'])
print(type(locations))

# we can slice using .iloc[]

first5_something = df3.iloc[:5, 0]
print(first5_something)

first_fifth = df3.iloc[[0, 4], [2, 3]]
print(type(first_fifth))