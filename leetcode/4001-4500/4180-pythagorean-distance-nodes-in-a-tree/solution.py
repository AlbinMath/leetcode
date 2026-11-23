from collections import deque
from typing import List

class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(src):
            dist = [-1] * n
            dist[src] = 0
            q = deque([src])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return dist

        dx, dy, dz = bfs(x), bfs(y), bfs(z)
        ans = 0
        for u in range(n):
            a, b, c = sorted((dx[u], dy[u], dz[u]))
            if a * a + b * b == c * c:
                ans += 1
        return ans
