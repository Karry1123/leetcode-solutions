from typing import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(root, res, depth):
            if not root:
                return 
            if len(res)-1 < depth:
                res.append([])
            res[depth].append(root.val)
            dfs(root.left, res, depth+1)
            dfs(root.right, res, depth+1)
        dfs(root, res, 0)
        return res