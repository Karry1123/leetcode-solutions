from typing import List
from typing import Optional
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)==1:
            return 0
        res=0
        intervals.sort(key=lambda interval:interval[1])
        right=intervals[0][1]
        for interval in intervals[1:]:
            if interval[0]<right:
                res+=1
            else:
                right=interval[1]
        return res