def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):  # 5-1 = 4 | 0,1,2,3

        for j in range(0, n-i-1):  # (0,5-3-1=1) = 0
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [88, 56, 100, 27, 1]
print(bubbleSort(arr))  # [1, 27, 56, 88, 100]

''' 
< Time Complexity = (iteration numbers) * the number of comparisons >
1. Iteration number = first for loop => (n-1)
2. The number of comparisons => (n-1)
THEREFORE, (n-1)*(n-1) = n^2 - 2n + 1 => O(n^2)
'''

'''
(n-1) + (n-2) + .... + 2 + 1 => n(n-1)/2
(5-1) + (5-2) + (5-3) + (5-4) => 5(5-1)/2
4 + 3 + 2 + 1 = 10

i = 0
j = 0,1,2,3

i = 1
j = 0,1,2

i = 2
j = 0,1

i = 3
j = 0
'''


def bubble(list):

    n = len(list)
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, n-1):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
    return list


print(bubble([88, 56, 100, 27, 1]))  
# [1, 27, 56, 88, 100]
