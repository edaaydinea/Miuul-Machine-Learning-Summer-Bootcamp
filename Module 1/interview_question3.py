"""
Purpose: Square the even numbers and add them to a dictionary.
Items of keys should be the same, items of values should be changed.
"""
import random

numbers = random.sample(range(0, 10), 10)
print(numbers)

# {number  : number  ** 2 for number in list if number % 2 == 0}
# number = key
# number ** 2 = value

new_dict = {number: number ** 2 for number in numbers if number % 2 == 0}
print(new_dict)
