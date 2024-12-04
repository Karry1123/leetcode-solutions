from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1=list(set(nums1))
        l1.sort()
        l2=list(set(nums2))
        l2.sort()
        res=[]
        m,n=0,0
        while m<len(l1) and n<len(l2):
            if l1[m]<l2[n]:
                m+=1
            elif l1[m]>l2[n]:
                n+=1
            else:
                res.append(l1[m])
                m+=1
                n+=1
        return res