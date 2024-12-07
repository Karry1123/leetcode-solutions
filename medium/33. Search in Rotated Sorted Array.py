from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarysearch(nums,left,right,target):
            if left>right:
                return -1
            if nums[left]==target:
                return left
            if nums[right]==target:
                return right
            medium=(left+right)//2
            if nums[medium]==target:
                return medium
            if nums[left]>nums[right]:
                if nums[medium]>target:
                    if nums[medium]>nums[left] and nums[right]>target:
                        return binarysearch(nums,medium+1,right,target)
                    else:
                        return binarysearch(nums,left,medium-1,target)
                else:
                    if nums[medium]<nums[right] and nums[left]<target:
                        return binarysearch(nums,left,medium-1,target)
                    else:
                        return binarysearch(nums,medium+1,right,target)
            else:
                if nums[medium]>target:
                    return binarysearch(nums,left,medium-1,target)
                else:
                    return binarysearch(nums,medium+1,right,target)
        return binarysearch(nums,0,len(nums)-1,target)