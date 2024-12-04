class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        total = 0
        i = 0
        num = 0
        for i in range(len(nums)):
            if nums[i]==0:
                num=0
            else:
                num = num+1
                if num > total:
                    total = num
        return total