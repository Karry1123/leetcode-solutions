from collections import deque
from typing import List
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<4:
            return n
        p,q,r=1,2,3
        for n in range(4,n+1):
            p,q=q,r
            r=p+q
        return r  