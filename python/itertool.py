# working with itertools module

import itertools

# ! permutations :
# all possible outcomes
winners = {1: 'Patrick', 2: 'James', 3: 'Paul'}
# keys
for combo in itertools.permutations(winners):
    print(combo)

# names
for combo in itertools.permutations(winners.values()):
    print(combo)

# ! combination :
# all possible out comes, without repetition
# say we can only have two: president and running mate
candidates = ['Ruto', 'Weta', 'MDVD', 'Kabogo', 'Rigathe']

for two in itertools.combinations(candidates, 2):
    print(two)
