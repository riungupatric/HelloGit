# a more capable dictionary
from collections import defaultdict

fruits = ['apple', 'mango', 'banana', 'avocado',
          'avocado', 'apple', 'apple', 'mango']

# create a dictionary with fruit as key and
# amount of each type as value


# !old method
fruits_dict = {}

for fruit in fruits:
    if fruit in fruits_dict.keys():
        fruits_dict[fruit] += 1
    else:
        fruits_dict[fruit] = 1

# print(fruits_dict)

# todo: Using the collections module
# if there is no key in the dictionary,
# as is the case in the first iteration,
# defaultdict(int) makes sure that value defaults to 0,
# or just use lambda:0
fruits_counter = defaultdict(lambda: 0)

for fruit in fruits:
    fruits_counter[fruit] += 1

print(fruits_counter)
