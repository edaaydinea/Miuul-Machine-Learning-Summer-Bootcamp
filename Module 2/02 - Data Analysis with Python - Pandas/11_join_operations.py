import numpy as np
import pandas as pd

m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

# Concat two different data frame
pd.concat([df1, df2])

# Concat two different data frame by ignoring index
# axis : {0/'index', 1/'columns'}, default 0
pd.concat([df1, df2], ignore_index=True)

# Join with Merge Operations
df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
"""
  employees        group  start_date
0      john   accounting        2009
1    dennis  engineering        2014
2      mark  engineering        2010
3     maria           hr        2019
"""
pd.merge(df1, df2, on="employees")
"""
  employees        group  start_date
0      john   accounting        2009
1    dennis  engineering        2014
2      mark  engineering        2010
3     maria           hr        2019
"""

# Purpose: We want to access the information of each employee's manager.

df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})
pd.merge(df3, df4)
"""
  employees        group  start_date  manager
0      john   accounting        2009    Caner
1    dennis  engineering        2014  Mustafa
2      mark  engineering        2010  Mustafa
3     maria           hr        2019  Berkcan
"""
