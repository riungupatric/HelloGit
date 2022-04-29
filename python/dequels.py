# double ended list

from collections import deque

# deafault list
normal_list = ['center']
normal_list.append('right')  # append right
normal_list.append('right')
# can't append left, or at the beginning of list
# although you use insert for that
normal_list.insert(0, 'left')
normal_list.insert(0, 'left')
normal_list.pop()  # return last item

# can't popleft, BUT
first = normal_list[0]
normal_list.remove(first)
# rotate list by 2 spaces,
# no rotate() function, BUT..
last = normal_list.pop()
normal_list.insert(0, last)
last = normal_list.pop()
normal_list.insert(0, last)

# deque list
double_list = deque(['center'])
double_list.append('right')
double_list.append('right')
double_list.appendleft('left')
double_list.appendleft('left')
double_list.pop()  # last item
double_list.popleft()  # firstitem
# rotate by 2, EASY!
double_list.rotate(2)


print(normal_list)
print(double_list)
