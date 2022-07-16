import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

categorical_columns = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
"""
['sex',
 'embarked',
 'class',
 'who',
 'adult_male',
 'deck',
 'embark_town',
 'alive',
 'alone']
"""

nominal_columns = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
"""['survived', 'pclass', 'sibsp', 'parch']"""

cardinal_columns = [col for col in df.columns if
                    df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
"""
[]
"""
categorical_columns = categorical_columns + nominal_columns
"""
['sex',
 'embarked',
 'class',
 'who',
 'adult_male',
 'deck',
 'embark_town',
 'alive',
 'alone',
 'survived',
 'pclass',
 'sibsp',
 'parch']
"""
categorical_columns = [col for col in categorical_columns if col not in cardinal_columns]

df[["age", "fare"]].describe().T
"""
      count       mean        std   min      25%      50%   75%       max
age   714.0  29.699118  14.526497  0.42  20.1250  28.0000  38.0   80.0000
fare  891.0  32.204208  49.693429  0.00   7.9104  14.4542  31.0  512.3292
"""

numerical_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
numerical_cols = [col for col in numerical_cols if col not in categorical_columns]
"""
['age', 'fare']
"""


def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)


num_summary(df, "age")
"""
count    714.000000
mean      29.699118
std       14.526497
min        0.420000
5%         4.000000
10%       14.000000
20%       19.000000
30%       22.000000
40%       25.000000
50%       28.000000
60%       31.800000
70%       36.000000
80%       41.000000
90%       50.000000
95%       56.000000
99%       65.870000
max       80.000000
Name: age, dtype: float64
"""


def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.savefig("{} Histogram Graph.png".format(numerical_col.capitalize()))
        plt.show(block=True)


num_summary(df, "age", plot=True)

for col in numerical_cols:
    num_summary(df, col, plot=True)
