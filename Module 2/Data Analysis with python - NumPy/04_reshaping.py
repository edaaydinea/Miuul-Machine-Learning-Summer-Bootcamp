"""
numpy.reshape(a, newshape, order='C')
- Returns an array containing the same data with a new shape.
- Gives a new shape to an array without changing its data

:param a :  array_like
            Array to be reshaped.

:param newshape: int or tuple of ints
                 The new shape should be compatible with the original shape.
                 If an integer, then the result will be a 1-D array of that length.
                 One shape dimension can be -1. In this case,the value is inferred from the length of the array and remaining dimensions.


:param order : {‘C’, ‘F’, ‘A’}, optional
               Read the elements of a using this index order, and place the elements into the reshaped array using this index order.
               ‘C’ means to read / write the elements using C-like index order, with the last axis index changing fastest, back to the first axis index changing slowest.
               ‘F’ means to read / write the elements using Fortran-like index order, with the first index changing fastest, and the last index changing slowest.
               Note that the ‘C’ and ‘F’ options take no account of the memory layout of the underlying array, and only refer to the order of indexing.
               ‘A’ means to read / write the elements in Fortran-like index order if a is Fortran contiguous in memory, C-like order otherwise.
"""
import numpy as np

a = np.random.randint(low=1, high=10, size=9)
# Example output: array([2, 2, 3, 7, 4, 5, 4, 9, 1])

b = a.reshape(3, 3)
# Example output: array([[2, 2, 3],
#                       [7, 4, 5],
#                       [4, 9, 1]])
