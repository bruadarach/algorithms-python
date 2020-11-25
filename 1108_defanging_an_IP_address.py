'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
 
Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 
Constraints:
	•	The given address is a valid IPv4 address.
'''


class Solution:
    def defangIPaddr(self, address: str) -> str:

        return address.replace('.', '[.]')

# (runtime / memory)
#  32 ms / 14.3 MB


'''
class Solution:
    def defangIPaddr(self, address: str) -> str:

        result = ''
        for i in address:
            if i == '.':
                result += '[.]'
            else:
                result += i
        return result
'''
# (runtime / memory)
#  20 ms / 14.1 MB
