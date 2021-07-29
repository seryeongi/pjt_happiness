import pandas as pd
import numpy as np


df1 = pd.read_csv('2017_result.csv')
df2 = pd.read_csv('2018_result.csv')
df3 = pd.read_csv('2019_result.csv')
df4 = pd.read_csv('2015.csv')

print(df1.info())
print(df2.info())
print(df3.info())
print(df1[df1['region'].isnull() == True])
print(df2[df2['region'].isnull() == True])
print(df3[df3['region'].isnull() == True])
print(df4['region'].unique())