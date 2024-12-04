from typing import List
from typing import Optional
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        presum = {}  # 使用字典存储累积和的首次出现位置
        cur = 0  # 当前累积和
        res = 0  # 最终结果

        for i, h in enumerate(hours, 1):
            # 更新累积和
            cur += 1 if h > 8 else -1

            # 如果累积和小于 0，从头到当前位置的时间段表现良好
            if cur > 0:
                res = i
            else:
                # 如果 cur - 1 存在于字典中，尝试更新结果
                if cur - 1 in presum:
                    res = max(res, i - presum[cur - 1])
                # 如果 cur 尚未记录，存储其首次出现的位置
                if cur not in presum:
                    presum[cur] = i

        return res