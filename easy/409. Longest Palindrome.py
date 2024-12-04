from typing import List
class Solution:
    def longestPalindrome(self, s: str) -> int:
        l=Counter(s)
        count1=0
        count2=0
        for c,i in l.items():
            if i%2==1:
                count1+=1
            else:
                count2+=1
        if count1<=1:
            return len(s)
        else:
            return len(s)+1-count1