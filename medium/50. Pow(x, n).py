from typing import List
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n=-n
        res=1
        stack=[]
        while n>0:
            if n%2==1:
                stack.append(1)
            else:
                stack.append(0)
            n=n//2
        while stack:
            if stack[-1]==1:
                res=x*res*res
            else:
                res=res*res
            stack.pop()
        return res