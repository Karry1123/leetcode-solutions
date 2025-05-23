from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack=[intervals[0]]
        for i in intervals[1:]:
            if i[0]<=stack[-1][1]:
                stack[-1][1]=max(i[1],stack[-1][1])
            else:
                stack.append(i)
        return stack