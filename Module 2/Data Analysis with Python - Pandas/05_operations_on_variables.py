import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)

df = sns.load_dataset("titanic")
df.head()
"""
   survived  pclass     sex   age  sibsp  parch     fare embarked  class  \
0         0       3    male  22.0      1      0   7.2500        S  Third   
1         1       1  female  38.0      1      0  71.2833        C  First   
2         1       3  female  26.0      0      0   7.9250        S  Third   
3         1       1  female  35.0      1      0  53.1000        S  First   
4         0       3    male  35.0      0      0   8.0500        S  Third   
     who  adult_male deck  embark_town alive  alone  
0    man        True  NaN  Southampton    no  False  
1  woman       False    C    Cherbourg   yes  False  
2  woman       False  NaN  Southampton   yes   True  
3  woman       False    C  Southampton   yes  False  
4    man        True  NaN  Southampton    no   True  
"""

"age" in df
"""True"""

df["age"].head()
"""
0    22.0
1    38.0
2    26.0
3    35.0
4    35.0
Name: age, dtype: float64
"""

# Return pandas Series
type(df["age"].head())
"""Out[10]: pandas.core.series.Series"""

# Return Pandas DataFrame
type(df[["age"]].head())
"""Out[11]: pandas.core.frame.DataFrame"""

df[["age", "alive"]]
"""
      age alive
0    22.0    no
1    38.0   yes
2    26.0   yes
3    35.0   yes
4    35.0    no
..    ...   ...
886  27.0    no
887  19.0   yes
888   NaN    no
889  26.0   yes
890  32.0    no
[891 rows x 2 columns]
"""

col_names = ["age", "embarked", "alive"]
df[col_names]
"""
      age embarked alive
0    22.0        S    no
1    38.0        C   yes
2    26.0        S   yes
3    35.0        S   yes
4    35.0        S    no
..    ...      ...   ...
886  27.0        S    no
887  19.0        S   yes
888   NaN        S    no
889  26.0        C   yes
890  32.0        Q    no
[891 rows x 3 columns]
"""

# Add new column to the dataframe
df["age2"] = df["age"] ** 2

df["age3"] = df["age"] / df["age2"]

# Delete a column from the dataframe
df.drop("age3", axis=1).head()

# Delete more than one column from the dataframe
df.drop(col_names, axis=1).head()

# Drop columns whose name contains a specific string from pandas DataFrame

# First Solution
age_filter = df.filter(regex="age")
"""
Out[24]: 
      age    age2      age3
0    22.0   484.0  0.045455
1    38.0  1444.0  0.026316
2    26.0   676.0  0.038462
3    35.0  1225.0  0.028571
4    35.0  1225.0  0.028571
..    ...     ...       ...
886  27.0   729.0  0.037037
887  19.0   361.0  0.052632
888   NaN     NaN       NaN
889  26.0   676.0  0.038462
890  32.0  1024.0  0.031250
[891 rows x 3 columns]
"""

df.drop(list(age_filter), axis=1)

# Second Solution
#  loc: Access a group of rows and columns by label(s) or a boolean array.
df.loc[:, ~df.columns.str.contains("age")].head()
"""
~: means not symbol (everything else except choice)
df.columns: select all columns
df.columns.str: select columns names as string
df.columns.str.contains("age"): select columns whose name contains "age"
[select all rows: select all columns] --> 
    If you don't write anything before colon, this means that you want to select all rows.
    If you don't write anything after colon, this means that you want to select all columns.
"""
