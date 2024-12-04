from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        re5=0
        re10=0
        for i in range(0,len(bills)):
            if bills[i]==5:
                re5+=1
            elif bills[i]==10 and re5>=1:
                re5-=1
                re10+=1
            elif bills[i]==20 and re10>=1 and re5>=1:
                re10-=1
                re5-=1
            elif bills[i]==20 and re5>=3:
                re5-=3
            else:
                return False
        return True