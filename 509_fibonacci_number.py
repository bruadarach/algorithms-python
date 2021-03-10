'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 
Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Constraints:

0 <= n <= 30
'''

# Pibonacci number starts from 0 and 1, and continues to add the 2 previous pibonacci numbers
# For example, 0,1,1,2,3,5,8,13,21,34,55,89...

# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8

class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        elif n > 2:
            prev = 0
            current = 1
            for i in range(0, n-1):
                answer = prev + current # without this variable 'answer', it will not return a correct answer! # Think about WHY
                prev = current
                current = answer
        return answer

# (runtime / memory)
#  24 ms / 14.4 MB



'''
class Solution:
    def fib(self, n: int) -> int:
        a,b = 0,1
        for _ in range(n):
            a, b = b, a+b
        return a
'''
# (runtime / memory)
#  24 ms / 14.1 MB

''' WRONG: this answer is wrong, thing about WHY?!
class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        for _ in range(n):
            a = b
            b = a+b
        return a
'''
# WRONG ANSWER! 



'''
class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0:
            return 0

        elif n == 1:
            return 1

        elif n >= 2:
            first = 0
            second = 1
            next = first + second

            for i in range(2, n):
                first = second
                second = next
                next = first + second
        return next
'''
# (runtime / memory)
#  28 ms / 14.2 M

