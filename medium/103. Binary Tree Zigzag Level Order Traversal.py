from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]

        def dfs(root:Optional[TreeNode],index:int):
            if not root:
                return
            if index==len(res):
                res.append([])
            res[index].append(root.val)
            dfs(root.left,index+1)
            dfs(root.right,index+1)
        
        dfs(root,0)
        i=1
        while i<len(res):
            res[i]=res[i][::-1]
            i+=2
        return res