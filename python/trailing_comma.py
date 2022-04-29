x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
names = ["patrick", "james", "ken", "mathew", "patrick"]

# ! dealing with trailin comma for ints
for item in x:
    print(item, end="")
    if(item != x[-1]):
        print(",", end=" ")
print()

# ! dealing with trailing comma for strings
print(", ".join(names))
