from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        def get(i: int) -> int:
            if i == -1 or i == n:
                return float('-inf')
            return arr[i]
        left, right, ans = 0, n - 1, -1
        while left<=right:
            mid=(left+right)//2
            if get(mid-1)<get(mid)>get(mid+1):
                return mid
            elif get(mid-1)>get(mid):
                right=mid-1
            else:
                left=mid+1