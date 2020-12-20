'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

 
Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
'''


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        if len(A) < 1 or len(A) > 5000:
            return []

        even = []
        odd = []
        for num in A:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        even.extend(odd)
        return even
        #return even + odd

# (runtime / memory)
#  68 ms / 15 MB



'''
The resultant array will have all the even numbers followed by the odd numbers. To do that follow two steps:

keep track of indexes from the beginning. Do that using p, so p is the index where the next even number will be placed.
Whenever you encounter an even number, say at index i, swap it with the number at p
Let's visualize that with an example,
1, 3, 5, 2, 4, 6
p = 0, so the first even number will be placed at 0
when i = 3, A[i] is even, swap it with A[p], increment p.
the array is: 2, 3, 5, 1, 4, 6

Now p is 1, so the next even number will be placed at 1,
when i=4, A[i] is even, swap it with A[p], increment p.
the array is: 2, 4, 5, 1, 3, 6

Now p is 2, so the next even number will be placed at 1,
when i=5, A[i] is even, swap it with A[p], increment p.
the array is: 2, 4, 6, 1, 3, 5

Then the loop terminates. So you got your result, also the relative order is unchanged.
'''

'''
p = 0
for i in range(len(A)):
    if A[i] % 2 == 0:
        A[i], A[p] = A[p], A[i]
        p += 1
return A

# (runtime / memory)
#  72 ms / 15 MB



'''
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [i for i in A if i % 2 == 0] + [i for i in A if i % 2 != 0]
'''
# (runtime / memory)
#  76 ms / 14.9 MB



'''
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:    
        return sorted(A, key=lambda x: x%2)
'''
# (runtime / memory)
#  76 ms / 15 MB     

