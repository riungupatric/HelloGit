# working with datetime

from datetime import datetime

now = datetime.now()

print(now.time())
print(now.date())
print(now.year)
print(now.weekday())

# date formating
print(now.strftime('%a %D'))
print(now.strftime('%a, %dth %b'))
print(now.strftime('%A, %dth %B'))

# formating time
print(now.strftime('%H:%M:%S %p'))

# Year
print(now.strftime('%Y'))
