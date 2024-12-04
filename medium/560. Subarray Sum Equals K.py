from typing import List
from typing import Optional
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums, res = 0, 0
        dt = {0: 1}
        for num in nums:
            sums += num
            res += dt.get(sums - k, 0)
            dt[sums] = dt.get(sums, 0) + 1

        return res