from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == k:
            return sum(nums) / k
        cur_sum = sum(nums[0:k])
        max_sum = cur_sum
        for i in range(k, len(nums)):
            cur_sum = cur_sum - nums[i-k] + nums[i]
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum / k