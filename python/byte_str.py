b = b"hi there : "
c = "hi, how are you?"

# ! can't conacatenate a byte and a string
# you need to decode byte to str
b1 = b.decode('utf-8')
# or encode str to byte
c1 = c.encode('utf-8')
print(b1 + c)
print(b + c1)
