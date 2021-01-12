'''
There is a hidden integer array arr that consists of n non-negative integers.

It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].

You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].

Return the original array arr. It can be proved that the answer exists and is unique.

 

Example 1:

Input: encoded = [1,2,3], first = 1
Output: [1,0,2,1]
Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]

Example 2:

Input: encoded = [6,2,7,3], first = 4
Output: [4,2,0,7,4]
 

Constraints:

2 <= n <= 104
encoded.length == n - 1
0 <= encoded[i] <= 105
0 <= first <= 105

'''


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:

        result = [first]
        for i in range(len(encoded)):
            result.append(encoded[i] ^ result[i])
        return result

# (runtime / memory)
#  60 ms / 14.6 MB

'''
Explanation:
We know that if a XOR b = c,
then a XOR c = b

Truth Table for XOR is:
Here C = A XOR B
A | B | C
0 | 0 | 0 -> C XOR A is 0 XOR 0 = 0 = B
0 | 1 | 1 -> C XOR A is 0 XOR 1 = 1 = B
1 | 0 | 1 -> C XOR A is 1 XOR 0 = 1 = B
1 | 1 | 0 -> C XOR A is 1 XOR 1 = 0 = B

Steps:

We append the first element into the answer list
We iterate through the encoded list and append XOR of answer list's element with encoded list's element
return the answer list
'''
