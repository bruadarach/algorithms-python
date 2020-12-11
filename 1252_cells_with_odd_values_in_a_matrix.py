'''
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.
Return the number of cells with odd values in the matrix after applying the increment to all indices.

 
Example 1:


Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.

Example 2:


Input: n = 2, m = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.
 

Constraints:

1 <= n <= 50
1 <= m <= 50
1 <= indices.length <= 100
0 <= indices[i][0] < n
0 <= indices[i][1] < m
'''


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:

        matrix = [[0 for i in range(m)] for j in range(n)]

        for pair in indices:
            r = pair[0]  # 0 # 1
            c = pair[1]  # 1 # 1

            matrix[r] = [x+1 for x in matrix[r]]
            for i in range(len(matrix)):
                matrix[i][c] += 1

        count = 0
        for list in matrix:
            for num in list:
                if num % 2 != 0:
                    count += 1
        return count
# (runtime / memory)
#  52 ms / 14.4 MB


'''
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:

        row = [0] * n
        col = [0] * m
        
        for i i
        n indices:
            r = i[0]
            c = i[1]
            row[r] += 1
            col[c] += 1
        
        count = 0
        for x in row:
            for y in col:
                if (x + y) % 2 == 1:
                    count += 1
        return count
'''
# (runtime / memory)
#  36 ms / 14.2 MB


''' ##### FAILED CODE #####
n = 28
m = 38
indices = [[17,16],[26,31],[19,12],[22,24],[17,28],[23,21],[27,32],[23,27],[23,33],[18,7],[4,20],[0,31],[25,33],[5,22]]

my answer : 406
right answer : 460

* Check the issue on list copy -> shallow copy and deep copy (including list comprehension)
############################
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:

        temp = [[0]*m]*n
        matrix = temp.copy()

        for pair in indices:
            r = pair[0] # 0 # 1
            c = pair[1] # 1 # 1 

            matrix[r] = [x+1 for x in matrix[r]]
            for i in range(len(matrix)):
                matrix[i][c] += 1

        count = 0
        for list in matrix:
            for num in list:
                if num % 2 != 0:
                    count += 1
        return count
'''
