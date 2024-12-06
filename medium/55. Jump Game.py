from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l=len(nums)
        if l==1 or nums[0]==l-1:
            return True
        if nums[0]==0:
            return False
        cur=0
        for i in range(1,l):
            if nums[i]>=l-1-i:
                return True
            if nums[i]>nums[cur]-i+cur:
                cur=i
            else:
                if nums[cur]==i-cur:
                    return False