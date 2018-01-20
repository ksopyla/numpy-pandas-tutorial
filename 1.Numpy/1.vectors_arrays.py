# author: Krzysztof Sopyła (krzysztofsopyla@gmail.com)
# Twitter: ksopyla
# Blog: http://ksopyla.com

# If you want to use this material in your own trainning please let me know.

import numpy as np


# vector creation
v1 = np.arange(1,10)
print("v1={}".format(v1))

v2 = np.arange(1,10,step=0.5)
print("v2={}".format(v2))


v3 = np.linspace(0,10,num=10)
print("v3={}".format(v3))
v3 = np.linspace(0,10,num=10,endpoint=False)
print("v3={}".format(v3))


v4 = np.linspace(0,10,num=11,endpoint=True)
print("v4={}".format(v4))


# check size == shape
print(v1.shape)
print(v2.shape)
print(v3.shape)
print(v4.shape)


# matrix ceation

a1 = np.array([1,2,3,4]) # Create a rank 1 array
print("a1={}".format(a1))
print(type(a1))            # Prints "<type 'numpy.ndarray'>"
print("a1 shape={}".format(a1.shape))


a2 = np.array([[1,2,3,4], [5,6,7,8]])
print("a2={}".format(a2))
print("a2 shape={}".format(a2.shape))


a3 = np.zeros((2,2))      # Create an array of all zeros
print("a3={}".format(a3)) # Prints "[[ 0.  0.]
                          #          [ 0.  0.]]"
    
a4 = np.ones((3,2))       # Create an array of all ones
print("a4={}".format(a4)) 


a5 = np.eye(2)        # Create a 2x2 identity matrix
print("a5={}".format(a5)) 
    
a6 = np.random.random((2,2)) # Create an array filled with random values
print("a6={}".format(a6))    # Might print "[[ 0.91940167  0.08143941]
                             #               [ 0.68744134  0.87236687]]"

a7 = np.full((5,3), 7)  # Create a constant array
print("a7={}".format(a7)) 


# 3d arrays, wgrrrrrrr!
b1 = np.array([ 
                [ [1, 2], [3, 4], [5, 6] ],
                [ [11, 12], [13, 14], [15, 16] ],
                [ [21, 22], [23, 24], [25, 26] ],
                [ [31, 32], [33, 34], [35, 36] ],
              ])

# 
#                 axis2
#            _____________ 
#           /            /|
#   axis1  /            / |
#         /            /  |
#        /____________/   |
#       |             |   |
#       |             |   /
# axis0 |             |  /
#       |             | /
#       |_____________|/


print("b1={}".format(b1))
print("b1 shape={}".format(b1.shape))
# help me, my brain is melting
print(b1[0,:,:].shape)
print(b1[0,:,:])

print(b1[:,0,:].shape)
print(b1[:,0,:])

print(b1[:,:,0].shape)
print(b1[:,:,0])

# play with indexes

# 5,2,3