# Working with the random module
import random

# float: between 0 and 1
small = random.random()

# Random 0 or 1

bit1 = random.randint(0, 1)
# or
bit2 = random.randrange(2)

# randrange between 1, 49
under50 = random.randrange(1, 50)

# !loterry
# pick five random winners out of 100 contestants
winners = random.sample(range(1, 101), 5)
# print(winners)

# !choice
# pick just one out of many
langs = ['Solidity', 'Javascript', 'Python', 'CSS', 'Rust', 'Ruby']
#print(f"We have picked '{random.choice(langs)}' for you")

# !shuffle
cards = ['Hearts', 'Spades', 'Flowers', 'Diamond']
random.shuffle(cards)
print(cards)
