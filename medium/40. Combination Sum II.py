from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        path=[]
        
        def dfs(i,left):
            if left==0:
                ans.append(path.copy())
                return
            
            if i==len(candidates) or candidates[i]>left:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[j] > left:
                    break
                path.append(candidates[j])
                dfs(j + 1, left - candidates[j])
                path.pop()

        dfs(0,target)
        return ans