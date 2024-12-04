class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left = 0  # 指向有效元素的位置
        right = len(nums) - 1  # 指向数组的末尾
        
        while left <= right:
            if nums[left] == val:  # 左指针遇到目标值
                nums[left], nums[right] = nums[right], nums[left]  # 交换
                right -= 1  # 右指针左移
            else:
                left += 1  # 左指针右移
        
        return left  # 有效元素的长度