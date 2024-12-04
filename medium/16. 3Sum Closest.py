from typing import List
from typing import Optional
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=len(nums)
        best=nums[0]+nums[1]+nums[2]
        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur


        for i in range(l-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            s=nums[i]+nums[i+1]+nums[i+2]
            if s>target:
                update(s)
                continue
                
            s=nums[i]+nums[-2]+nums[-1]
            if s<target:
                update(s)
                continue
            left=i+1
            right=l-1
            while left<right:
                if nums[i]+nums[left]+nums[right]==target:
                    return target
                elif nums[i]+nums[left]+nums[right]>target:
                    update(nums[i]+nums[left]+nums[right])
                    while(left<right and nums[right]==nums[right-1]):
                        right=right-1
                    right-=1
                else:
                    update(nums[i]+nums[left]+nums[right])
                    while(left<right and nums[left]==nums[left+1]):
                        left=left+1
                    left+=1
        return best