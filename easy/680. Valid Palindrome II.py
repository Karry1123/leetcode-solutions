from typing import List
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        i=0
        l=len(s)
        while i<l-1-i:
            if s[i]!=s[l-1-i]:
                s1=s[i+1:l-i]
                s2=s[i:l-i-1]
                return s1==s1[::-1] or s2==s2[::-1]
            i+=1