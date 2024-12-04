from typing import List
from typing import Optional
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        stack=[]
        l=len(nums)
        for i in range(l-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            elif nums[i] + nums[i + 1] + nums[i + 2] +nums[i + 3] > target:
                break
            elif nums[i] + nums[l - 3] + nums[l - 2] +nums[l - 1] < target:
                continue
            else:
                f=i+1
                while f<=l-3:
                    s=f+1
                    t=l-1
                    while s<t:
                        sum=nums[i]+nums[f]+nums[s]+nums[t]
                        if sum==target:
                            stack.append([nums[i],nums[f],nums[s],nums[t]])
                            while s<t and nums[s]==nums[s+1]:
                                s+=1
                            while s<t and nums[t]==nums[t-1]:
                                t-=1
                            s+=1
                            t-=1
                        elif sum<target:
                            s+=1
                        else:
                            t-=1
                    while f<=l-3 and nums[f]==nums[f+1]:
                        f+=1
                    f+=1
        return stack