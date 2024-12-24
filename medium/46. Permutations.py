from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, used):
            # 如果路径长度等于nums长度，说明找到了一个排列
            if len(path) == len(nums):
                result.append(path[:])  # 注意要复制path
                return
            
            # 遍历所有数字
            for i in range(len(nums)):
                # 如果当前数字已使用，跳过
                if used[i]:
                    continue
                    
                # 选择当前数字
                path.append(nums[i])
                used[i] = True
                
                # 继续递归
                backtrack(path, used)
                
                # 撤销选择
                path.pop()
                used[i] = False
        
        result = []
        backtrack([], [False] * len(nums))
        return result