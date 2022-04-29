# Other ways to format string
from string import Template
# common method
str1 = "Learning {} by {}.".format('Advanced Python', 'Joe Marini')
print(str1)

# using string template
# strictly for value substitution, no formating
# especially useful with external data that might not be secure
# since format is powerful and can be manipulated.

templ = Template("Learning ${title} by ${author}.")
str2 = templ.substitute(title='Advanced Python', author='Joe Marini')
print(str2)

# OR dictionary data source
data = {'title': 'Advance Python', 'author': 'Joe Marini',
        'subtitle': 'Take your Python skills to the next level'}
str3 = templ.substitute(data)

print(str3)
