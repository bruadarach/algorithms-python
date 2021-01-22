
'''<1. collections - deque>'''

# 1. Python code to demonstrate deque
import requests
from multiprocessing import Queue
from collections import deque

queue = deque(['name', 'age', 'address']) # declare deque

print(queue)  # deque(['name', 'age', 'address'])



# 2. append(), appendleft(), pop(), popleft()
import collections

de = collections.deque([1,2,3])
de.append(4) 
print(de)  # deque([1, 2, 3, 4])

de.appendleft(0) 
print(de)  # deque([0, 1, 2, 3, 4])

de.pop() 
print(de)  # deque([0, 1, 2, 3])

de.popleft() 
print(de)  # deque([1, 2, 3])



# 3. index(ele,beg,end), insert(idx, value), remove(), count()
import collections

de = collections.deque([1,2,3,3,4,2,4])
print(de.index(4,2,5)) # 4 

de.insert(4, 7) # (idx, value) 
print(de)  # deque([1, 2, 3, 3, 7, 4, 2, 4])

de.remove(3) 
print(de)  # deque([1, 2, 3, 7, 4, 2, 4])

print(de.count(4)) # 2



# 4. extend(iterable), extendleft(iterable), reverse(), rotate()
import collections

de = collections.deque([1,2,3])

de.extend([4,5,6])
print(de)  # deque([1, 2, 3, 4, 5, 6])

de.extendleft([7,8,9])
print(de)  # order is reversed!
# deque([9, 8, 7, 1, 2, 3, 4, 5, 6])

de.rotate(-3)  
print(de)  # deque([1, 2, 3, 4, 5, 6, 9, 8, 7])

de.reverse()
print(de)  # deque([7, 8, 9, 6, 5, 4, 3, 2, 1])
print(list(de))  # [7, 8, 9, 6, 5, 4, 3, 2, 1]



# 5. len(), clear()
print(len(de)) # 9

de.clear()
print(de)  # deque([])
