class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i = 0
        result = []

        while i < len(nums):
            result.extend([nums[i+1]]*nums[i])
            i += 2
        return result
'''
(runtime / memory)
 56 ms / 14.7 MB
'''       


''' (68 ms / 14.6 MB)
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i = 0
        result = []

        while i < len(nums):
            result += [nums[i+1]]*nums[i]
            i += 2
        return result
'''


''' (56 ms / 14.5 MB)
    def decompressRLElist(self, nums: List[int]) -> List[int]:
            result = []
            
            for i in range(0, len(nums)-1, 2):
                result += ([nums[i+1]] * nums[i])
            return result
'''
    
