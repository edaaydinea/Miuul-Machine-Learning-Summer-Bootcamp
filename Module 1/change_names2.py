import seaborn as sns

data_frame = sns.load_dataset("car_crashes")

data_frame.columns = ["FLAG_" + column if "INS" in column else "NO_FLAG_" + column for column in data_frame.columns]

print(data_frame.columns)
