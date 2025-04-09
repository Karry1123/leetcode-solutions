from collections import deque
from typing import List
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        base, mod = 113, 10**9 + 7
    
        def check(length):
            hash1 = 0
            for i in range(length):
                hash1 = (hash1 * base + nums1[i]) % mod
            seen = {hash1}
            power = pow(base, length - 1, mod)
            for i in range(1, len(nums1) - length + 1):
                hash1 = ((hash1 - nums1[i-1] * power) * base + nums1[i+length-1]) % mod
                seen.add(hash1)
            
            hash2 = 0
            for i in range(length):
                hash2 = (hash2 * base + nums2[i]) % mod
            if hash2 in seen:
                return True
            for i in range(1, len(nums2) - length + 1):
                hash2 = ((hash2 - nums2[i-1] * power) * base + nums2[i+length-1]) % mod
                if hash2 in seen:
                    return True
            return False
        
        left, right = 0, min(len(nums1), len(nums2)) + 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1