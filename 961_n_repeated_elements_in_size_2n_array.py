'''
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
Return the element repeated N times.
 

Example 1:

Input: [1,2,3,3]
Output: 3

Example 2:

Input: [2,1,2,5,3,2]
Output: 2

Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5
 

Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
'''


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        dict = {}
        for i in A:
            if i not in dict:
                dict[i] = 1
            else:
                return i

# (runtime / memory)
#  188 ms / 15.6 M



'''
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        dict = {}
        for i in A:
            if i in dict.keys():
                return i
            else:
                dict[i] = 1
'''
# (runtime / memory)
#  191 ms / 15.5 M



'''
import statistics 

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        return mode(A)
'''
# (runtime / memory)
#  204 ms / 15.6 M



'''
from collections import Counter

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:

        c = collections.Counter(A)
        for value, count in c.items():
            if count > 1:
                return value
'''
# (runtime / memory)
#  200 ms / 15.6 MB



'''
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        c = collections.Counter(A)
        return c.most_common()[0][0]
'''
# (runtime / memory)
#  212 ms / 16 MB
