from typing import List
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root, temp):
            if not root:
                return temp  # 返回当前深度
            temp += 1
            left_depth = depth(root.left, temp)
            right_depth = depth(root.right, temp)
            return max(left_depth, right_depth)
        return depth(root, 0)