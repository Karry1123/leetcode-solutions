from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []  # 单调栈，栈底到栈顶递减
        for num in nums:
            node = TreeNode(num)  # 为当前元素创建节点
            while stack and stack[-1].val < num:
                # 如果当前节点比栈顶节点大，则栈顶节点是当前节点的左子节点
                node.left = stack.pop()
            if stack:
                # 如果栈不为空，则当前节点是栈顶节点的右子节点
                stack[-1].right = node
            stack.append(node)  # 将当前节点压入栈
        return stack[0]  # 栈底的节点是最大二叉树的根节点