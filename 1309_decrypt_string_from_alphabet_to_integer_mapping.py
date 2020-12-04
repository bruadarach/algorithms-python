'''
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.


Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:

Input: s = "1326#"
Output: "acz"

Example 3:

Input: s = "25#"
Output: "y"
Example 4:

Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"
 

Constraints:

1 <= s.length <= 1000
s[i] only contains digits letters ('0'-'9') and '#' letter.
s will be valid string such that mapping is always possible.
'''


class Solution:
    def freqAlphabets(self, s: str) -> str:

        dic = {}
        alphabet = list(string.ascii_lowercase)
        for i, j in zip(range(1, 27), alphabet):
            if i > 9:
                i = str(i)+"#"
                dic[i] = j
            else:
                i = str(i)
                dic[i] = j

        temp = []
        count = 0
        for i in range(len(s)):
            if s[i] != "#":
                count += 1
                temp.append((s[i]))
            elif s[i] == "#":
                # temp.pop()
                # temp.pop()
                del temp[-2:]
                temp.append(s[i-2:i+1])

        result = ""
        for j in temp:
            result += dic[j]
        return result

# (runtime / memory)
#  28 ms / 14.2 MB
