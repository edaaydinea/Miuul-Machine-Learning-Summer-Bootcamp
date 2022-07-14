import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head()
"""
    survived  pclass     sex   age  sibsp  parch     fare embarked   class  \
6          0       1    male  54.0      0      0  51.8625        S   First   
11         1       1  female  58.0      0      0  26.5500        S   First   
15         1       2  female  55.0      0      0  16.0000        S  Second   
33         0       2    male  66.0      0      0  10.5000        S  Second   
54         0       1    male  65.0      0      1  61.9792        C   First   
      who  adult_male deck  embark_town alive  alone  
6     man        True    E  Southampton    no   True  
11  woman       False    C  Southampton   yes   True  
15  woman       False  NaN  Southampton   yes   True  
33    man        True  NaN  Southampton    no   True  
54    man        True    B    Cherbourg    no  False 
"""

df[df["age"] > 50]["age"].count()
"""64"""

df.loc[df["age"] > 50, ["age", "class"]].head()
"""
     age   class
6   54.0   First
11  58.0   First
15  55.0  Second
33  66.0  Second
54  65.0   First
"""

df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()
"""
     age   class
6   54.0   First
33  66.0  Second
54  65.0   First
94  59.0   Third
96  71.0   First
"""

df["embark_town"].value_counts()
"""
Southampton    644
Cherbourg      168
Queenstown      77
Name: embark_town, dtype: int64
"""

df_new = df.loc[(df["age"] > 50)
                & (df["sex"] == "male")
                & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
                ["age", "class", "embark_town"]]

"""
      age   class  embark_town
6    54.0   First  Southampton
33   66.0  Second  Southampton
54   65.0   First    Cherbourg
94   59.0   Third  Southampton
96   71.0   First    Cherbourg
124  54.0   First  Southampton
150  51.0  Second  Southampton
152  55.5   Third  Southampton
155  51.0   First    Cherbourg
170  61.0   First  Southampton
174  56.0   First    Cherbourg
222  51.0   Third  Southampton
232  59.0  Second  Southampton
249  54.0  Second  Southampton
252  62.0   First  Southampton
262  52.0   First  Southampton
317  54.0  Second  Southampton
326  61.0   Third  Southampton
406  51.0   Third  Southampton
438  64.0   First  Southampton
449  52.0   First  Southampton
456  65.0   First  Southampton
467  56.0   First  Southampton
487  58.0   First    Cherbourg
492  55.0   First  Southampton
493  71.0   First    Cherbourg
545  64.0   First  Southampton
555  62.0   First  Southampton
570  62.0  Second  Southampton
582  54.0  Second  Southampton
587  60.0   First    Cherbourg
625  61.0   First  Southampton
630  80.0   First  Southampton
631  51.0   Third  Southampton
647  56.0   First    Cherbourg
659  58.0   First    Cherbourg
672  70.0  Second  Southampton
684  60.0  Second  Southampton
694  60.0   First  Southampton
695  52.0  Second  Southampton
714  52.0  Second  Southampton
745  70.0   First  Southampton
851  74.0   Third  Southampton
857  51.0   First  Southampton
"""

df_new["embark_town"].value_counts()
"""
Southampton    35
Cherbourg       9
Name: embark_town, dtype: int64
"""
