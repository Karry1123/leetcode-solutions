from typing import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def calculate_depth(node):
            """
            计算完全二叉树的左子树深度
            """
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth
        
        def count_nodes(root):
            """
            计算完全二叉树的节点个数
            时间复杂度：O((logN)^2)
            """
            if not root:
                return 0
            
            # 计算左子树深度
            left_depth = calculate_depth(root.left)
            # 计算右子树深度
            right_depth = calculate_depth(root.right)
            
            if left_depth == right_depth:
                # 左子树是满二叉树
                return (1 << left_depth) + count_nodes(root.right)
            else:
                # 右子树是满二叉树（少一层）
                return (1 << right_depth) + count_nodes(root.left)
        return count_nodes(root)