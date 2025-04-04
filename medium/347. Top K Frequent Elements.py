from collections import deque
from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=Counter(nums)
        s=sorted(dic.items(), key=lambda x: -x[1])
        stack=[]
        for key,value in s:
            if k==0:
                break
            stack.append(key)
            k-=1
        return stack