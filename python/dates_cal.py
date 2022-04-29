# working with dates and calendar
import calendar
from datetime import datetime, timedelta


# 7 days from now
deadline = datetime.now() + timedelta(days=7)

# 3 weeks from today
future = datetime.now() + timedelta(weeks=3)
# 2 days ago
order_date = datetime.now() - timedelta(days=3)
print(deadline)
print(order_date)

# comparing dates
if deadline > datetime.now():
    print(f"There is still time remaining : {deadline - datetime.now()}")

# calendar
this_month = calendar.month(2022, 3)

print(this_month)

# Is this year a leap year
if calendar.isleap(datetime.now().year):
    print(f"{datetime.now().year} is a leap year")
else:
    print(f"{datetime.now().year} is not a leap year")
