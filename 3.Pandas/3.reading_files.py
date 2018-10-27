import pandas as pd
import numpy as np

from io import StringIO


# our simple csv file
data = '''col1,col2,col3,col4
a,b,1,
a,b,2, "foo"
c,d,3, "bar"
'''

# create dataframe, read_csv data
dt = pd.read_csv(StringIO(data))
print(dt.head())

# choose columns 

dt = pd.read_csv(StringIO(data), usecols=['col1', 'col3'])
print(dt.head())

# parse and cast data to special format
dt = pd.read_csv(StringIO(data), usecols=['col1', 'col3'], dtype={'col3': np.float})
print(dt.head())

