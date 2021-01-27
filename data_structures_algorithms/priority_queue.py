''' implementing Priority Queue in Python'''

### 1. using 'List' ###
from queue import PriorityQueue

q = []

q.append((2, "Minji"))
q.append((3, "Jake"))

q.sort(reverse=True)

q.append((1,"Suji"))
q.sort(reverse=True)

q.append((4, "Lucky"))
q.sort(reverse=True)

while q:
    print(q.pop(0))
'''
while q:
    next_item = q.pop()
    print(next_item)
'''
# (4, 'Lucky')
# (3, 'Jake')
# (2, 'Minji')
# (1, 'Suji')