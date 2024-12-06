from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        another method for this problem for this problem is hashset, but memory: O(n)
        the first time see a num, add it to hashset, the second time remove it
        """
        # XOR (order does not matter)
        result = 0
        for num in nums:
            result = result ^ num
        return resul