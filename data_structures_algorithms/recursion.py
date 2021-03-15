'''
# E.g) Fibonacci Numbers
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

# (runtime / memory)
#  28 ms / 14.2 M



class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

# (runtime / memory)
#  916 ms / 14.3 M