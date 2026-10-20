from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float('inf')] * n
        seen = [False] * n
        dist[0] = cost = 0

        for _ in range(n):
            u = min((dist[i], i) for i in range(n) if not seen[i])[1]
            seen[u] = True
            cost += dist[u]
            x, y = points[u]

            for v, (a, b) in enumerate(points):
                if not seen[v]:
                    dist[v] = min(dist[v], abs(x-a) + abs(y-b))

        return cost
