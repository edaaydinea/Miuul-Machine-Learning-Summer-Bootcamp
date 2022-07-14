import pandas as pd

series = pd.Series(data=[10, 77, 12, 4, 5])
print("Pandas series: \n{}".format(series))

print("Type of series: {}".format(type(series)))

print("Index information: {}".format(series.index))

print("Type information of the variables in the series: {}".format(series.dtype))

print("Number of elements in the series: {}".format(series.size))

print("Dimension information of the series: {}".format(series.ndim))
# Pandas series has a one dimension. This does not change from data to data.

print("Variables of the series: {}".format(series.values))

print("Type of series.values output: {}".format(type(series.values)))
# This result equals to numpy array. Because when the values method is added after the pandas series, pandas changes
# the array to numpy array. Because it is here said that Pandas does not care about data indexing.

print("The first 3 variables of the series:\n{}".format(series.head(3)))

print("The last 3 variables of the series:\n{}".format(series.tail(3)))

"""
Output:
Pandas series: 
0    10
1    77
2    12
3     4
4     5
dtype: int64

Type of series: <class 'pandas.core.series.Series'>

Index information: RangeIndex(start=0, stop=5, step=1)

Type information of the variables in the series: int64

Number of elements in the series: 5

Dimension information of the series: 1

Variables of the series: [10 77 12  4  5]

Type of series.values output: <class 'numpy.ndarray'>

The first 3 variables of the series:
0    10
1    77
2    12
dtype: int64

The last 3 variables of the series:
2    12
3     4
4     5
dtype: int64
"""
