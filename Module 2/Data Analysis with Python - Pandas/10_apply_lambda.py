import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

# Without apply method
df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 5

for col in df.columns:
    if "age" in col:
        print((df[col] / 10).head())

for col in df.columns:
    if "age" in col:
        df[col] = df[col] / 10

# With apply method
df[["age", "age2", "age3"]].apply(lambda x: x / 10).head()
"""
    age  age2  age3
0  0.22  0.44  1.10
1  0.38  0.76  1.90
2  0.26  0.52  1.30
3  0.35  0.70  1.75
4  0.35  0.70  1.75
"""

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x / 10).head()
"""
    age  age2  age3
0  0.22  0.44  1.10
1  0.38  0.76  1.90
2  0.26  0.52  1.30
3  0.35  0.70  1.75
4  0.35  0.70  1.75
"""

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()
"""
        age      age2      age3
0 -0.530005 -0.530005 -0.530005
1  0.571430  0.571430  0.571430
2 -0.254646 -0.254646 -0.254646
3  0.364911  0.364911  0.364911
4  0.364911  0.364911  0.364911
"""


# Use function with apply method
def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()


df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()
"""
        age      age2      age3
0 -0.530005 -0.530005 -0.530005
1  0.571430  0.571430  0.571430
2 -0.254646 -0.254646 -0.254646
3  0.364911  0.364911  0.364911
4  0.364911  0.364911  0.364911
"""

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.head()
"""
   survived  pclass     sex       age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone      age2      age3
0         0       3    male -0.530005      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False -0.530005 -0.530005
1         1       1  female  0.571430      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False  0.571430  0.571430
2         1       3  female -0.254646      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True -0.254646 -0.254646
3         1       1  female  0.364911      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False  0.364911  0.364911
4         0       3    male  0.364911      0      0   8.0500        S  Third    man        True  NaN  Southampton    no   True  0.364911  0.364911
"""
