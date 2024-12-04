from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 创建一个字典保存值和索引的映射
        num_to_index = {}
        for i, num in enumerate(nums):
            # 检查是否存在目标值所需的配对数
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            # 将当前数及其索引加入字典
            num_to_index[num] = i
        return []