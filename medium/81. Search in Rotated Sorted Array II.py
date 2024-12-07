from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def binarysearch(left,right):
            if left>right:
                return False
            medium=(left+right)//2
            if nums[medium]==target or nums[left]==target or nums[right]==target:
                return True
            # 处理重复元素的特殊情况
            while left < medium and nums[left] == nums[medium]:
                left += 1
            while right > medium and nums[right] == nums[medium]:
                right -= 1
            # 如果左半部分是有序的
            if nums[left] <= nums[medium]:
                # 判断目标是否在左半部分
                if nums[left] <= target < nums[medium]:
                    return binarysearch(left, medium - 1)
                else:
                    return binarysearch(medium + 1, right)
            else:
                # 否则右半部分是有序的
                if nums[medium] < target <= nums[right]:
                    return binarysearch(medium + 1, right)
                else:
                    return binarysearch(left, medium - 1)
        return binarysearch(0,len(nums)-1)