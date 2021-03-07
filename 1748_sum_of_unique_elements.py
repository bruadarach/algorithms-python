'''
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
Return the sum of all the unique elements of nums.

 
Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Example 2:

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.

Example 3:

Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
'''



from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        return sum(k for k, v in collections.Counter(nums).items() if v == 1)

# (runtime / memory)
#  32 ms / 14.3 MB

# (Complexity)
# (Time O(n) / Space O(n))



'''
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        return sum([ i for i,v in  __import__("collections").Counter(nums).items() if v == 1 ])
'''


