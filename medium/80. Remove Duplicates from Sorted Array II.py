from typing import List
from typing import Optional
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count,move=0,0
        l=len(nums)
        num=[]
        for i in range(l):
            if not num:
                num.append(nums[i])
                count+=1
            elif num[0]==nums[i] and count<2:
                count+=1
                nums[i-move]=nums[i]
            elif num[0]==nums[i] and count==2:
                move+=1
            else:
                num[0]=nums[i]
                nums[i-move]=nums[i]
                count=1
        for i in range(move):
            nums.pop()
        return len(nums)