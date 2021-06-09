"""
832. Flipping an Image
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.  
For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1
"""


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for i in range(len(image)):
            image[i].reverse()
            for j in range(len(image[i])):
                #print(image[i][j])
                if image[i][j] == 0:
                    image[i][j] = 1
                elif image[i][j] == 1:
                    image[i][j] = 0
        return image
        
# (runtime / memory)
#  44 ms / 14.3 MB



""" SOLUTION 1

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        for i in A:
            i.reverse()
            
        result=[]
        new=[]
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    result.append(0)
                    j=j+1
                elif A[i][j] == 0:
                    result.append(1)
                    j=j+1
            new.append(result)
            result=[]
            i=i+1
        return new
"""



""" SOLUTION 2

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        a = []
        for i in A:
            for j in range(len(i)):
                if i[j] == 1:
                    i[j] = 0

                elif i[j] == 0:
                    i[j] = 1

            a.append(i[::-1])

        return a

""" 



""" SOLUTION 3

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        for i in range(len(A)):
            A[i] = A[i][::-1]
            for j in range(len(A[i])):
                A[i][j] = 1 - A[i][j]
        return A
"""
        

