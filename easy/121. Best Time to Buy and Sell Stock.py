from collections import deque
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = inf
        max_price = -1
        result = 0
        
        for price in prices:
            # 如果当前价格比之前记录的最低价格还要低
            if price < min_price:
                min_price = price  # 更新最低价格
                max_price = -1  # 重置最高价格（意味着交易必须从新的低点开始）
                continue  # 继续遍历下一个价格

            # 如果当前价格比记录的最高价格还要高
            if price > max_price:
                max_price = price  # 更新最高价格
                # 计算当前可能的最大利润，并更新全局最大利润
                result = max(result, max_price - min_price)

        return result  # 返回最大利润