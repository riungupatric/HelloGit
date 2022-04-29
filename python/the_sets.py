# sets contain uniques items only

names = set(["patrick", "james", "ken", "mathew", "patrick"])
monos = set(['jack', 'stano', 'ken', 'mathew', 'alan'])

# sort the names
namiz = sorted(names)

# check names in set names but not in monos
bazus = (names - monos)

# members in names or monos, or both
raia = (names | monos)

# members in names or monos, but not both
karas = (names ^ monos)

# member in both lists
dups = (names & monos)
for name in dups:
    print(name)
