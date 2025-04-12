from collections import deque
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        f0, f1 = 0, -inf
        for p in prices:
            f0, f1 = max(f0, f1 + p - fee), max(f1, f0 - p)
        return f0