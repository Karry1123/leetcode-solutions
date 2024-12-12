from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []
        
        dq = deque()  # 双端队列，存储元素的索引
        result = []
        
        for i in range(len(nums)):
            # 移除滑出窗口的元素索引
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # 移除队列中所有小于当前元素的索引（保持队列递减）
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # 将当前元素的索引加入队列
            dq.append(i)
            
            # 窗口形成后，记录最大值
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result