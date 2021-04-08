'''
Given an integer array arr. You have to sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.
Return the sorted array.
 

Example 1:

Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]


Example 2:

Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
Output: [1,2,4,8,16,32,64,128,256,512,1024]
Explantion: All integers have 1 bit in the binary representation, you should just sort them in ascending order.


Example 3:

Input: arr = [10000,10000]
Output: [10000,10000]


Example 4:

Input: arr = [2,3,5,7,11,13,17,19]
Output: [2,3,5,17,7,11,13,19]


Example 5:

Input: arr = [10,100,1000,10000]
Output: [10,100,10000,1000]
 

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 10^4
'''


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        d = {}
        ovelap_keys = []

        for i in arr:
            bin_num = sum(list(map(int, bin(i)[2:])))
            if bin_num in d.keys():
                d[bin_num].append(i)
            else:
                d[bin_num] = [i]

        d = dict(sorted(d.items(), key=lambda item: item[0]))

        final = []
        for i in d.values():
            final.extend(sorted(i))

        if ovelap_keys:
            for i in final:
                final.insert(final.index(i), i)

        return final

# (runtime / memory)
#  84 ms / 14.5 MB



'''
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        return sorted(arr, key=lambda arr: [bin(arr).count('1'), arr])
'''
'''
# Why keep an x in the end?
# => If there is a tie in "1" count, you would need to sort their original order.
# => In case of two or more integers have the same number of 1's you have to sort them in ascending order.

Since Python's sort Timsort will perform stable order, means if [4,2,1] is sorted using only count('1'), the result will become [4,2,1] with its original order.
But the question asked a sorted order using its own value, hence an original value is pass to sort key as (count, original_value).
This is call 'complex sorts' and the second value will be used if the first values compare are the same
'''
# (runtime / memory)
#  48 ms / 14.5 MB
