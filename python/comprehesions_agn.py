# More comprehensions

# make a list of even and odds below 20:
odds = []
evens = []
for x in range(1, 21):
    if x % 2 == 0:
        evens.append(x)
    else:
        odds.append(x)
# Todo Perform mapping and filering on a list.
# square evens between 4 and 16

evenSquared = list(
    map(lambda x: x**2, filter(lambda x: x > 4 and x < 16, evens)))
# Todo, square evens btn 4 and 16 using list comprehension
# !List comprehension
evenBetter = [x**2 for x in evens if x > 4 and x < 16]

# print(odds)
# print(evens)
# print(evenSquared)
# print(evenBetter)

# !Dictionary comprehension
# make a temperatures dictionary,
# where key is celcius and value is kelvin
#conversion (t*9/5)+32.0
# condition: for temps below 100 degrees

celcius = [-2, 23, 44, 8, 50, 100, 120, 23, 44, 34, 30, 2]

temp_dict = {t: (t*9/5)+32.0 for t in celcius if t < 100}

# print(temp_dict)
# todo, combine two teams into 1.
team1 = {'Joe': 9, 'Snow': 11, 'Becker': 1, 'Ronaldo': 7, 'Alexis': 9}
team2 = {'Mane': 9, 'Alnod': 23, 'Salah': 8, 'Drogba': 17}

team = {k: v for team in (team1, team2) for k, v in team.items()}

# print(team)

# TODO, make a set of only unique kevin temps, for celcius
#!set comprehesions

uniq_ktemps = {(t*9/5)+32.0 for t in celcius}

print(uniq_ktemps)
