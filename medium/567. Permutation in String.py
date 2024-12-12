from typing import List
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        hashs1=[0]*26
        for c in s1:
            hashs1[ord(c)-ord("a")]+=1
        hashs2=[0]*26
        for c in s2[:len(s1)]:
            hashs2[ord(c)-ord("a")]+=1
        if hashs1==hashs2:
            return True
        for i in range(len(s2)-len(s1)):
            hashs2[ord(s2[i])-ord("a")]-=1
            hashs2[ord(s2[i+len(s1)])-ord("a")]+=1
            if hashs1==hashs2:
                return True
        return False