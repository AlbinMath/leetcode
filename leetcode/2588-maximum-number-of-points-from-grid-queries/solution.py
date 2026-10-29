import heapq
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        k = len(queries)

        # Sort queries while preserving original indices
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])

        ans = [0] * k
        visited = [[False] * n for _ in range(m)]

        # Min-heap stores: (grid[r][c], r, c)
        pq = [(grid[0][0], 0, 0)]
        visited[0][0] = True

        points = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for orig_idx, q_val in sorted_queries:
            # Expand all reachable boundary cells with value strictly less than q_val
            while pq and pq[0][0] < q_val:
                val, r, c = heapq.heappop(pq)
                points += 1

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        visited[nr][nc] = True
                        heapq.heappush(pq, (grid[nr][nc], nr, nc))

            ans[orig_idx] = points

        return ans
