import numpy as np

# One Dimension
a = np.random.randint(low=0, high=10, size=10)

print("One Dimensional Array: {}".format(a))

print("The first element: {}".format(a[0]))

print("The first five elements: {}".format(a[0:5]))
# Alternative:
print("The first five elements: {}".format(a[:5]))

# More than One Dimension
m = np.random.randint(low=0, high=10, size=(3, 5))

print("More Than One Dimensional Array: {}".format(m))

# m[row, column]
print("Element in the first row, firs column:{}".format(m[1, 1]))

print("Element in the second row, third column: {}".format(m[2, 3]))

# Change the value in the array
m[2, 3] = 2.9

print("More Than One Dimensional Array: {}".format(m))
# It recorded as 2, not 2.9. This is because NumPy works with fixed type.

print("First column with whole rows: {}".format(m[:, 0]))

print("Second row with whole columns: {}".format(m[1, :]))

print("First two row with first three columns: {}".format(m[0:2, 0:3]))

"""
Sample Output:
One Dimensional Array: [7 0 5 1 9 2 5 6 2 1]
The first element: 7
The first five elements: [7 0 5 1 9]
The first five elements: [7 0 5 1 9]
More Than One Dimensional Array: [[2 3 5 7 7]
                                 [5 7 7 0 5]
                                 [2 4 5 0 4]]
Element in the first row, firs column:7
Element in the second row, third column: 0
More Than One Dimensional Array: [[2 3 5 7 7]
                                 [5 7 7 0 5]
                                 [2 4 5 2 4]]
First column with whole rows: [2 5 2]
Second row with whole columns: [5 7 7 0 5]
First two row with first three columns: [[2 3 5]
                                         [5 7 7]]

"""
