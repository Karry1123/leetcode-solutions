from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixsum=[0]*(len(nums)+1)
        for i,v in enumerate(nums):
            prefixsum[i+1]=prefixsum[i]+v
        for i in range(1,len(prefixsum)):
            if prefixsum[i-1]==prefixsum[-1]-prefixsum[i]:
                return i-1
        return -1