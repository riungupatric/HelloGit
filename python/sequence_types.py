# Mutable and Immutable sequence types

# ! Mutable

numbers = [1, 2, 3, 4, 5]  # lists are mutable
numbers2 = list(range(1, 6))
# numbers[2] = 23
for number in numbers2:
    print(number, end=" ")

print()

# Dictonaries are mutable
languages = {"py": "Python", "rs": "Rust", "js": "JavaScript", "rb": "Ruby"}

for key, value in languages.items():
    print(f"{value} extension is {key}")


# ! Immutable
# Tuple is immutable
digits = (1, 2, 3, 4, 5)

# range is immutable
values = range(10, 101, 10)  # tens

for number in values:
    print(number, end=" ")

print(type(digits))
