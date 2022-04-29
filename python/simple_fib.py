# a very very simple fibonacci
# upto 500

a, b = 0, 1
values = []
while b < 1000:
    values.append(b)
    a, b = b, a + b

for value in values:
    print(value, end=' ', flush=True)
print()  # line ending
