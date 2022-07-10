# Conditions on NumPy

import numpy as np

v = np.array([1, 2, 3, 4, 5])

print("v: {}".format(v))  # v: [1 2 3 4 5]

# %%
# With loop
ab = []
for i in v:
    if i < 3:
        ab.append(i)

print("ab array: {}".format(ab))  # ab array: [1, 2]

# %%
# With NumPy

print("Elements smaller than 3 in v numpy array: {}".format(v[v < 3]))
# Elements smaller than 3 in v array: [1 2]
