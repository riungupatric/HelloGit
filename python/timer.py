# creating a timer

import time


def count_down(duration):
    try:
        t = int(duration)
    except:
        raise ValueError("Please enter time in seconds")

    while t:
        mins, secs = divmod(t, 60)
        hrs, mins = divmod(mins, 60)
        counter = f"{hrs:02d}:{mins:02d}:{secs:02d}"
        print(counter, end='\r')
        time.sleep(1)
        t -= 1
    print("Time is up!")


# let's run it
duration = input("Enter duration : ")
count_down(duration)
