from typing import List
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum = 0
        n = len(arr)
        prefixSums = [0] * (n + 1)
        for i, v in enumerate(arr):
            prefixSums[i + 1] = prefixSums[i] + v
        for start in range(n):
            length = 1
            while start + length <= n:
                end = start + length - 1
                sum += prefixSums[end + 1] - prefixSums[start]
                length += 2
        return sum