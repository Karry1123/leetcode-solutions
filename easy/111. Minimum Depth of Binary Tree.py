from typing import List
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # 初始化队列，存储节点及其深度
        queue = deque([(root, 1)])  # (节点, 深度)
        
        while queue:
            node, depth = queue.popleft()  # 取出队首节点及其深度
            
            # 如果当前节点是叶子节点，返回当前深度
            if not node.left and not node.right:
                return depth
            
            # 将左子节点加入队列
            if node.left:
                queue.append((node.left, depth + 1))
            
            # 将右子节点加入队列
            if node.right:
                queue.append((node.right, depth + 1))