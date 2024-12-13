from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        change=[[0,0] for _ in range(len(nums))]
        for i in range(len(nums)):
            string=str(nums[i])
            l=len(string)
            div="1"*l
            change[i][0]=nums[i]/int(div)
            change[i][1]=nums[i]
        change.sort(reverse=True)
        res=""
        for item in change:
            res=res+str(item[1])
        if int(res)==0:
            return "0"
        return res