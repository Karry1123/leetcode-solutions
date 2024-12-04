from typing import List
from typing import Optional
class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n==0:
            return 0
        else:
            return int(pow(n,0.5))