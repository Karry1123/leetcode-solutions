from typing import List
from typing import Optional
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum=0
        for i in range(1,len(prices)):
            if prices[i]-prices[i-1]>0:
                sum+=prices[i]-prices[i-1]
        return sum