# %% Why NumPy?

import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

# Without NumPy
for i in range(0, len(a)):
    ab.append(a[i] * b[i])

print(ab) # view as list

# With NumPy
a1 = np.array([1, 2, 3, 4])
b1 = np.array([2, 3, 4, 5])

print(a1 * b1) # view as ndarray


"""
Why NumPy? 
1) Speed - NumPy keeps all values in a single data type.
2) It provides high level operations (vector operations).
"""
