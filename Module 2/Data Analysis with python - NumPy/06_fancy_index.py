"""
Fancy Indexing

It means passing an array of indices to access multiple array elements at once.

Resource: Python Data Science Handbook by Jake VanderPlas.
"""

import numpy as np

v = np.arange(start=0, stop=30, step=3)
print("v : {}".format(v))

# Fancy Indexing
catch = [1, 2, 3]
print("Get the second, third, fourth elements from numpy array: {}".format(v[catch]))

print("Get the fifth, sixth elements from numpy array: {}".format([v[5], v[6]]))

"""
Sample Output:
v : [ 0  3  6  9 12 15 18 21 24 27]
Get the second, third, fourth elements from numpy array: [3 6 9]
Get the fifth, sixth elements from numpy array: [15, 18]
"""
