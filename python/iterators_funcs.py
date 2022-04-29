# other built-in funcions for iteration

days = ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']
days_fr = ['lundi', 'mardi', 'mercredi',
           'jeudi', 'vendredi', 'samedi', 'dimanche']
days_order = (1, 2, 3, 4, 5, 6, 7)
# iter
# iterate through days one by one
day = iter(days)
print(next(day))  # mon
print(next(day))  # tue

# iterate through file lines
# pass a sentinel, in this case '', to make end of the file
with open('truth_meter.txt', 'r') as fp:
    for line in iter(fp.readline, ''):
        print(line.strip())

# the enumerate function
for index, day in enumerate(days, start=1):
    print(f"{index} : {day}")

# the zip function
for day in zip(days_order, days):
    # print(day)#(1, 'mon')
    print(f"{day[0]} : {day[1]}")

#enumerate and zip
for indx, day in enumerate(zip(days, days_fr), start=1):
    print(f"{indx}: {day[0]} is {day[1]} in French")
