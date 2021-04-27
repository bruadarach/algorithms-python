'''
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

 
Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.


Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Constraints:

The given integer num is guaranteed to fit within the range of a 32-bit signed integer.
num >= 1
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
'''


class Solution:
    def findComplement(self, num: int) -> int:

        bit_mask = (2**num.bit_length()) - 1
        return (num ^ bit_mask)

# (runtime / memory)
#  20 ms / 14.3 MB


'''
Example_#1

input: 5

5 = 0b 101
bits length of 5 = 3
masking = 2^3 -1 = 8 - 1 = 7 = 0b 111

5 = 0b 101
3 = 0b 111 ( XOR )
—————————
2 = 0b 010

output: 2
'''

'''
Example_#2

input: 9

9 = 0b 1001
bits length of 2 = 4
masking = 2^4 -1 = 16 - 1 = 15 = 0b 1111

09 = 0b 1001
15 = 0b 1111 ( XOR )
—————————
06 = 0b 0110

output: 6
'''
