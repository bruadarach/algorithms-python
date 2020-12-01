'''
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"

Example 2:

Input: "here"
Output: "here"

Example 3:

Input: "LOVELY"
Output: "lovely"
'''


class Solution:
    def toLowerCase(self, str: str) -> str:

        return str.lower()

# (runtime / memory)
#  28 ms / 14.1 MB


'''
class Solution:
    def toLowerCase(self, str: str) -> str:
    
    # The ASCII codes for A-Z is 65-90 and those for a-z is that range plus 32.
    # ord(c)는 문자의 아스키 코드 값을 돌려주는 함수이다.
    # ※ ord 함수는 chr 함수와 반대이다.

        result = ""
        for char in str:
            if 65 <= ord(char) <= 90:
                result += chr(ord(char)+32)
            else:
                result += char
        
        return result
'''
# (runtime / memory)
#  28 ms / 14.2 MB


'''
class Solution:
    def toLowerCase(self, str: str) -> str:

        alphabet = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e',
             'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j',
             'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o',
             'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't',
             'U': 'u', 'V': 'v', 'X': 'x', 'W': 'w', 'Y': 'y',
             'Z': 'z'}
        for char in str:
            if char in alphabet:
                str = str.replace(char, alphabet[char])
        return str
'''
# (runtime / memory)
#  32 ms / 14.2 MB




