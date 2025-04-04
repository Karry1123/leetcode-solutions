from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n and m:
            nums1[m+n-1]=max(nums1[m-1],nums2[n-1])
            if nums1[m+n-1]==nums1[m-1]:
                m-=1
            else:
                n-=1
        while m==0 and n:
            nums1[n-1]=nums2[n-1]
            n-=1