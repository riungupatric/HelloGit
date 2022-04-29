from functools import reduce as r

names = ({'name': 'Patrick', 'age': 32}, {
         'name': 'Joe', 'age': 45}, {'name': 'Paul', 'age': 53})

# initial val of acc is 0
total_ages = r(lambda acc, val: acc + val['age'], names, 0)

print(total_ages)
