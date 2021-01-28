''' implementing Priority Queue in Python'''

### 1. using 'List' ###
import heapq
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



### 2. using 'headpq' ###

q = []

heapq.heappush(q, (2, "Minji"))
heapq.heappush(q, (3, "Jake"))
heapq.heappush(q, (1, "Suji"))
heapq.heappush(q, (4, "Lucky"))
print(q)  # [(1, 'Suji'), (3, 'Jake'), (2, 'Minji'), (4, 'Lucky')]

while q:
    print(q[0]) 
    print(heapq.heappop(q))
'''
while q:
    next_item = heapq.heappop(q)
    print(next_item)
'''
# (1, 'Suji')
# (2, 'Minji')
# (3, 'Jake')
# (4, 'Lucky')
