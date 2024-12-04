from typing import List
from typing import Optional
class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[]
        l=len(height)
        v=0
        n=0
        for i in range(l):
            while stack and height[i]>height[stack[-1]]:
                n=stack.pop()
                h=height[n]
                if stack and height[i]>=height[stack[0]]:
                    v+=(height[stack[0]]-h)*(n-stack[-1])
                if stack and height[i]<height[stack[0]]:
                    v+=(height[i]-h)*(n-stack[-1])
            stack.append(i)
        return v