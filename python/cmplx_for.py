# for with additional conditions
working_days = ("mon", "tue", "wed", "thur", "fri", "sat", "sun")
for day in working_days:
    if day == "sun":
        continue  # I don't want to see sun
    # if day == "sat":
    #     break #break out of the loop and skip else
    print(day)
else:
    # called if the loop exited normally
    # You can put success message here
    print("Everything went well!")
