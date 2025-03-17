from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalindrome(i,j):
            if i >= j:
                return 1
            return ispalindrome(i + 1, j - 1) if s[i] == s[j] else -1
        
        res=[]
        path=[]
        end=len(s)-1
        def palindrome(start:int):
            if start>end:
                res.append(path.copy())
                return
            for index in range(start,end+1):
                if ispalindrome(start,index)==1:
                    path.append(s[start:index+1])
                    palindrome(index+1)
                    path.pop()
        
        palindrome(0)
        return res