import seaborn as sns

df = sns.load_dataset("titanic")

# Return the first `n` rows.
print(df.head(3))
"""
   survived  pclass     sex   age  ...  deck  embark_town  alive  alone
0         0       3    male  22.0  ...   NaN  Southampton     no  False
1         1       1  female  38.0  ...     C    Cherbourg    yes  False
2         1       3  female  26.0  ...   NaN  Southampton    yes   True
[3 rows x 15 columns]
"""

# Return the last `n` rows.
print(df.tail(3))
"""
     survived  pclass     sex   age  ...  deck  embark_town  alive  alone
888         0       3  female   NaN  ...   NaN  Southampton     no  False
889         1       1    male  26.0  ...     C    Cherbourg    yes   True
890         0       3    male  32.0  ...   NaN   Queenstown     no   True
[3 rows x 15 columns]
"""

# Return a tuple representing the dimensionality of the DataFrame.
print(df.shape)
"""
(891, 15)
"""

# Return information of the DataFrame
print(df.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 15 columns):
 #   Column       Non-Null Count  Dtype   
---  ------       --------------  -----   
 0   survived     891 non-null    int64   
 1   pclass       891 non-null    int64   (int64 = Numerical Data - Integer)
 2   sex          891 non-null    object  (object = Categorical Data)
 3   age          714 non-null    float64 (float64 = Numerical Data - Decimal)
 4   sibsp        891 non-null    int64   
 5   parch        891 non-null    int64   
 6   fare         891 non-null    float64 
 7   embarked     889 non-null    object  
 8   class        891 non-null    category (category = Categorical Data - expressed categorically.)
 9   who          891 non-null    object  
 10  adult_male   891 non-null    bool    (bool = Categorical Data)
 11  deck         203 non-null    category
 12  embark_town  889 non-null    object  
 13  alive        891 non-null    object  
 14  alone        891 non-null    bool    
dtypes: bool(2), category(2), float64(2), int64(4), object(5)
memory usage: 80.7+ KB
None
"""

# Return columns' names
print(df.columns)
"""
Index(['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
       'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
       'alive', 'alone'],
      dtype='object')
      """

# Return index information of the DataFrame
print(df.index)
"""
RangeIndex(start=0, stop=891, step=1)
"""

# Generate descriptive statistics.
# DataFrame.count: Count number of non-NA/null observations.
#         DataFrame.max: Maximum of the values in the object.
#         DataFrame.min: Minimum of the values in the object.
#         DataFrame.mean: Mean of the values.
#         DataFrame.std: Standard deviation of the observations.

# For numeric data, the result's index will include ``count``,
#         ``mean``, ``std``, ``min``, ``max`` as well as lower, ``50`` and
#         upper percentiles. By default the lower percentile is ``25`` and the
#         upper percentile is ``75``. The ``50`` percentile is the
#         same as the median.
#
#         For object data (e.g. strings or timestamps), the result's index
#         will include ``count``, ``unique``, ``top``, and ``freq``. The ``top``
#         is the most common value. The ``freq`` is the most common value's
#         frequency. Timestamps also include the ``first`` and ``last`` items.

print(df.describe())
"""
         survived      pclass         age       sibsp       parch        fare
count  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
mean     0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
std      0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
min      0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
25%      0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
50%      0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
75%      1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
max      1.000000    3.000000   80.000000    8.000000    6.000000  512.329200
"""

# Return True/False if there is a missing data in the DataFrame
print(df.isnull().values.any())
"""
True
"""

# Returns the missing status in variables.
print(df.isnull().sum())
"""
urvived         0
pclass           0
sex              0
age            177
sibsp            0
parch            0
fare             0
embarked         2
class            0
who              0
adult_male       0
deck           688
embark_town      2
alive            0
alone            0
dtype: int64
"""

# Return head of the determined variable
print(df["sex"].head())
"""
0      male
1    female
2    female
3    female
4      male
Name: sex, dtype: object
"""

# Return a Series containing counts of unique values.
print(df["sex"].value_counts())
"""
male      577
female    314
Name: sex, dtype: int64
"""
