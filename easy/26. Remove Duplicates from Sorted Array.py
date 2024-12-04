class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return o
        
        n = len(nums)
        fast = 0
        slow = 0
        while fast < n:
            if nums[fast] == nums[slow]:
                fast=fast + 1
            else:
                slow = slow + 1
                nums[slow] = nums[fast]
        return slow+1