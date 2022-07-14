import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

# iloc: integer based selection
# Purely integer-location based indexing for selection by position.
first_three_rows = df.iloc[0:3]  # not include index 3rd
"""
   survived  pclass     sex   age  sibsp  parch     fare embarked  class  \
0         0       3    male  22.0      1      0   7.2500        S  Third   
1         1       1  female  38.0      1      0  71.2833        C  First   
2         1       3  female  26.0      0      0   7.9250        S  Third   
     who  adult_male deck  embark_town alive  alone  
0    man        True  NaN  Southampton    no  False  
1  woman       False    C    Cherbourg   yes  False  
2  woman       False  NaN  Southampton   yes   True  
"""
df.iloc[0, 0]

df.iloc[0:3, 0:3]
"""
   survived  pclass     sex
0         0       3    male
1         1       1  female
2         1       3  female
"""

# loc: label based selection
# Access a group of rows and columns by label(s) or a boolean array.
df.loc[0:3]  # include index 3rd
"""
   survived  pclass     sex   age  sibsp  parch     fare embarked  class  \
0         0       3    male  22.0      1      0   7.2500        S  Third   
1         1       1  female  38.0      1      0  71.2833        C  First   
2         1       3  female  26.0      0      0   7.9250        S  Third   
3         1       1  female  35.0      1      0  53.1000        S  First   
     who  adult_male deck  embark_town alive  alone  
0    man        True  NaN  Southampton    no  False  
1  woman       False    C    Cherbourg   yes  False  
2  woman       False  NaN  Southampton   yes   True  
3  woman       False    C  Southampton   yes  False  
"""

# Select one column and more than one row with loc
df.loc[0:3, "age"]
"""
0    22.0
1    38.0
2    26.0
3    35.0
Name: age, dtype: float64
"""

# Select more than one column with loc
col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]
"""
    age embarked alive
0  22.0        S    no
1  38.0        C   yes
2  26.0        S   yes
3  35.0        S   yes
"""
