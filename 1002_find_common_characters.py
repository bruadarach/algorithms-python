'''
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
You may return the answer in any order.
 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
'''

import collections
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        common = collections.Counter(A[0])
        for i in range(1, len(A)):
            common = common & collections.Counter(A[i])

        result = []
        for k, v in common.items():
            result.extend(list(k*v))
        return sorted(result)

# (runtime / memory)
#  44 ms / 14.4 MB



'''
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
    
        common = A[0]
        for i in range(1, len(A)):
            common = list((collections.Counter(common) & collections.Counter(A[i])).elements())
        return common
'''
# (runtime / memory)
#  80 ms / 14.1 MB
