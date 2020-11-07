# author: Krzysztof Sopyła (krzysztofsopyla@gmail.com)
# Twitter: ksopyla
# Blog: https://ksopyla.com
# If you want to use this material in your own training please let me know.

#todo:

- sorting
- argsort
- argmax

#%% sorting
a = np.array([[1,4],[3,1]])
np.sort(a)  # sort along the last axis

#%%
np.sort(a, axis=None)     # sort the flattened array
#%%
np.sort(a, axis=0)  # sort along the first axis



#%% argsort

x = np.array([3, 1, 2])
np.argsort(x)

#%%

x = np.array([[0, 3], [2, 2]])

ind = np.argsort(x, axis=0)  # sorts along first axis (down)
ind


np.take_along_axis(x, ind, axis=0)  # same as np.sort(x, axis=0)

#%%

a = np.arange(6).reshape(2,3) + 10

#%%
np.argmax(a)

np.argmax(a, axis=0)

np.argmax(a, axis=1)
