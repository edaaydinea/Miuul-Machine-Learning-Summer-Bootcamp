# Import Libraries
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("titanic")
df.head()
"""
   survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False
1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True
3         1       1  female  35.0      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False
4         0       3    male  35.0      0      0   8.0500        S  Third    man        True  NaN  Southampton    no   True
"""

df.tail()
"""
     survived  pclass     sex   age  sibsp  parch   fare embarked   class    who  adult_male deck  embark_town alive  alone
886         0       2    male  27.0      0      0  13.00        S  Second    man        True  NaN  Southampton    no   True
887         1       1  female  19.0      0      0  30.00        S   First  woman       False    B  Southampton   yes   True
888         0       3  female   NaN      1      2  23.45        S   Third  woman       False  NaN  Southampton    no  False
889         1       1    male  26.0      0      0  30.00        C   First    man        True    C    Cherbourg   yes   True
890         0       3    male  32.0      0      0   7.75        Q   Third    man        True  NaN   Queenstown    no   True
"""


def check_dataframe(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("\n##################### Types #####################")
    print(dataframe.dtypes)
    print("\n##################### Head #####################")
    print(dataframe.head(head))
    print("\n##################### Tail #####################")
    print(dataframe.tail(head))
    print("\n##################### NA #####################")
    print(dataframe.isnull().sum())
    print("\n##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


check_dataframe(dataframe=df)

"""
##################### Shape #####################
(891, 15)

##################### Types #####################
survived          int64
pclass            int64
sex              object
age             float64
sibsp             int64
parch             int64
fare            float64
embarked         object
class          category
who              object
adult_male         bool
deck           category
embark_town      object
alive            object
alone              bool
dtype: object

##################### Head #####################
   survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False
1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True
3         1       1  female  35.0      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False
4         0       3    male  35.0      0      0   8.0500        S  Third    man        True  NaN  Southampton    no   True

##################### Tail #####################
     survived  pclass     sex   age  sibsp  parch   fare embarked   class    who  adult_male deck  embark_town alive  alone
886         0       2    male  27.0      0      0  13.00        S  Second    man        True  NaN  Southampton    no   True
887         1       1  female  19.0      0      0  30.00        S   First  woman       False    B  Southampton   yes   True
888         0       3  female   NaN      1      2  23.45        S   Third  woman       False  NaN  Southampton    no  False
889         1       1    male  26.0      0      0  30.00        C   First    man        True    C    Cherbourg   yes   True
890         0       3    male  32.0      0      0   7.75        Q   Third    man        True  NaN   Queenstown    no   True

##################### NA #####################
survived         0
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
##################### Quantiles #####################
          count       mean        std   min    0%     5%      50%        95%        99%      100%       max
survived  891.0   0.383838   0.486592  0.00  0.00  0.000   0.0000    1.00000    1.00000    1.0000    1.0000
pclass    891.0   2.308642   0.836071  1.00  1.00  1.000   3.0000    3.00000    3.00000    3.0000    3.0000
age       714.0  29.699118  14.526497  0.42  0.42  4.000  28.0000   56.00000   65.87000   80.0000   80.0000
sibsp     891.0   0.523008   1.102743  0.00  0.00  0.000   0.0000    3.00000    5.00000    8.0000    8.0000
parch     891.0   0.381594   0.806057  0.00  0.00  0.000   0.0000    2.00000    4.00000    6.0000    6.0000
fare      891.0  32.204208  49.693429  0.00  0.00  7.225  14.4542  112.07915  249.00622  512.3292  512.3292

"""

df = sns.load_dataset("flights")
check_dataframe(dataframe=df)

"""
##################### Shape #####################
(144, 3)

##################### Types #####################
year             int64
month         category
passengers       int64
dtype: object

##################### Head #####################
   year month  passengers
0  1949   Jan         112
1  1949   Feb         118
2  1949   Mar         132
3  1949   Apr         129
4  1949   May         121

##################### Tail #####################
     year month  passengers
139  1960   Aug         606
140  1960   Sep         508
141  1960   Oct         461
142  1960   Nov         390
143  1960   Dec         432

##################### NA #####################
year          0
month         0
passengers    0
dtype: int64

##################### Quantiles #####################
            count         mean         std     min      0%      5%     50%      95%      99%    100%     max
year        144.0  1954.500000    3.464102  1949.0  1949.0  1949.0  1954.5  1960.00  1960.00  1960.0  1960.0
passengers  144.0   280.298611  119.966317   104.0   104.0   121.6   265.5   488.15   585.79   622.0   622.0
"""
