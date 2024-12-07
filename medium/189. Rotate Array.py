from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        不返回任何值，而是原地修改 nums。
        """
        l = len(nums)  # 获取数组长度
        move = k % l   # 计算实际需要移动的步数（防止 k 超过数组长度）
        
        # 整体翻转数组
        nums[:] = nums[::-1]
        
        # 翻转前 move 个元素
        nums[:move] = nums[:move][::-1]
        
        # 翻转剩余的元素
        nums[move:] = nums[move:][::-1]