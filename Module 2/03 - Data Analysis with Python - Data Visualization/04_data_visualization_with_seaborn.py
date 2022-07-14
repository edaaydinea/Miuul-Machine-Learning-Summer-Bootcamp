import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("tips")
df.head()
"""
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
"""

# Categorical Data Visualization

df["sex"].value_counts()
sns.countplot(x=df["sex"], data=df)
plt.savefig("Categorical Data (Sex) Visualization with Countplot.png")
plt.show()

df["sex"].value_counts().plot(kind="bar")
plt.savefig("Categorical Data (Sex) Visualization with Bar Plot")
plt.show()

# Numerical Data Visualization

sns.boxplot(x=df["total_bill"])
plt.savefig("Numerical Data (Total Bill) Visualization with Box Plot")
plt.show()

df["total_bill"].hist()
plt.savefig("Numerical Data (Total Bill) Visualization with Histogram")
plt.show()
