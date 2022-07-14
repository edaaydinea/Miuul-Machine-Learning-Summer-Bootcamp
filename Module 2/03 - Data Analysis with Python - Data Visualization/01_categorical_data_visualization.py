import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

"""
Categorical Data --> count-plot bar, pie chart
Numerical Data --> Histogram, Boxplot (also shows outliers)
"""

# Categorical Data Visualization

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

df['sex'].value_counts().plot(kind='bar')
plt.savefig("Sex - Categorical Data Visualization.png")
plt.show()
