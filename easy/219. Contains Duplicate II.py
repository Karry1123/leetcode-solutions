from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False
        num_index={}
        for i,num in enumerate(nums):
            if num in num_index and i-num_index[num]<=k:
                return True
            if num in num_index:
                num_index[num]=i
            num_index[num]=i
        return False  