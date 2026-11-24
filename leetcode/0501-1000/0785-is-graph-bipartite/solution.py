from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n  # 0: unvisited, 1: color A, -1: color B
        
        for i in range(n):
            if color[i] != 0:
                continue
            
            # Start BFS from unvisited component
            queue = deque([i])
            color[i] = 1
            
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == 0:
                        color[v] = -color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
                        
        return True
