#%%

import pandas as pd
import numpy as np

# Creating a DataFrame by passing a numpy array, with an index and labeled columns:
dates = pd.date_range('20200101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

#%%

## Selection
df['A']

df[0:3]

# Selection by Label
df.loc[dates[0]]

# get all the indexes and only two columns
df.loc[:,['A','B']]

# you can use slicing on index
df.loc['20200102':'20200104',['A','B']]

# if you want particular value
df.loc[dates[0],'A']

#%% Selection by Position

# choose third row
df.iloc[3]

# acting similar to numpy/python
df.iloc[3:5,0:2]

df.iloc[[1,2,4],[0,2]]
df.iloc[1:3,:]


# Boolean Indexing
df[df.A > 0]

df2 = df.copy()
# easily add new columne, be carefuly and look at shapes
df2['E'] = ['one', 'one','two','three','four','three']

# get from the set of values
df2[df2['E'].isin(['two','four'])]