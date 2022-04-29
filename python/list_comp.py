# list comprehension
# A list created based on another list on iterator
from math import *
money = []
for mon in range(50, 500, 50):
    money.append(mon)

# list comp: double my money
money2 = [x * 2 for x in money]

# 5x only the hundreds
hundreds = [x * 5 for x in money if x % 100 == 0]

# a tuple of my money squared
xmoney = [(x, x**2) for x in money]

# find sqrt and round my money to 2 decimal places
real = [round(sqrt(x), 2) for x in money]

# a dictionary of multiplication
multi = {x: x**2 for x in money}

print(multi)
