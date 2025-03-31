from typing import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total=0
        stack=[]
        node=root

        while node or stack:
            while node:
                stack.append(node)
                node=node.right
            node=stack.pop()
            total+=node.val
            node.val=total
            node=node.left
        return root