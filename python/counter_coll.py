# powerful counter dictionary

from collections import Counter

form1 = ['bob', 'alan', 'morris', 'kevin', 'bob', 'alan', 'bob', 'morris']
form2 = ['kevin', 'vinn', 'bob', 'patrick', 'alan', 'morty']

# initialize the Counter

f1 = Counter(form1)
f2 = Counter(form2)

# how many students are named 'alan' in form 1
print(f1['alan'])

# total students in form 2
print(sum(f2.values()))

# 2 most common names in form 1
print(f1.most_common(2))

# combine two counters(form1 + form2)
f1.update(f2)
print(f1.most_common(2))

# unique names in form 2
print(sorted(f2))

# separate the two classes
f1.subtract(f2)

# common names in form1 and form 2
print(f1 & f2)
