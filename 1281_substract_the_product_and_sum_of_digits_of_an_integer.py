'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
 

Constraints:

1 <= n <= 10^5
'''


class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        sum = 0
        multi = 1
        for i in list(str(n)):
            multi *= int(i)
            sum += int(i)
        return multi-sum

# (runtime / memory)
#  28 ms / 14.1 MB


class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        return eval('*'.join(str(n))) - eval('+'.join(str(n)))

# (runtime / memory)
#  20 ms / 14.3 MB

