from typing import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(root,p,q):
            if not root:
                return None
            if root==p or root==q:
                return root
            left=find(root.left,p,q)
            right=find(root.right,p,q)

            if left and right:
                return root
            elif left:
                return left
            else:
                return right
        return find(root,p,q)