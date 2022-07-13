import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
"""
Output:
Out[8]: 
   survived  pclass     sex   age  ...  deck  embark_town  alive  alone
0         0       3    male  22.0  ...   NaN  Southampton     no  False
1         1       1  female  38.0  ...     C    Cherbourg    yes  False
2         1       3  female  26.0  ...   NaN  Southampton    yes   True
3         1       1  female  35.0  ...     C  Southampton    yes  False
4         0       3    male  35.0  ...   NaN  Southampton     no   True
[5 rows x 15 columns]
"""

index_ = df.index

slice = df[0:13]  # 0 includes, 13 doesn't include

# Drop specified labels from rows or columns.
"""
Parameters
        ----------
        labels : single label or list-like
            Index or column labels to drop. A tuple will be used as a single
            label and not treated as a list-like.
        axis : {0 or 'index', 1 or 'columns'}, default 0
            Whether to drop labels from the index (0 or 'index') or
            columns (1 or 'columns').
        index : single label or list-like
            Alternative to specifying axis (``labels, axis=0``
            is equivalent to ``index=labels``).
        columns : single label or list-like
            Alternative to specifying axis (``labels, axis=1``
            is equivalent to ``columns=labels``).
        level : int or level name, optional
            For MultiIndex, level from which the labels will be removed.
        inplace : bool, default False
            If False, return a copy. Otherwise, do operation
            inplace and return None.
        errors : {'ignore', 'raise'}, default 'raise'
            If 'ignore', suppress error and only existing labels are
            dropped.
"""

df.drop(0, axis=0).head()  # delete the first row
"""
Out[11]: 
   survived  pclass     sex   age  ...  deck  embark_town  alive  alone
1         1       1  female  38.0  ...     C    Cherbourg    yes  False
2         1       3  female  26.0  ...   NaN  Southampton    yes   True
3         1       1  female  35.0  ...     C  Southampton    yes  False
4         0       3    male  35.0  ...   NaN  Southampton     no   True
5         0       3    male   NaN  ...   NaN   Queenstown     no   True
[5 rows x 15 columns]
"""

# If we want to delete more than one rows from the data frame,
delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head(10)
"""
Out[13]: 
    survived  pclass     sex   age  ...  deck  embark_town  alive  alone
0          0       3    male  22.0  ...   NaN  Southampton     no  False
2          1       3  female  26.0  ...   NaN  Southampton    yes   True
4          0       3    male  35.0  ...   NaN  Southampton     no   True
6          0       1    male  54.0  ...     E  Southampton     no   True
8          1       3  female  27.0  ...   NaN  Southampton    yes  False
9          1       2  female  14.0  ...   NaN    Cherbourg    yes  False
10         1       3  female   4.0  ...     G  Southampton    yes  False
11         1       1  female  58.0  ...     C  Southampton    yes   True
12         0       3    male  20.0  ...   NaN  Southampton     no   True
13         0       3    male  39.0  ...   NaN  Southampton     no  False
[10 rows x 15 columns]
"""

# If we want to use delete function permanently in the data frame,
# First solution
# df2 = df.drop(delete_indexes, axis=0)

# Second solution
# df.drop(delete_indexes, axis=0, inplace=True)
# If inplace equals to False, return a copy. Otherwise, do operation inplace and return None.


# %%
#######################
# Converting a variable to an Index
#######################

df["age"].head()
df.age.head()
"""
Output:
Out[5]: 
0    22.0
1    38.0
2    26.0
3    35.0
4    35.0
Name: age, dtype: float64
"""
df.index = df["age"]

df.drop("age", axis=1).head()  # Delete age column (axis = 1))
"""
Out[17]: 
   survived  pclass     sex  sibsp  ...  deck  embark_town alive  alone
0         0       3    male      1  ...   NaN  Southampton    no  False
1         1       1  female      1  ...     C    Cherbourg   yes  False
2         1       3  female      0  ...   NaN  Southampton   yes   True
3         1       1  female      1  ...     C  Southampton   yes  False
4         0       3    male      0  ...   NaN  Southampton    no   True
[5 rows x 14 columns]
"""

df.drop("age", axis=1, inplace=True)
df.head()
"""
Out[19]: 
   survived  pclass     sex  sibsp  ...  deck  embark_town alive  alone
0         0       3    male      1  ...   NaN  Southampton    no  False
1         1       1  female      1  ...     C    Cherbourg   yes  False
2         1       3  female      0  ...   NaN  Southampton   yes   True
3         1       1  female      1  ...     C  Southampton   yes  False
4         0       3    male      0  ...   NaN  Southampton    no   True
[5 rows x 14 columns]
"""

# %%
#######################
# Converting Index to Variable
#######################

df.index
"""Out[9]: 
Float64Index([22.0, 38.0, 26.0, 35.0, 35.0,  nan, 54.0,  2.0, 27.0, 14.0,
              ...
              33.0, 22.0, 28.0, 25.0, 39.0, 27.0, 19.0,  nan, 26.0, 32.0],
             dtype='float64', name='age', length=891)"""

df["age"] = df.index

df.head()
"""
      survived  pclass     sex  sibsp  ...  embark_town  alive  alone   age
age                                    ...                                 
22.0         0       3    male      1  ...  Southampton     no  False  22.0
38.0         1       1  female      1  ...    Cherbourg    yes  False  38.0
26.0         1       3  female      0  ...  Southampton    yes   True  26.0
35.0         1       1  female      1  ...  Southampton    yes  False  35.0
35.0         0       3    male      0  ...  Southampton     no   True  35.0
[5 rows x 15 columns]
"""

df.drop("age", axis=1, inplace=True)
"""
Reset the index, or a level of it.
Reset the index of the DataFrame, and use the default one instead.
If the DataFrame has a MultiIndex, this method can remove one or more
levels.
"""
df.reset_index().head()
"""
Out[14]: 
    age  survived  pclass     sex  ...  deck  embark_town  alive  alone
0  22.0         0       3    male  ...   NaN  Southampton     no  False
1  38.0         1       1  female  ...     C    Cherbourg    yes  False
2  26.0         1       3  female  ...   NaN  Southampton    yes   True
3  35.0         1       1  female  ...     C  Southampton    yes  False
4  35.0         0       3    male  ...   NaN  Southampton     no   True
[5 rows x 15 columns]
"""
df = df.reset_index()
df.head()
"""
Out[16]: 
    age  survived  pclass     sex  ...  deck  embark_town  alive  alone
0  22.0         0       3    male  ...   NaN  Southampton     no  False
1  38.0         1       1  female  ...     C    Cherbourg    yes  False
2  26.0         1       3  female  ...   NaN  Southampton    yes   True
3  35.0         1       1  female  ...     C  Southampton    yes  False
4  35.0         0       3    male  ...   NaN  Southampton     no   True
[5 rows x 15 columns]
"""
