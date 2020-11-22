#%%
import pandas as pd
import numpy as np


### We add this import!
import matplotlib.pyplot as plt

np.random.seed(1024)

#%%

# plot siple time series data
ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('1/1/2020', periods=1000))
part_sum = ts.cumsum()
part_sum.plot()
plt.show()


#%%
# plot 4 plots, each for one column
df = pd.DataFrame(
    np.random.randn(1000, 4),
    index=pd.date_range('1/1/2020', periods=1000, freq='30min'),
    columns=list('ABCD'))
df.head()

#%%
df_cum = df.cumsum()
print(df.head())
#df_cum.plot()

#%% other types of plots

row1 = df.iloc[0]
row2_6 = df.iloc[1:6]
print(row2_6)

#row1.plot(kind='bar')

# row2_6.plot(kind='bar')
# plt.axhline(0, color='k')
#plt.show()

#%% 
bar_stacked = pd.DataFrame(np.random.rand(6, 4),
                    columns=['a', 'b', 'c', 'd'])

bar_stacked.plot.bar(stacked=True,
                    title="Bar stacked plot");

bar_stacked.plot.barh(stacked=True);
plt.show()

# %%

df_part = pd.DataFrame(
    np.random.randn(1000, 4),
    index=pd.date_range('1/1/2020', periods=30 freq='30min'),
    columns=list('ABCD'))

df_part[['A', 'B']]+=5

group1 = df_part.plot.scatter(x='A',y='B',color="blue", label='grupa 1')

df_part.plot.scatter(x='C',y='D',color="red", label='grupa 2', ax=group1)