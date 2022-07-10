# Basic Mathematical Operations

import numpy as np

v = np.array([1, 2, 3, 4, 5])
print("V array: {}".format(v))

# Addition
print("Add 5 to all elements of the V array: {}".format(np.add(v, 5)))

# Subtraction
print("Subtract 5 from all elements of the V array: {}".format(np.subtract(v, 5)))

# Division
print("All elements of the V array division by 5: {}".format(np.divide(v, 5)))

# Multiplication
print("All elements of the V array multiply by 5: {}".format(np.multiply(v, 5)))

# Squaring
print("Square all elements of the V array: {}".format(np.square(v)))

# Mean
print("Mean of V array: {}".format(np.mean(v)))

# Summation
print("Sum of all elements in V array: {}".format(np.sum(v)))

# Minimum element
print("Minimum element in V array: {}".format(np.min(v)))

# Maximum element
print("Maximum element in V array: {}".format(np.max(v)))

# Variance
print("Variance in V array: {}".format(np.var(v)))

"""
Output: 
V array: [1 2 3 4 5]
Add 5 to all elements of the V array: [ 6  7  8  9 10]
Subtract 5 from all elements of the V array: [-4 -3 -2 -1  0]
All elements of the V array division by 5: [0.2 0.4 0.6 0.8 1. ]
All elements of the V array multiply by 5: [ 5 10 15 20 25]
Square all elements of the V array: [ 1  4  9 16 25]
Mean of V array: 3.0
Sum of all elements in V array: 15
Minimum element in V array: 1
Maximum element in V array: 5
Variance in V array: 2.0
"""

# %%
# Equation Solution with Two Unknowns

# 5 * x0 + x1 = 12
# x0 + 3 * x1 = 10

import numpy as np

a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])

result = np.linalg.solve(a, b)

print("Result: {}".format(result))
# Result: [1.85714286 2.71428571]
