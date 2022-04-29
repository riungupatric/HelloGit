# working with temporary files

import tempfile

temp = tempfile.TemporaryFile()

# temporary files are saved as bytes

temp.write(b"What was going on in 1952 was terrible!")

# set the seek point to 0
temp.seek(0)

# print
print(temp.read())

# close the file
temp.close()
