from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic={}
        start,end=0,0
        ans,total=0,0
        while end<len(nums):
            if nums[end] not in dic:
                dic[nums[end]]=end
                total+=nums[end]
                ans=max(ans,total)
            elif nums[end] in dic and start>dic[nums[end]]:
                dic[nums[end]]=end
                total+=nums[end]
                ans=max(ans,total)
            else:
                while start<=dic[nums[end]]:
                    total-=nums[start]
                    start+=1
                dic[nums[end]]=end
                total+=nums[end]
            end+=1
        return ans