from typing import List
from typing import Optional
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count=0
        index=0
        times=1
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
                index=i
            else:
                times*=nums[i]
        res=[0]*len(nums)
        if count>=2:
            return res
        elif count==1:
            res[index]=times
            return res
        else:
            for i in range(len(nums)):
                res[i]=int(times/nums[i])
            return res