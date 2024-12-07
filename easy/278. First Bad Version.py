from typing import List
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def find(first,last):
            mid=(first+last)//2
            if mid==1 and isBadVersion(mid):
                return 1
            if not isBadVersion(mid):
                return find(mid+1,last)
            else:
                if not isBadVersion(mid-1):
                    return mid
                return find(first,mid-1)
        return find(1,n)