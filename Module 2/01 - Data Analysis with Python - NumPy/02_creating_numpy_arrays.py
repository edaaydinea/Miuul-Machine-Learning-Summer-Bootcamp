import numpy as np

data = np.array([1, 2, 3, 4, 5])
type(data)  # numpy.ndarray

np.zeros(shape=10, dtype=int)  # array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

np.random.randint(low=0, high=10, size=10)  # array([3, 9, 1, 2, 8, 2, 6, 9, 7, 4])

np.random.normal(loc=10, scale=4, size=(3, 4))
# array([[12.93276633,  8.2925641 ,  2.87486528,  7.37008176],
#        [10.76305641, 10.09857524, 15.1625159 , 16.81538996],
#        [ 6.67914782,  5.51060426,  7.14061236, 10.94524169]])
