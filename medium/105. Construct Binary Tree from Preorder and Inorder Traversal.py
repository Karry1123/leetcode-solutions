from typing import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dic={}
        for i in range(len(inorder)):
            dic[inorder[i]]=i
        def dfs(preleft,preright,inleft,inright):
            if preleft>preright or inleft>inright:
                return None
            root = TreeNode(preorder[preleft])  # 直接创建一个节点，val=preorder[preleft]
            pindex=dic.get(root.val)
            root.left=dfs(preleft+1,pindex-inleft+preleft,inleft,pindex-1)
            root.right=dfs(pindex-inleft+preleft+1,preright,pindex+1,inright)
            return root
        return dfs(0,len(preorder)-1,0,len(inorder)-1)