"""
Course: Miuul Machine Learning Summer Bootcamp
Topic: Project Solution of Module 1
Author: Eda AYDIN
"""
# %%
# Mission 1:
# Examine the data structures of the given values.

x = 8
y = 3.3
z = 8j + 18
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {
    "Name": "Jake",
    "Age": 22,
    "Address": "Downtown"
}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine learning", "Data Science"}

variables = [x, y, z, b, c, l, d, t, s]
variable_names = ["x", "y", "z", "b", "c", "l", "d", "t", "s"]

results = [type(x) for x in variables]

for names, types in zip(variable_names, results):
    print("Variable name: {}, type: {}".format(names, types))

# %%
# Mission 2:
# Capitalize all letters of the given string expression.
# Replace comma with space, separate word by word
import string

text = "The goal is to turn data into information, and information into insight."

new_text = [word.strip(string.punctuation).upper() for word in text.split()]

# %%
# Mission 3: Apply the following steps to the given list.
# Step1: See the number of elements from the given list.
# Step2: Call the elements in the zeroth and tenth index.
# Step3: From the given list["D", "A", "T", "A"] create a list.
# Step4: Delete the element in the eighth index.
# Step5: Add a new element.
# Step6: Repeat the "N" element in the eighth index.

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Step 1
print("Number of elements: {}".format(len(lst)))

# Step 2
print("First element : {} , last element: {}".format(lst[0], lst[-1]))

# Step 3
first_word = [x for x in lst[0:4]]

# Step 4
del lst[8]
print(lst)

# Step 5
lst.append("!")
print(lst)

# Step 6
lst.insert(8, "N")
print(lst)

# %%
# Mission 4: Perform the following steps on the given dictionary structure.
# Step1: Access the key values.
# Step2: Access the values.
# Step3: Update the value 12 of the Daisy key to 13.
# Step4: Add a new value whose key value is the value of Ahmet [Turkey,24].
# Step5: Delete Antonio from the dictionary.

dictionary = {"Christian": ["America", 18],
              "Daisy": ["England", 12],
              "Antonio": ["Spain", 22],
              "Dante": ["Italy", 25]}

# Step 1
print("Keys {}".format(dictionary.keys()))

# Step 2
print("Values: {}".format(dictionary.values()))

# Step 3
dictionary.update({"Daisy": ["England", 13]})
print(dictionary)


# Step 4
def add_values_in_dict(sample_dict, key, list_of_values):
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict


dictionary = add_values_in_dict(dictionary, "Ahmet", ["Turkey,24"])
print(dictionary)

# Step 5
dictionary.pop("Antonio")
print(dictionary)

# %% Mission 5
# Enter a function that takes a list as an argument,
# assigning the odd and even numbers within the list
# to separate lists, and returning the find lists.

l = [2, 13, 18, 93, 22]


def funct(lst):
    even_list = []
    odd_list = []
    [even_list.append(value) if value % 2 == 0 else odd_list.append(value) for value in lst]
    return even_list, odd_list


even_list, odd_list = funct(l)
print("Even list : {} - Odd List: {}".format(even_list, odd_list))

# %%
# Mission 6
# Using the List Comprehensive structure, capitalize the names of the numeric variables in the
# car_crashes data and NUM to the beginning.

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

df.columns = ["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]
df.columns

# %%
# Mission 7
# Using the List Comprehensive structure, write "FLAG" at the end of the names of the variables
# that do not contain "no" in the car_crashes data.

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns = [col.upper() if "no" in col else col.upper() + "_FLAG" for col in df.columns]
df.columns

# %%
# Mission 8
# Using the List Comprehension structure,
# select the names of the variables that are different from the variable names given below and
# create a new dataframe.

import seaborn as sns

df = sns.load_dataset("car_crashes")
print("Dataframe columns {}".format(df.columns))

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
print("New dataframe columns {}".format(new_df.columns))
