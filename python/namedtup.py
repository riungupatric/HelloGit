# named tuples for better readability

import collections

point = collections.namedtuple('Coordinate', ['x', 'y', 'z'])

# xyz coordinates
p1 = point(0, 0, 0)
p2 = point(10, 0, 23)
p3 = point(10, 5, 15)

print(p1)
print(p2.z)

# change p2.y with 12
p2 = p2._replace(y=12)

print(p2)
