'''
Given a string s. You should re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.


Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

Example 2:

Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.

Example 3:

Input: s = "leetcode"
Output: "cdelotee"

Example 4:

Input: s = "ggggggg"
Output: "ggggggg"

Example 5:

Input: s = "spo"
Output: "ops"
 

Constraints:

1 <= s.length <= 500
s contains only lower-case English letters.
'''


class Solution:
    def sortString(self, s: str) -> str:

        unique = sorted(set(s))  # ['a', 'b', 'c']

        dic = {}
        for i in unique:
            dic[i] = s.count(i)  # {'a': 4, 'b': 4, 'c': 4}

        result = ''
        flag = True
        while flag:
            flag = False
            for i in sorted(dic.keys()):
                if dic[i] != 0:
                    result += i
                    dic[i] -= 1
                    flag = True
            for j in sorted(dic.keys(), reverse=True):
                if dic[j] != 0:
                    result += j
                    dic[j] -= 1
                    flag = True
        return result

# (runtime / memory)
#  60 ms / 14.3 MB

'''
collections.Counter()
    : '동일한 값의 자료가 몇개인지를 파악하는데 사용하는 객체
    : 결과값(return)은 딕셔너리 형태로 출력
'''

'''
class Solution:
    def sortString(self, s: str) -> str:
        
        dic = collections.Counter(s)

        result = ''
        flag = True
        while flag:
            flag = False
            for i in sorted(dic.keys()):
                if dic[i] != 0:
                    result += i
                    dic[i] -= 1
                    flag = True
            for j in sorted(dic.keys(), reverse=True):
                if dic[j] != 0:
                    result += j
                    dic[j] -= 1
                    flag = True
        return result
'''
# (runtime / memory)
#  68 ms / 14.2 MB
