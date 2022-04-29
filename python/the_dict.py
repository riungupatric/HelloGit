# dictionaries

dict1 = {'name': 'Patrick', 'age': 32,
         'status': 'Married', 'Languages': '4', 'weight': 85.8}

dict2 = dict(name='Jack', age=23, status='married', languages=4, weight=64.5)
# for k in dict1.keys():
# for v in dict1.values():
# for k in dict1:
#print(f'{k} : {dict1[key]}')
for k, v in dict1.items():
    print(f"{k}: {v}")

print("Named" if "name" in dict1 else "absent")  # key exists?

# get the married status

print(dict1.get('status'))

# check key in a  dict
print('weight' in dict1)

# dict1[age] += 1
print(dict1)

dict1.update(age=34)
print(dict1)
