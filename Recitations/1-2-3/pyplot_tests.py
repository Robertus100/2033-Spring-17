# Slicing
import numpy as np

x = np.array([1, 2, 3])
y = np.array([2, 4, 6])

X = np.array([[ 1, 2, 3], [4, 5, 6]])
Y = np.array([[ 2, 4, 6], [8, 10, 12]])


x[2]    # 3
x[0:2]  # array([1, 2])

x + y  # elementwise addition = array([3, 6, 9])

X[:,1]  # second column of X: array([2, 5])


print(Y[1, :])  # second row of Y: [ 8, 10, 12]

print( X[:, 1] + Y[:, 2] )

print( X[1] == X[1,:] )

## Questions (Check what the following statements return)
x = np.array([1,2,5])
x[1:2]

a = np.array([1,2])
b = np.array([3,4,5])
a + b                     # can not be added - arrays of different shapes


# Indexing NumPy Arrays
z1 = np.array([1,3,5,7,9])
z2 = z1 + 1

ind = [0, 2, 3]
z1[ind]

ind1 = np.array( [0, 2, 3] )
z1[ind1]

# can also use logical indexing
z1 > 6

z1[ z1 > 6 ]
z2[ z1 > 6 ]

ind = z1 > 6
z1[ind]

# important: slicing arrays (using colon) returns a view of the array, while logical indexing returns a copy of it.
# First consider slicing:
z1 = np.array([1,3,5,7,9])
w = z1[0:3]
print(w)

w[0] = 33
print(w)
print(z1)

# Next, consider logical indexing
z1 = np.array([1,3,5,7,9])
ind = np.array([0, 1, 2])

w = z1[ind]
print(w)

w[0] = 555
print(w)

print(z1)

# Questions - what is returned?
# 1
a = np.array([1,2])
b = np.array([3,4,5])
b[a]

# 2
c = b[1:]
b[a] is c

# Building and Examining NumPy Arrays

x = np.random.random(10)
np.any(x > 0.9)
np.any(x > 0.5)

np.all(x > 0.5)
np.all(x > 0.05)


# Questions:
# 1 What does the following do? (Ans: Finds whether x is prime.)
x=20
not np.any([x%i == 0 for i in range(2, x)])


# Matplotlib and pyplot

import matplotlib.pyplot as plt
plt.plot([0,1,4,9,16])

plt.plot([0,1,2],[0,1,4],"rd-")


