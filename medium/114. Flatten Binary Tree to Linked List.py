# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                # 找到左子树的最右节点
                pre = cur.left
                while pre.right:
                    pre = pre.right
                
                # 把右子树接到左子树的最右节点
                pre.right = cur.right
                
                # 把左子树移到右边
                cur.right = cur.left
                cur.left = None
            
            # 移动到下一个节点
            cur = cur.right