import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df.groupby("sex")["age"].mean()
"""
sex
female    27.915709
male      30.726645
Name: age, dtype: float64
"""

df.groupby("sex").agg({"age": "mean"})
"""
              age
sex              
female  27.915709
male    30.726645
"""

df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})
"""
              age            survived
             mean       sum      mean
sex                                  
female  27.915709   7286.00  0.742038
male    30.726645  13919.17  0.188908
"""

df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                                        "survived": ["mean"]})
"""
                          age  survived
                         mean      mean
sex    embark_town                     
female Cherbourg    28.344262  0.876712
       Queenstown   24.291667  0.750000
       Southampton  27.771505  0.689655
male   Cherbourg    32.998841  0.305263
       Queenstown   30.937500  0.073171
       Southampton  30.291440  0.174603
"""

df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                                                 "survived": ["mean"]})
"""
                                 age  survived
                                mean      mean
sex    embark_town class                      
female Cherbourg   First   36.052632  0.976744
                   Second  19.142857  1.000000
                   Third   14.062500  0.652174
       Queenstown  First   33.000000  1.000000
                   Second  30.000000  1.000000
                   Third   22.850000  0.727273
       Southampton First   32.704545  0.958333
                   Second  29.719697  0.910448
                   Third   23.223684  0.375000
male   Cherbourg   First   40.111111  0.404762
                   Second  25.937500  0.200000
                   Third   25.016800  0.232558
       Queenstown  First   44.000000  0.000000
                   Second  57.000000  0.000000
                   Third   28.142857  0.076923
       Southampton First   41.897188  0.354430
                   Second  30.875889  0.154639
                   Third   26.574766  0.128302
"""
df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                                                 "survived": ["mean"],
                                                 "sex": ["count"]})
"""
                                 age  survived   sex
                                mean      mean count
sex    embark_town class                            
female Cherbourg   First   36.052632  0.976744    43
                   Second  19.142857  1.000000     7
                   Third   14.062500  0.652174    23
       Queenstown  First   33.000000  1.000000     1
                   Second  30.000000  1.000000     2
                   Third   22.850000  0.727273    33
       Southampton First   32.704545  0.958333    48
                   Second  29.719697  0.910448    67
                   Third   23.223684  0.375000    88
male   Cherbourg   First   40.111111  0.404762    42
                   Second  25.937500  0.200000    10
                   Third   25.016800  0.232558    43
       Queenstown  First   44.000000  0.000000     1
                   Second  57.000000  0.000000     1
                   Third   28.142857  0.076923    39
       Southampton First   41.897188  0.354430    79
                   Second  30.875889  0.154639    97
                   Third   26.574766  0.128302   265

"""
