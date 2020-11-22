# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# our simple csv file
file_path = "../data/GDP_Poland_neighbours.csv"
file_path = "../data/GDP_Poland_neighbours_simple.csv"
# %%
# create dataframe, read_csv data

df = pd.read_csv(file_path,
                 na_values=['..'],
                 nrows=16,
                #  skipfooter=5,
                #  index_col=False
                 )
#, ,index_col=False , nrows=16  
# %%
df
# %%
df_pivot = pd.pivot_table(df,
    index=["Series Name", 'Country Code'],
    dropna=False)
# %%
df_pivot.loc['GDP (current US$)'].T.plot()
df_pivot.loc['GDP per capita (current US$)'].T.plot()
# %%