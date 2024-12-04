class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        i = 0
        while i < len(nums)-zero:
            if nums[i] == 0:
                del nums [i]
                nums.append(0)
                i = i-1
                zero = zero+1
            i=i+1