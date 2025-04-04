from collections import deque
from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic=Counter(words)
        stack=[]
        s=sorted(dic.items(), key=lambda x:(-x[1],x[0]))
        for key,value in s:
            if k==0:
                break
            stack.append(key)
            k-=1
        return stack