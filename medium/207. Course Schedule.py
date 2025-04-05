from collections import deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i:[] for i in range(0,numCourses)}
        for u,v in prerequisites:
            graph[u].append(v)
        visited=set()
        recursion=set()
        def dfs(node):
            visited.add(node)
            recursion.add(node)
            for neighbor in graph.get(node,[]):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in recursion:
                    return True
            recursion.remove(node)
            return False
        
        for node in graph:
            if node not in visited:
                if dfs(node):
                    return False
        return True