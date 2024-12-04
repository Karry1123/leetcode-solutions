from typing import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        dic={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        string=[]
        for i in range(len(s)):
            if s[i] in dic:
                string.append(s[i])
        return string==string[::-1]