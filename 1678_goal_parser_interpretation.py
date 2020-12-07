
'''
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.
Given the string command, return the Goal Parser's interpretation of command.

 
Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".

Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"

Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"
 

Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.
'''


class Solution:
    def interpret(self, command: str) -> str:

        count = 0
        result = ""
        for i in command:
            if i == "(":
                count += 1
            elif i == ")":
                count -= 1
                if count == 0:
                    result += "o"
                    count = 0
                elif count > 0:
                    count = 0
            else:
                if count > 0:
                    count += 1
                    result += i
                else:
                    result += i
        return result

# (runtime / memory)
#  44 ms / 14.1 MB


'''
class Solution:
    def interpret(self, command: str) -> str:
        
        count = 0
        result = ""
        for i in command:
            if  i == "(":
                result+=i
                count += 1
            elif i == ")":
                result+=i
                count -= 1
                if count == 0:
                    result = result.replace("(","")
                    result = result.replace(")","")
                    result += "o"
                    count = 0
                elif count > 0:
                    result = result.replace("(","")
                    result = result.replace(")","")
                    count = 0 
            else:   
                if count > 0 :
                    count += 1
                    result += i
                else:
                    result += i

        return result
'''
# (runtime / memory)
#  24 ms / 14.3 MB


'''
class Solution:
    def interpret(self, command: str) -> str:
        
        return command.replace('()','o').replace('(al)','al')
'''
# (runtime / memory)
#  32 ms / 14.3 MB
