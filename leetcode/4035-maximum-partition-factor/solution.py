from collections import deque
from typing import List

class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 2:
            return 0

        # Precompute all pairwise Manhattan distances
        dist = [[0] * n for _ in range(n)]
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                d = abs(x1 - x2) + abs(y1 - y2)
                dist[i][j] = d
                dist[j][i] = d

        def is_bipartite(M: int) -> bool:
            color = [0] * n

            for i in range(n):
                if color[i] != 0:
                    continue

                color[i] = 1
                queue = deque([i])

                while queue:
                    u = queue.popleft()
                    for v in range(n):
                        if dist[u][v] < M and u != v:
                            if color[v] == 0:
                                color[v] = -color[u]
                                queue.append(v)
                            elif color[v] == color[u]:
                                return False  # Odd cycle detected

            return True

        low, high = 1, 4 * 10**8
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if is_bipartite(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
