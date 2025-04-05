from collections import deque
from typing import List
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 构建邻接表
        graph = {i: {} for i in range(1, n+1)}
        for u, v, w in times:
            graph[u][v] = w
        
        # 初始化距离字典
        distances = {node: float('infinity') for node in graph}
        distances[k] = 0
        
        # 优先队列
        priority_queue = [(0, k)]
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            # 如果当前距离大于已记录的距离，跳过
            if current_distance > distances[current_node]:
                continue
            
            # 遍历邻居
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        max_distance = max(distances.values())
        return max_distance if max_distance < float('infinity') else -1    