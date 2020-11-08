# based on http://cs231n.github.io/python-numpy-tutorial/

# If you want to use this material in your own trainning please let me know.
#%%

import numpy as np

x = np.array([1, 2])  # Let numpy choose the datatype
print( x.dtype)         # Prints "int64"

x = np.array([1., 2.])  # Let numpy choose the datatype
print( x.dtype)             # Prints "float64"

x = np.array([1, 127], dtype=np.int8)  # Force a particular datatype
print(x.dtype)       

#%%
x = np.array([1, 128], dtype=np.int8)  # Force a particular datatype
print(x)       



#%% basic math operation
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

#%% Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))

#%% Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)

print(np.subtract(x, y))

#%% Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))

#%% Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))


#%% 
# list of math functions https://numpy.org/doc/stable/reference/routines.math.html

#%% Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print( np.sqrt(x))


#%% vector matrix operation
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

#%% Inner product of vectors; both produce 219
print( v.dot(w))
print( np.dot(v, w))

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))



#%%
x = np.array([[1,2],[3,4]])

print(x)
print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))# Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"


#%%
print(np.mean(x))  # Compute mean of all elements;
print(np.mean(x, axis=0))# Compute mean of each column;
print(np.mean(x, axis=1))  # Compute mean of each row; 

#%%
print(np.std(x))          # Compute standard derivation of all elements;
print(np.std(x, axis=0))  # Compute standard derivation of each column;
print(np.std(x, axis=1))  # Compute standard derivation of each row; 


#%%
x = np.array([[1,2], [3,4]])
print(x)    # Prints "[[1 2]
           #          [3 4]]"
print(x.T)  # Prints "[[1 3]
           #          [2 4]]"

#%% Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1,2,3])
print(v)  # Prints "[1 2 3]"
print(v.T)  # Prints "[1 2 3]"


# generate linear map from (-pi/2, pi/2)
x = np.linspace(-np.pi/2,np.pi/2,10)

# calculate sine and cosine in one step, for whole array
print(np.sin(x))

print(np.cos(x))

# [-5, ... , 5]
x = np.arange(-5,5)

#%% calcultae e^(-5), .... , e^5
print(np.exp(x))

#%% x^2, compute x to power of 2 
print(np.power(x,2))

# using python operators compute each element of matrix x to power of 2
print(x**2)

# calculate 2^-5 ... 2^5, !!! error, integer not allowed negative exponent
print(np.power(2,x))

# now everything works as expected :)
x = np.arange(-5,5, dtype=np.float)

# natural logarithm, look at minus values!!
print(np.log(x))

xx = np.power(2,x)
print(xx)

# logarithm base 2
print(np.log2(xx))
