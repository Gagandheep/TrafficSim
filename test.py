from collections import deque, namedtuple

x = namedtuple('x', 'v')

a = x(1)
b = x(1)

l = deque([0] * 5, 5)
l.append(a)
print(b in l)

# for i in range(10):
#     a.append(i)
#     print(a)
