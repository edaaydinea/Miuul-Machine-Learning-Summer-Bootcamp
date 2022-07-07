#######################
# Create a dictionary which has a list in the value part and string in the key part.
# Do this for the values which have numerical variables.
#######################

# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}

import seaborn as sns

data_frame = sns.load_dataset("car_crashes")

num_columns = [column for column in data_frame.columns if data_frame[column].dtype != "0"]
agg_list = ["mean", "min", "max", "sum"]

new_dict = {column: agg_list for column in num_columns}
print(new_dict)

data_frame[num_columns].agg(new_dict)
