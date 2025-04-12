from collections import deque
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f = [[-inf] * 2 for _ in range(4)]
        for j in range(1, 4):
            f[j][0] = 0
        for p in prices:
            for j in range(3, 0, -1):
                f[j][0] = max(f[j][0], f[j][1] + p)
                f[j][1] = max(f[j][1], f[j - 1][0] - p)
        return f[-1][0]