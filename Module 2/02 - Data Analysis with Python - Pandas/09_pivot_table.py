import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

"""
First element of pivot table: value - Write down what you want to see at the intersection.
Second element of pivot table: index - Write what you want to see on the row.
Third element of pivot table: columns - Write what you want to see on the column.

The default value of Pivot Table is mean.
"""

df.pivot_table(values="survived",
               index="sex",
               columns="embarked")
"""
embarked         C         Q         S
sex                                   
female    0.876712  0.750000  0.689655
male      0.305263  0.073171  0.174603
"""

df.pivot_table(values="survived",
               index="sex",
               columns=["embarked", "class"])

"""
embarked         C                      Q                          S  
class        First Second     Third First Second     Third     First   Second     Third  
sex                                                                    
female    0.976744    1.0  0.652174   1.0    1.0  0.727273  0.958333   0.910448  0.375000 
male      0.404762    0.2  0.232558   0.0    0.0  0.076923  0.354430   0.154639  0.128302                     
"""

# Converting numerical data to categorical data
"""
cut(): If you know which categories you want to divide the numeric variable into, you can use the cut() function.
qcut(): If you don't know which categories you want to divide the numeric variable into, you can use the qcut() 
function.
"""

df["new_age"] = pd.cut(x=df["age"],
                       bins=[0, 10, 18, 25, 40, 90])

df.pivot_table(values="survived",
               index="sex",
               columns=["new_age"])

"""
new_age   (0, 10]  (10, 18]  (18, 25]  (25, 40]  (40, 90]
sex                                                      
female   0.612903  0.729730  0.759259  0.802198  0.770833
male     0.575758  0.131579  0.120370  0.220930  0.176471
"""

df.pivot_table(values="survived",
               index="sex",
               columns=["new_age", "class"])
"""
new_age (0, 10]                   (10, 18]                   (18, 25]                      (25, 40]                      (40, 90]                    
class     First Second     Third     First Second     Third     First    Second     Third     First    Second     Third     First    Second     Third
sex                                                                                                                                                  
female      0.0    1.0  0.500000  1.000000    1.0  0.523810  0.941176  0.933333  0.500000  1.000000  0.906250  0.464286  0.961538  0.846154  0.111111
male        1.0    1.0  0.363636  0.666667    0.0  0.103448  0.333333  0.047619  0.115385  0.513514  0.071429  0.172043  0.280000  0.095238  0.064516
"""

# It is used to see the output in the Python Console without going to the bottom line.
pd.set_option('display.width', 500)
