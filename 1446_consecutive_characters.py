'''
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.
Return the power of the string.

 
Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.


Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.


Example 3:

Input: s = "triplepillooooow"
Output: 5


Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11


Example 5:

Input: s = "tourist"
Output: 1
 

Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.
'''


class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        max_count = 0
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 1
        return max(count, max_count)

# (runtime / memory)
#  32 ms / 14.9 MB



'''
class Solution:
    def maxPower(self, s: str) -> int:

        count = 1
        max_count = 0

        if len(s) == 1:
            return 1
        elif len(s) == 2 and s[0] == s[1]:
            return 2

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1

            else:
                if count > max_count:
                    max_count = count
                count = 1
        return max(count, max_count)
'''
# (runtime / memory)
#  28 ms / 14 MB



'''
class Solution:
    def maxPower(self, s: str) -> int:
        
        count = max_count = 1
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
                max_count = max(count, max_count)
            else:
                count = 1
        return max_count
'''
# (runtime / memory)
#  36 ms / 14.3 MB



'''
class Solution:
    def maxPower(self, s: str) -> int:
        
        return max(len(list(b)) for a, b in itertools.groupby(s))
'''
# (runtime / memory)
#  36 ms / 14.2 MB
