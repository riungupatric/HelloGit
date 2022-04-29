# adding commas and decimal places
from decimal import Decimal

big_num = 34 * 347 * 1000

# rounded to 2 decimal places
print(f"Without commas : {big_num:.2f}")
biggie = "{:.2f}".format(big_num)
# print(biggie)
# print the num with commas
print("Real money : ${:,}".format(Decimal(biggie)))
