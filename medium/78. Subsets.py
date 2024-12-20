from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(index, path):
            # 当遍历到某个位置时，将当前的路径（子集）加入结果
            res.append(path)
            
            # 从当前索引开始遍历，尝试包括每一个元素
            for i in range(index, len(nums)):
                # 递归地将 nums[i] 加入当前子集，并继续从 i+1 索引开始向下探索
                dfs(i + 1, path + [nums[i]])
        
        # 从索引 0 开始，初始子集为空
        dfs(0, [])
        return res