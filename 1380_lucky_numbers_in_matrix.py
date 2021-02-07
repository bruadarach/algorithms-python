'''
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column

Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5.
All elements in the matrix are distinct.
'''


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        result = [min(i) for i in matrix]

        temp, answer = [], []
        for i in range(len(matrix[0])):  # 0,1,2,3
            for j in range(len(matrix)):  # 0,1,2
                temp.append(matrix[j][i])
            if max(temp) in result:
                answer.append(max(temp))
            temp = []
        return answer

# (runtime / memory)
#  128 ms / 14.6 MB



'''
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        minrow = {min(r) for r in matrix} # {9, 3, 15}
        maxcol = {max(c) for c in zip(*matrix)} # zip(*) # {16, 17, 15}
        return list(minrow & maxcol)
'''
# (runtime / memory)
#  120 ms / 14.5 MB
