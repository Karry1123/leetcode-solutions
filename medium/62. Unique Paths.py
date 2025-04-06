from collections import deque
from typing import List
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n>m:
            m,n=n,m
        table=[[[] for _ in range(m)] for _ in range(n)]
        for row in range(n):
            for column in range(m):
                if column==0 or row ==0:
                    table[row][column]=1
                else:
                    table[row][column]=table[row-1][column]+table[row][column-1]
        return table[n-1][m-1]