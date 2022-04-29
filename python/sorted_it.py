zen = ("In the face of ambiguity, refuse the temptation to guess. "
       "13?. There should be one -- and preferably only one -- obvious way to do it")

users = {'patrick': 67, 'jon': 46, 'alex': 98, 'boby': 23}

workers = [('patrick', 67, 2), ('jon', 46, 3),
           ('alex', 98, 1), ('boby', 23, 4)]

# key=str.lower --> convert each word to lower and then sort
# reverse=True --> sort in descending order
zen_sort = sorted(zen.split(), key=str.lower)

# sorting a dict, default sorts by keys
key_sort = sorted(users)

# sorting by values, high to low
rank = sorted(users.values(), reverse=True)

# sort users using values in the dictionary
user_pnts = sorted(users, key=lambda point: users[point], reverse=True)

# sort workers using points, high to low
worker_pnts = sorted(workers, key=lambda pnt: pnt[1], reverse=True)

print(user_pnts)
print(worker_pnts)
