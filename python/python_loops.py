# python loops have an else:

counter = 0
password = "manna"
access = False
max_attempts = 5
guess = ""

# while with additional conditions
while guess != password:
    counter += 1
    if counter == 3:
        continue  # skips 3
    if counter == 5:
        break  # exits the loop prematually, else is not executed
    guess = input(f"{counter}. Enter you guess here : ")
else:
    access = True

print("Access granted" if access else "Access blocked")
