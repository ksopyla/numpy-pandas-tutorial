#%%

import pandas as pd
import numpy as np

from io import StringIO


# our simple csv file
file_path = "./3.Pandas/simple_data.csv"
#%%
# create dataframe, read_csv data

dt = pd.read_csv(file_path)
dt

#%% choose columns 

dt = pd.read_csv(file_path, usecols=['Imie', 'wiek'])
print(dt.head())

#%% parse and cast data to special format
dt = pd.read_csv(file_path,
                usecols=['Imie', 'wiek'],
                dtype={'wiek': np.int16})
print(dt.head())

#%% 
def imie_converter(imie):
    return imie*5

file_path = "./3.Pandas/simple_data.csv"
dt = pd.read_csv(file_path,
                usecols=['Imie', 'wiek'],
                dtype={'Imie': str, 'wiek': np.int8},
                converters={"Imie":imie_converter}
                )