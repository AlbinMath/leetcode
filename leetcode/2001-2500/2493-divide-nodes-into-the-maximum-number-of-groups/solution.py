from collections import deque
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 1. Check bipartiteness and identify components
        color = [0] * (n + 1)
        components = []

        for i in range(1, n + 1):
            if color[i] != 0:
                continue

            current_comp = []
            queue = deque([i])
            color[i] = 1

            while queue:
                u = queue.popleft()
                current_comp.append(u)
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = -color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return -1  # Odd cycle detected; impossible to partition

            components.append(current_comp)

        # 2. Helper to compute max BFS depth from a starting node
        def max_groups_from(start: int) -> int:
            dist = {start: 1}
            queue = deque([start])
            max_depth = 1

            while queue:
                curr = queue.popleft()
                for neighbor in adj[curr]:
                    if neighbor not in dist:
                        dist[neighbor] = dist[curr] + 1
                        max_depth = max(max_depth, dist[neighbor])
                        queue.append(neighbor)

            return max_depth

        # 3. For each component, pick the start node maximizing BFS depth
        total_groups = 0
        for comp in components:
            comp_max = max(max_groups_from(node) for node in comp)
            total_groups += comp_max

        return total_groups
