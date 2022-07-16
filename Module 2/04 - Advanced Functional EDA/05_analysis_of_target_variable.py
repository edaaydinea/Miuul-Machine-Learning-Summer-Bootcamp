import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)


def categorical_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name.capitalize(): dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


def grab_col_names(dataframe, categorical_threshold=10, cardinal_threshold=30):
    """
    It gives the names of categorical, numerical and categorical but cardinal variables in the data set.

    Parameters
    ----------
    dataframe: dataframe
        This variable is the dataframe whose names are to be retrieved.
    categorical_threshold : int, float
        Class threshold value for numeric but categorical variables'
    cardinal_threshold: int, float
        Class threshold value for categorical but cardinal variables'

    Returns
    -------
    categorical_cols: list
        Categorical variable list
    numerical_cols: list
        Numerical variable list
    cardinal_cols: list
        Cardinal variable list

    Notes
    -----
    categorical_cols + numerical_cols + cardinal_cols = total numer of variables
    nominal_cols inside categorical_cols
    """

    categorical_cols = [col for col in dataframe.columns if
                        str(dataframe[col].dtypes) in ["category", "object", "bool"]]

    nominal_cols = [col for col in dataframe.columns if
                    dataframe[col].nunique() < 10 and dataframe[col].dtypes in ["int64", "float64"]]

    cardinal_cols = [col for col in dataframe.columns if
                     dataframe[col].nunique() > 20 and str(dataframe[col].dtypes) in ["category", "object"]]

    categorical_cols = categorical_cols + nominal_cols
    categorical_cols = [col for col in categorical_cols if col not in cardinal_cols]

    numerical_cols = [col for col in dataframe.columns if dataframe[col].dtypes in ["int64", "float64"]]
    numerical_cols = [col for col in numerical_cols if col not in categorical_cols]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'Categorical Columns: {len(categorical_cols)}')
    print(f'Numerical Columns: {len(numerical_cols)}')
    print(f'Cardinal Columns: {len(cardinal_cols)}')
    print(f'Nominal Columns: {len(nominal_cols)}')

    return categorical_cols, numerical_cols, cardinal_cols


categorical_cols, numerical_cols, cardinal_cols = grab_col_names(df)
"""
Observations: 891
Variables: 15
Categorical Columns: 13
Numerical Columns: 2
Cardinal Columns: 0
Nominal Columns: 4
"""

df["survived"].value_counts()
"""
0    549
1    342
Name: survived, dtype: int64
"""

categorical_summary(dataframe=df, col_name="survived")
"""
   Survived      Ratio
0       549  61.616162
1       342  38.383838
"""

# Analysis of Target Variable with Categorical Data

df.groupby("sex")["survived"].mean()


def target_summary_with_categorical_data(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}), end="\n\n\n")


target_summary_with_categorical_data(dataframe=df, target="survived", categorical_col="pclass")
"""
        TARGET_MEAN
pclass             
1          0.629630
2          0.472826
3          0.242363
"""

for col in categorical_cols:
    target_summary_with_categorical_data(dataframe=df, target="survived", categorical_col=col)

# Analysis of Target Variable with Numerical Data

df.groupby("survived")["age"].mean()
"""
survived
0    30.626179
1    28.343690
Name: age, dtype: float64
"""

df.groupby("survived").agg({"age": "mean"})
"""
                age
survived           
0         30.626179
1         28.343690
"""


def target_summary_with_numerical_data(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")


target_summary_with_numerical_data(df, "survived", "age")

for col in numerical_cols:
    target_summary_with_numerical_data(df, "survived", col)
