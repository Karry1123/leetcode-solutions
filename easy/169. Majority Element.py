from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        res = nums[0]
        for x in nums:
            if cnt == 0:
                res = x
            if res == x:
                cnt += 1
            else:
                cnt -= 1
        return res
        #Boyer-Moore 投票算法 找众数