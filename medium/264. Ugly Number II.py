from typing import List
from typing import Optional
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        stack=[1]*n
        index2,index3,index5=0,0,0
        for i in range(1,n):
            stack[i]=min(2*stack[index2],3*stack[index3],5*stack[index5])
            if stack[i]==2*stack[index2]:
                index2+=1
            if stack[i]==3*stack[index3]:
                index3+=1
            if stack[i]==5*stack[index5]:
                index5+=1
        return stack[-1]