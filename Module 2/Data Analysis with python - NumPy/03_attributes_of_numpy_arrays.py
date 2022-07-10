import numpy as np

"""
ndim: Number of array dimensions - boyut sayısı
shape : Tuple of array dimensions - boyut bilgisi
size: Number of elements in the array - toplam eleman sayısı
dtype: Data-type of the array's elements - array veri tipi
"""

a = np.random.randint(low=0, high=10, size=5)  # Alternative if low equals to 0 : a = np.random.randint(10,size=5)
"""
If you don't add the number for the low part, the numpy will understand that low number starts from 0. 
If you want to start the low part with a specific number, you must notify that number to numpy.
"""

print("Number of array dimensions {}".format(a.ndim))
print("Tuple of array dimensions: {}".format(a.shape))
print("Number of elements in the array: {}".format(a.size))
print("Data-type of the array's elements: {}".format(a.dtype))

"""
Output: 
Number of array dimensions 1
Tuple of array dimensions: (5,)
Number of elements in the array: 5
Data-type of the array's elements: int32
"""
