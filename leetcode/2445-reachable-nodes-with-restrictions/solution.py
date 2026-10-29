from collections import deque
from typing import List

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        is_restricted = [False] * n
        for node in restricted:
            is_restricted[node] = True

        adj = [[] for _ in range(n)]
        for u, v in edges:
            if not is_restricted[u] and not is_restricted[v]:
                adj[u].append(v)
                adj[v].append(u)

        visited = [False] * n
        queue = deque([0])
        visited[0] = True
        reachable_count = 0

        while queue:
            node = queue.popleft()
            reachable_count += 1
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return reachable_count
