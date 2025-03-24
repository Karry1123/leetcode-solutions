from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=len(height)
        left=0
        right=l-1
        maxheight=max(height)
        maxvolume=0
        while left<right:
            width=right-left
            if maxheight*width < maxvolume:
                break
            l_h=height[left]
            r_h=height[right]
            real_height=min(l_h,r_h)
            realvolume=real_height*width
            if realvolume>maxvolume:
                maxvolume=realvolume
            if l_h < r_h:
                left += 1
            else:
                right -= 1
        return maxvolume