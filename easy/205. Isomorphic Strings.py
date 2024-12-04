from typing import List
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        char={}
        t_char=[]
        for i,c in enumerate(s):
            if c in char and char[c]!=t[i]:
                return False
            if c not in char:
                if t[i] in t_char:
                    return False
                else:
                    char[c]=t[i]
                    t_char.append(t[i])
        return True