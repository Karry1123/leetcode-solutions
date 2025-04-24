from collections import deque
from typing import List
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip()
        end=len(s)-1
        res=0
        while s[end]!=" " and end>=0:
            end-=1
            res+=1
        return res