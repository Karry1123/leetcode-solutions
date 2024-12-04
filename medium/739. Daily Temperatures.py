from typing import List
from typing import Optional
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        l=len(temperatures)
        res=[0]*l
        for i in range(l-1,-1,-1):
            while stack and temperatures[i]>=temperatures[stack[-1]]:
                stack.pop()
            if not stack:
                res[i]=0
                stack.append(i)
            else:
                res[i]=stack[-1]-i
                stack.append(i)
        return res