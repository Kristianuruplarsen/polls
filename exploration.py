import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('polls.csv')

df['date'] = pd.to_datetime((df.year*10000+df.month*100+df.day).apply(str),format='%Y%m%d')

not_parties = ['id','pollingfirm','year','month','day','n', 'source', 'date']
parties = [c for c in df.columns if c not in not_parties]

corr = {}
for y in range(2010,2019):
    ddf = df.loc[df['year'] == y]
    corr[y] = ddf.drop(['id', 'pollingfirm','year','month','day','n','source'], axis = 1).corr()


for part in parties:
    df2 = pd.concat(corr).reset_index(level = 0)

    for p in parties:
        sns.regplot('level_0', p, df2[df2.index == part], order = 1)
        plt.title(part)
        plt.show()





cor = df.drop(['id', 'pollingfirm','year','month','day','n','source'], axis = 1).corr()

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(100, 200, as_cmap=True)

corr

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

plt.show()
