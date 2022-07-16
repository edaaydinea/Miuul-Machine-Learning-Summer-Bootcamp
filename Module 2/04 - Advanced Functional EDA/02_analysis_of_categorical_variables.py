import matplotlib.pyplot as plt
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

df["embarked"].value_counts()
"""
S    644
C    168
Q     77
Name: embarked, dtype: int64
"""

df["sex"].unique()
"""array(['male', 'female'], dtype=object)"""

df["class"].nunique()
"""3"""

df.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 15 columns):
 #   Column       Non-Null Count  Dtype   
---  ------       --------------  -----   
 0   survived     891 non-null    int64   
 1   pclass       891 non-null    int64   
 2   sex          891 non-null    object  
 3   age          714 non-null    float64 
 4   sibsp        891 non-null    int64   
 5   parch        891 non-null    int64   
 6   fare         891 non-null    float64 
 7   embarked     889 non-null    object  
 8   class        891 non-null    category
 9   who          891 non-null    object  
 10  adult_male   891 non-null    bool    
 11  deck         203 non-null    category
 12  embark_town  889 non-null    object  
 13  alive        891 non-null    object  
 14  alone        891 non-null    bool    
dtypes: bool(2), category(2), float64(2), int64(4), object(5)
memory usage: 80.7+ KB

"""

categorical = ["category", "object", "bool"]
numeric = ["int64", "float64"]

categorical_cols = [col for col in df.columns if str(df[col].dtypes) in categorical]
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

numerical_cols = [col for col in df.columns if str(df[col].dtypes) in numeric]
"""
survived      2
pclass        3
age          88
sibsp         7
parch         7
fare        248
dtype: int64
"""

"""
Nominal data: Conveys identity (labeled)
    Examples: - sex,
              - preferred type of chocolate
              - blood type
              - color
"""
nominal_data = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in numeric]
"""
['survived', 'pclass', 'sibsp', 'parch']
"""

"""
Cardinal numbers: - Conveys quantity (counted + discrete)
                  - The numbers that are used for counting. It helps us to know how many elements are there.
                  - Tall (12oz), Grande(16oz), Venti (20oz)
"""
cardinal_data = [col for col in df.columns if df[col].nunique() > 20 and df[col].dtypes in ["category", "object"]]
"""
[]
"""

categorical_cols += nominal_data
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

categorical_cols = [col for col in categorical_cols if col not in cardinal_data]

df[categorical_cols].nunique()
"""
sex            2
embarked       3
class          3
who            3
adult_male     2
deck           7
embark_town    3
alive          2
alone          2
dtype: int64
"""

[col for col in df.columns if col not in categorical_cols]
"""
['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare']
"""

df["survived"].value_counts()
"""
0    549
1    342
Name: survived, dtype: int64
"""

100 * df["survived"].value_counts() / len(df)
"""
0    61.616162
1    38.383838
Name: survived, dtype: float64
"""


def cat_summary(dataframe, col_name):
    print(pd.DataFrame(data={col_name.capitalize(): dataframe[col_name].value_counts(),
                             "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))

    print("##########################################")


cat_summary(dataframe=df, col_name="sex")

"""
        Sex      Ratio
male    577  64.758698
female  314  35.241302
##########################################
"""

for col in categorical_cols:
    cat_summary(dataframe=df, col_name=col)
"""
        Sex      Ratio
male    577  64.758698
female  314  35.241302
##########################################
   Embarked      Ratio
S       644  72.278339
C       168  18.855219
Q        77   8.641975
##########################################
        Class      Ratio
Third     491  55.106622
First     216  24.242424
Second    184  20.650954
##########################################
       Who      Ratio
man    537  60.269360
woman  271  30.415264
child   83   9.315376
##########################################
       Adult_male     Ratio
True          537  60.26936
False         354  39.73064
##########################################
   Deck     Ratio
C    59  6.621773
B    47  5.274972
D    33  3.703704
E    32  3.591470
A    15  1.683502
F    13  1.459035
G     4  0.448934
##########################################
             Embark_town      Ratio
Southampton          644  72.278339
Cherbourg            168  18.855219
Queenstown            77   8.641975
##########################################
     Alive      Ratio
no     549  61.616162
yes    342  38.383838
##########################################
       Alone     Ratio
True     537  60.26936
False    354  39.73064
##########################################
   Survived      Ratio
0       549  61.616162
1       342  38.383838
##########################################
   Pclass      Ratio
3     491  55.106622
1     216  24.242424
2     184  20.650954
##########################################
   Sibsp      Ratio
0    608  68.237935
1    209  23.456790
2     28   3.142536
4     18   2.020202
3     16   1.795735
8      7   0.785634
5      5   0.561167
##########################################
   Parch      Ratio
0    678  76.094276
1    118  13.243547
2     80   8.978676
5      5   0.561167
3      5   0.561167
4      4   0.448934
6      1   0.112233
##########################################
"""


def categorical_data_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({
        col_name.capitalize(): dataframe[col_name].value_counts(),
        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)
    }))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        if "_" not in str(col_name):
            plt.savefig("{} Count Plot.png".format(str(col_name.capitalize())))
            plt.show()
        if "_" in str(col_name):
            words = col_name.split("_")
            new_col_name = words[0].capitalize() + " " + "_".join(map(lambda x: x.capitalize(), words[1:]))
            plt.savefig("{} Count Plot.png".format(str(new_col_name)))
            plt.show()


categorical_data_summary(dataframe=df, col_name="sex", plot=True)
categorical_data_summary(dataframe=df, col_name="embark_town", plot=True)

if __name__ == '__main__':
    for col in categorical_cols:
        if df[col].dtypes == "bool":
            df[col] = df[col].astype(int)
            categorical_data_summary(dataframe=df, col_name=col, plot=True)
        else:
            categorical_data_summary(dataframe=df, col_name=col, plot=True)

"""
        Sex      Ratio
male    577  64.758698
female  314  35.241302
##########################################
             Embark_town      Ratio
Southampton          644  72.278339
Cherbourg            168  18.855219
Queenstown            77   8.641975
##########################################
        Sex      Ratio
male    577  64.758698
female  314  35.241302
##########################################
   Embarked      Ratio
S       644  72.278339
C       168  18.855219
Q        77   8.641975
##########################################
        Class      Ratio
Third     491  55.106622
First     216  24.242424
Second    184  20.650954
##########################################
       Who      Ratio
man    537  60.269360
woman  271  30.415264
child   83   9.315376
##########################################
   Adult_male     Ratio
1         537  60.26936
0         354  39.73064
##########################################
   Deck     Ratio
C    59  6.621773
B    47  5.274972
D    33  3.703704
E    32  3.591470
A    15  1.683502
F    13  1.459035
G     4  0.448934
##########################################
             Embark_town      Ratio
Southampton          644  72.278339
Cherbourg            168  18.855219
Queenstown            77   8.641975
##########################################
     Alive      Ratio
no     549  61.616162
yes    342  38.383838
##########################################
   Alone     Ratio
1    537  60.26936
0    354  39.73064
##########################################
   Survived      Ratio
0       549  61.616162
1       342  38.383838
##########################################
   Pclass      Ratio
3     491  55.106622
1     216  24.242424
2     184  20.650954
##########################################
   Sibsp      Ratio
0    608  68.237935
1    209  23.456790
2     28   3.142536
4     18   2.020202
3     16   1.795735
8      7   0.785634
5      5   0.561167
##########################################
   Parch      Ratio
0    678  76.094276
1    118  13.243547
2     80   8.978676
5      5   0.561167
3      5   0.561167
4      4   0.448934
6      1   0.112233
##########################################
"""
