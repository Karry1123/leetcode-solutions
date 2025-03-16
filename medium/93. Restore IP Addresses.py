from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        ip=""
        
        def isvalid(string):
            if len(string)>len(str(int(string))):
                return False
            if int(string)>=0 and int(string)<=255:
                return True
            return False

        for a in range(1,len(s)-2):
            if not isvalid(s[:a]):
                break
            for b in range(a+1,len(s)-1):
                if not isvalid(s[a:b]):
                    break
                for c in range(b+1,len(s)):
                    if not isvalid(s[b:c]):
                        break
                    if isvalid(s[c:]):
                        ip=ip+s[:a]+"."+s[a:b]+"."+s[b:c]+"."+s[c:]
                        res.append(ip)
                        ip=""
        return res