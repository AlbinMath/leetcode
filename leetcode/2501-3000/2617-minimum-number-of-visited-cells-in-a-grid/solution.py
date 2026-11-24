from collections import deque
from typing import List

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 1

        # row_parent[r][c] = next unvisited column index >= c in row r
        row_parent = [list(range(n + 1)) for _ in range(m)]
        # col_parent[c][r] = next unvisited row index >= r in col c
        col_parent = [list(range(m + 1)) for _ in range(n)]

        def find_row(r: int, c: int) -> int:
            path = []
            curr = c
            while row_parent[r][curr] != curr:
                path.append(curr)
                curr = row_parent[r][curr]
            for node in path:
                row_parent[r][node] = curr
            return curr

        def find_col(c: int, r: int) -> int:
            path = []
            curr = r
            while col_parent[c][curr] != curr:
                path.append(curr)
                curr = col_parent[c][curr]
            for node in path:
                col_parent[c][node] = curr
            return curr

        # Mark (0, 0) as visited in both DSUs
        row_parent[0][0] = find_row(0, 1)
        col_parent[0][0] = find_col(0, 1)

        queue = deque([(0, 0, 1)])  # (row, col, distance)

        while queue:
            r, c, d = queue.popleft()
            val = grid[r][c]

            # 1. Scan rightward in row r
            max_c = min(n - 1, c + val)
            nxt_c = find_row(r, c + 1)
            while nxt_c <= max_c:
                if r == m - 1 and nxt_c == n - 1:
                    return d + 1
                queue.append((r, nxt_c, d + 1))
                # Remove nxt_c from row r and column nxt_c
                row_parent[r][nxt_c] = find_row(r, nxt_c + 1)
                col_parent[nxt_c][r] = find_col(nxt_c, r + 1)
                nxt_c = find_row(r, nxt_c)

            # 2. Scan downward in col c
            max_r = min(m - 1, r + val)
            nxt_r = find_col(c, r + 1)
            while nxt_r <= max_r:
                if nxt_r == m - 1 and c == n - 1:
                    return d + 1
                queue.append((nxt_r, c, d + 1))
                # Remove nxt_r from column c and row nxt_r
                col_parent[c][nxt_r] = find_col(c, nxt_r + 1)
                row_parent[nxt_r][c] = find_row(nxt_r, c + 1)
                nxt_r = find_col(c, nxt_r)

        return -1
