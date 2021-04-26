'''
Given an integer n. Each number from 1 to n is grouped according to the sum of its digits. 

Return how many groups have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
Example 3:

Input: n = 15
Output: 6
Example 4:

Input: n = 24
Output: 5
 

Constraints:

1 <= n <= 10^4
'''


##### Using defaultdict #####
class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        if n < 10:
            return n
       
        l = collections.defaultdict(int)
        for i in range(1,n+1):
            sum = 0
            for j in str(i):
                sum += int(j)
            l[sum] += 1
            sum = 0

        largest_size = max(l.values())
        count = 0
        for n, c in l.items():
            if c == largest_size:
                count += 1
        return count

# (runtime / memory)
#  104 ms / 14.2 MB



##### Using dictionary #####
'''
class Solution:
    def countLargestGroup(self, n: int) -> int:

        if n < 10:
            return n
       
        d = {}
        
        for i in range(1, n+1):
            num_sum = sum(map(int, list(str(i))))
            
            if num_sum not in d:
                d[num_sum] = 1
            else:
                d[num_sum] += 1
        
        largest_size = max(d.values())
        return sum(1 for i in d.values() if i == largest_size)
'''
# (runtime / memory)
#  116 ms / 14.3 MB
