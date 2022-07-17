import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.info()


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
                    dataframe[col].nunique() < categorical_threshold and dataframe[col].dtypes in ["int64", "float64"]]

    cardinal_cols = [col for col in dataframe.columns if
                     dataframe[col].nunique() > cardinal_threshold and str(dataframe[col].dtypes) in ["category",
                                                                                                      "object"]]

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


def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")


for col in categorical_cols:
    cat_summary(df, col)


def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title("{} Histogram Graph.png".format(numerical_col.capitalize()))
        plt.show(block=True)


for col in numerical_cols:
    num_summary(df, col, plot=True)

# BONUS
df = sns.load_dataset("titanic")
df.info()

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

cat_cols, num_cols, cat_but_car = grab_col_names(df)


def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


for col in cat_cols:
    cat_summary(df, col, plot=True)

for col in num_cols:
    num_summary(df, col, plot=True)
