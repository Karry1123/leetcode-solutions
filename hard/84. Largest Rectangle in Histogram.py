from typing import List
from typing import Optional
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        size=0
        n=0
        maxsize=0
        for i in range(len(heights)):
            if not stack:
                size=heights[i]
                maxsize=max(maxsize,size)
            while stack and heights[i]<=heights[stack[-1]]:
                n=stack.pop()
                size=heights[n]*((i-stack[-1]-1)if stack else i)
                maxsize=max(maxsize,size)
            stack.append(i)
        while stack:
            n=stack.pop()
            size=heights[n]*((len(heights)-1-stack[-1])if stack else len(heights))
            maxsize=max(maxsize,size)
        return maxsize