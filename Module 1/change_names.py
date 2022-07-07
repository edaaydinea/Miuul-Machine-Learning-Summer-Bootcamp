import seaborn as sns

data_frame = sns.load_dataset("car_crashes")

# Solution 1
# for column in data_frame.columns:
#     print(column.upper())

# Solution 2

data_frame.columns = [column.upper() for column in data_frame.columns]

print(data_frame.columns)
