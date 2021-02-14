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



##### 1) Easy to understand, using .find() #####
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        result = []
        for i in words:
            for j in words:
                if i != j and j.find(i) >= 0:
                    result.append(i)
                    break
        return result

# (runtime / memory)
#  36 ms / 14.1 MB



'''
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        return set([i for i in words for j in words if i != j and j.find(i) >= 0])                             
'''
# (runtime / memory)
#  36 ms / 14.1 MB



##### 2. sort first and using .find() #####
'''
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        words = sorted(words, key=len)
        return set([words[i] for i in range(len(words)) for j in range(i+1,len(words)) if words[j].find(words[i]) >= 0])   
'''
# (runtime / memory)
#  36 ms / 14.1 MB



'''
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        words = sorted(words, key=len)
    
        result = []
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[j].find(words[i]) >= 0:
                    result.append(words[i])
                    break
        return result  
'''
# (runtime / memory)
#  32 ms / 14.2 MB



##### 3. other answers ##### 
'''
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
       
        temp = ' '.join(words) # mass as hero superhero
        subStr = [i for i in words if temp.count(i) >= 2]

        return subStr
'''
# (runtime / memory)
#  20 ms / 14.2 MB



'''
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
       
        words = sorted(words, key=len)
        result = []
        
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    result.append(words[i])
                    break       
        return result
'''
# (runtime / memory)
#  28 ms / 14.3 MB
