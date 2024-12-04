from typing import List
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 and x % 10 == 0:
            return False
        
        i = x
        y = 0
        while i > 0:
            y = y * 10 + i % 10
            i = i // 10
        
        if x == y:
            return True
        else:
            return False