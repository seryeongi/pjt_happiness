import pandas as pd
import numpy as np

df1 = pd.read_csv('2015.csv')
df2 = pd.read_csv('2017.csv')
df3 = pd.read_csv('2018.csv')
df4 = pd.read_csv('2019.csv')
print(df1.columns)
df1_1 = df1[['country','region']]
df2_1 = df2[['country','rank']]
df3_1 = df3[['country','rank']]
df4_1 = df4[['country','rank']]
print(df2_1)

df1_2 = df1_1.set_index(df1_1['country'])
df2_2 = df2_1.set_index(df2_1['country'])
df3_2 = df3_1.set_index(df3_1['country'])
df4_2 = df4_1.set_index(df4_1['country'])

del df1_2['country']
del df2_2['country']
del df3_2['country']
del df4_2['country']

print(df2_2)
print(df3_2)
print(df4_2)

result2017 = pd.concat([df1_2,df2_2],axis=1)
result2018 = pd.concat([df1_2,df3_2],axis=1)
result2019 = pd.concat([df1_2,df4_2],axis=1)
print(result2017.shape)
print(result2017.info())
print(result2018.info())
print(result2019.info())

result2017.to_excel('./2017.xlsx')
result2018.to_excel('./2018.xlsx')
result2019.to_excel('./2019.xlsx')
