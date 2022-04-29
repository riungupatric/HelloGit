# this should output 0, but it doesn't

from decimal import *

ans_a = (0.1 + 0.1 + 0.1) - 0.3  # outputs unsual answer

# ? Better way
# ! best when dealing with money
a = Decimal('0.10')
b = Decimal('0.30')

ans_b = a + a + a - b

print(ans_b)
print(type(ans_b))
