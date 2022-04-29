# list and tuples
# same except list is mutable and tuples are not
# tuples don't have methods that alter a collection like append
#!Lists
from ntpath import join


birds = ['eagle', 'kiwi', 'chicken', 'owl', 'dove', 'hawk', 'kusama']

# add bird at the beginning of list
birds.insert(0, 'duck')

# append a bird at end of list
birds.append('peakock')

# pop
birds.pop()  # remove and return the last item
birds.pop(3)  # remove and return item at index 3

# del
del birds[0:3:2]  # delete first and third item

# returns index of dove
dove = birds.index('dove')

print(birds[0:3:2])  # return first an d 3rd bird
print(birds[3:])  # return everything from 4th item, inclusive

# Join
print(','.join(birds))
