from collections import deque
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')   # smallest value seen so far
        second = float('inf')  # second smallest value seen so far
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                # Found a number larger than both first and second
                return True
        
        return False