from collections import deque, defaultdict
from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # Build adjacency graph
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = [0] * (n + 1)  # 0: uncolored, 1: group 1, -1: group 2

        for i in range(1, n + 1):
            if color[i] != 0:
                continue

            # Start BFS for uncolored component
            queue = deque([i])
            color[i] = 1

            while queue:
                u = queue.popleft()
                for neighbor in graph[u]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[u]
                        queue.append(neighbor)
                    elif color[neighbor] == color[u]:
                        return False

        return True
