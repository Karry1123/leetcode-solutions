from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        a =  int(len(nums3))
        if len(nums3) % 2 == 0 :
            mid_num = (nums3[int(a / 2)] + nums3[int((a / 2) - 1)]) / 2
        else:
            mid_num = nums3[int((a - 1) / 2)]
        return mid_num