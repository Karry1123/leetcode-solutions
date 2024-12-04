from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        index = len(s)-1
        for i in range(len(g)-1, -1, -1):
            if index >=0 and g[i]<=s[index]:
                count+=1
                index-=1
        return count