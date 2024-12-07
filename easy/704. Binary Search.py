from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarysearch(nums,left,right,target):
            if left>right:
                return-1
            medium=(left+right)//2
            if nums[medium]==target:
                return medium
            elif nums[medium]<target:
                return binarysearch(nums,medium+1,right,target)
            else:
                return binarysearch(nums,left,medium-1,target)
        return binarysearch(nums,0,len(nums)-1,target)