import pandas as pd
df = pd.read_csv('C:\BigdataProjects\BigdataService_team1\project01\data\data_standard.csv',
                 index_col='year')
print(df)
df2 = df.copy()
print(df['region'].unique())

df2 = df.replace(['Western Europe','Central and Eastern Europe','Commonwealth of Independent States'],'Europe')
df2 = df2.replace(['Eastern Asia','Southeastern Asia','Southern Asia','Southeast Asia','East Asia','South Asia'],'Asia')
df2 = df2.replace(['Australia and New Zealand'],'Oceania')
df2 = df2.replace([ 'Sub-Saharan Africa', 'Middle East and North Africa', 'Middle East and Northern Africa'],'Africa')
df2 = df2.replace(['North America and ANZ'],'North America')
df2 = df2.replace(['Latin America and Caribbean'],'South America')

print(df2)
print(df2['region'].unique())
df2.to_csv('./data_sorted.csv')