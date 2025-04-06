from collections import deque
from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]  # 路径压缩
                u = parent[u]
            return u
        
        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u == root_v:
                return False  # 已经连通，合并失败
            parent[root_v] = root_u
            return True
        
        # 初始化，每个节点是自己的父节点
        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
        
        # 处理边
        for u, v in edges:
            if not union(u, v):
                return [u, v]