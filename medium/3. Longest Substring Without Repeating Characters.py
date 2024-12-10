from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring=""
        maxlength=0
        for i in range(len(s)):
            if s[i] not in substring:
                substring=substring+s[i]
            else:
                index=substring.find(s[i])
                substring=substring[index+1:]+s[i]
            maxlength=max(maxlength,len(substring))
        return maxlength