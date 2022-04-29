# working with zip files
import zipfile

# open the zip file

zipf = zipfile.ZipFile('pythonify.zip', 'r')

# files in the zip folder
f = zipf.namelist()
# print(f)

# print metadata of the files
for meta in zipf.infolist():
    print(meta)
# or
web = zipf.getinfo('web.txt')
# print(web)

with zipf.open('abase.txt') as fl:
    # print(fl.read())
    for line in fl:
        print(line)

# extract files from the zip
zipf.extractall()
