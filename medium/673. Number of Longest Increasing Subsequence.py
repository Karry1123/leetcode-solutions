from collections import deque
from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        def lower_bound(nums, target):
            # 从大到小
            # 找到刚好比target小的
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def upper_bound(nums, target):
            # 从小到大
            # 找到刚好不比target小的下标
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        

        p = [nums[0]]           # 桶顶元素，也就是最小的，在列表尾部
        path_counts = [[1]]     # 对应桶位置上的每个元素作结尾的路径和
        buckets = [[nums[0]]]   # 多个桶，桶的个数就是路径长度
        # 最长路径个数就是把最后一个桶各个元素作结尾的路径和加起来  这里可以使用前缀和，这里还没用


        for i in range(1, len(nums)):
            if nums[i] > p[-1]: # 开辟新桶
                local = lower_bound(buckets[-1], nums[i])  # 在前一个桶中找到严格小于nums[i]的下标
                buckets.append([nums[i]])
                p.append(nums[i])
                path_counts.append([sum(path_counts[-1][local: ])])
            else:
                # nums[i]应该放在p中刚好不比nums[i]小的索引上
                k = upper_bound(p, nums[i])     # nums[i] 放到索引为k的桶中
                buckets[k].append(nums[i])
                p[k] = nums[i]
                if k == 0:  # 如果要放在第0个桶里，那就不能找前一个桶，路径和初始化为1
                    path_counts[0].append(1)
                else:
                    local = lower_bound(buckets[k - 1], nums[i])
                    path_counts[k].append(sum(path_counts[k-1][local:]))
                    
        return sum(path_counts[-1])