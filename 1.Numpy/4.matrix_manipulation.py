# author: Krzysztof Sopyła (krzysztofsopyla@gmail.com)
# Twitter: ksopyla
# Blog: http://ksopyla.com

# If you want to use this material in your own trainning please let me know.

# Numpy docs https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.array-manipulation.html

import numpy as np


a1 = np.arange(0,24,step=1)
print(a1)

# reshape matrix a1 into (2,12) matrix, 
a2 = np.reshape(a1,(2,12))
print(a2)

a1[0] = 12345
print(a2)
# assing correct value as was before
a1[0] = 0

a3 = np.reshape(a2,(3,8))
print(a3)
a4 = np.reshape(a2,(4,6))
print(a4)
a5 = np.reshape(a2,(6,4))
print(a5)



a1 = np.ones((3,3))
a2 = np.ones((8,3))*2
a3 = np.ones((3,7))*3

# Join a sequence of arrays along an existing axis
# https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.concatenate.html#numpy.concatenate
np.concatenate((a1,a2))

# ValueError: all the input array dimensions except for the concatenation axis must match exactly
# np.concatenate((a1,a3))

np.concatenate((a1,a3), axis=1)


# stack - Join a sequence of arrays along a new axis.
#  https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.stack.html#numpy.stack

v1 = np.arange(1,5)
v2 = np.arange(5,9)
print(v1)
print(v2)

vv = np.stack((v1,v2),axis=0)
vh = np.stack((v1,v2),axis=1)
print(vv)
print(vh)

# stack in 3d
a = np.reshape(np.arange(1,9),(2,4))
b = np.reshape(np.arange(1,9),(2,4))+10


# one matrix on top of another
#    ___________
#   /          /
#  /          /
# /__________/
#    ___________
#   /          /
#  /          /
# /__________/

ab0 = np.stack((a,b),axis=0)
print(ab0)
print(ab0.shape)
print(ab0[0,:,:])

# one matrix behind another
#         ____________
#        |            |
#  ______|_____       |
# |            |      |
# |            |______|
# |            |
# |____________|

ab1 = np.stack((a,b),axis=1)
print(ab1)
print(ab1.shape)
print(ab1[0,:,:])

# one matrix next to another
#
#    /|    /|
#   / |   / |
#  /  |  /  |
# |   | |   |
# |  /  |  /
# | /   | /
# |/    |/

ab2 = np.stack((a,b),axis=2)
print(ab2)
print(ab2.shape)
print(ab2[0,:,:])