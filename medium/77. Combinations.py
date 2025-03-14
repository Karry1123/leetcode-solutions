from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        path=[]
        def dfs(i,left):
            if left==0:
                ans.append(path.copy())
                return
            if i==n+1 or left+i>n+1:
                return
            dfs(i+1,left)
            path.append(i)
            dfs(i+1,left-1)
            path.pop()
        dfs(1,k)
        return ans