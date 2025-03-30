from typing import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack=[]
        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if stack:
                num=stack[-1]
                stack.append(root.val)
                if num>=stack[-1]:
                    return False
            else:
                stack.append(root.val)
            return inorder(root.right)
        return inorder(root)