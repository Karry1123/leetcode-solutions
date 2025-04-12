from collections import deque
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre0, f0, f1, = 0, 0, -inf
        for p in prices:
            pre0, f0, f1 = f0, max(f0, f1 + p), max(f1, pre0 - p)
        return f0