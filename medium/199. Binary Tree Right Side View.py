from typing import Optional
from typing import List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if root:
            q=deque([root])
            while q:
                node=q[-1]
                res.append(node.val)
                l=len(q)
                while l>0:
                    node=q.popleft()
                    l-=1
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                
        return res