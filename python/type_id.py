#type and id

names = ["Patrick", "Python", "Java", "Javascript"]
slang = ["Patrick", "Python", "Java", "Javascript"]  # a copy
popular = ("Mozilla", "Chrome", "Brave")
browsers = ("Opera Mini", "Chrome", "Brave")

# checking if the objects are the same
if names is slang:
    print("They are the same")
    print(f"names id : {id(names)} and slang id : {id(slang)}")
else:
    print("They are different")
    print(f"names id : {id(names)} and slang id : {id(slang)}")

# checking if the items are the same object
if popular[1] is browsers[1]:
    print("Tuple items are the same")
    print(
        f"Populars Python id: {id(popular[1])}, Browsers Python id: {id(browsers[1])}")
else:
    print("Nope, they are very different")

# checking type
if isinstance(names, tuple):
    print("Names is a tuple")
elif isinstance(names, list):
    print("names is a list")
else:
    print("No clue")
