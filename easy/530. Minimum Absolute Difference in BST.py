from typing import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack=[]
        minnum=float("inf")
        def find(root):
            if not root:
                return
            find(root.left)
            if not stack:
                stack.append(root.val)
            else:
                nonlocal minnum
                minnum=min(minnum,root.val-stack[-1])
                stack.append(root.val)
            find(root.right)
        find(root)
        return minnum