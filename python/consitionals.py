# membership operators

names = ["John", "Doe", "Jane"]
people = ("Jack", "Joy", "John")

if "Doe" in names:
    print("we have a Doe")

# make sure jack is not in there
if "Jack" not in names:
    print("Yes, Jack is not in the list")

# Making sure two objects are not the same
if names[0] is not people[2]:
    print("Yes, seems they are different")
else:
    print("Surprise, they are the same!!")


# ! ternary operator
# must have both if and else
danger = "We have a problem people" if True else "No, we are safe for now"
print(danger)
