from collections import deque
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            left, right = 0, len(tails)
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num  # 仅替换，不增加长度
        return len(tails)