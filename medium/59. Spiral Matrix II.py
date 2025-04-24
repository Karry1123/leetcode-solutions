from collections import deque
from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res=[[0]*n for _ in range(n)]
        start=0
        num=1
        if n%2==1:
            res[n//2][n//2]=n*n
        while n>0:
            i,j=start,start
            for _ in range(n-1):
                res[i][j]=num
                num+=1
                j+=1
            for _ in range(n-1):
                res[i][j]=num
                num+=1
                i+=1
            for _ in range(n-1):
                res[i][j]=num
                num+=1
                j-=1
            for _ in range(n-1):
                res[i][j]=num
                num+=1
                i-=1
            n-=2
            start+=1
        return res