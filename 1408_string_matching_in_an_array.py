'''
Given an array of string words. Return all strings in words which is substring of another word in any order. 
String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].
 

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Example 3:

Input: words = ["blue","green","bu"]
Output: []
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
It's guaranteed that words[i] will be unique.
'''


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        result = []
        for i in words:
            for j in words:
                if i != j:
                    if j.find(i) >= 0:
                        result.append(i)
        return set(result)

# (runtime / memory)
#  44 ms / 14.2 MB


'''
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
       
        return set([i for i in words for j in words if i != j and j.find(i) >= 0])                     
'''
# (runtime / memory)
#  40 ms / 14.1 MB



'''
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
       
        temp = ' '.join(words) # mass as hero superhero
        subStr = [i for i in words if temp.count(i) >= 2]

        return subStr
'''
# (runtime / memory)
#  20 ms / 14.2 MB