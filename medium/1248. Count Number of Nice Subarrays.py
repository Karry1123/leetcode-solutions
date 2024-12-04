from typing import List
from typing import Optional
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        stack=[0]
        left,right=0,0
        res=0
        for i,v in enumerate(nums):
            if v%2==1:
                stack.append(i+1)
                right+=1
                if right-left==k+1:
                    left+=1
                    res+=(stack[right]-stack[right-1])*(stack[left]-stack[left-1])
        stack.append(len(nums)+1)
        right+=1
        if right-left==k+1:
            left+=1
            res+=(stack[right]-stack[right-1])*(stack[left]-stack[left-1])
        return res