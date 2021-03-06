#%%

import numpy as np
import pandas as pd


s = pd.Series([1,2,3,'foo',4,np.nan,'bar'])


#%%

# Creating a DataFrame by passing a numpy array, with an index and labeled columns:
dates = pd.date_range('20200101', periods=6,freq="D")


#%%
df = pd.DataFrame(np.random.randn(6,4), 
                  index=dates, 
                  columns=['imie','nazwisko','wiek','miasto'])

df


#%%
# Creating a DataFrame by passing a dict of objects that can be converted to series-like.
df2 = pd.DataFrame( { 'A' : 1.0,
                     'B' : pd.Timestamp('20201126'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' } )

# check column types
print(df2.dtypes)


#%%
# Viewing Data

df.head()
df.tail(5)

# Display the index, columns, and the underlying numpy data
print(df.index)

print(df.columns)

print(df.values)

# Describe shows a quick statistic summary of your data
df.describe()

#%%
# Transposition
print(df.T)

# sorting
df.sort_index(axis=1, ascending=False)
#%%
df.sort_values(by='B')


# %%
