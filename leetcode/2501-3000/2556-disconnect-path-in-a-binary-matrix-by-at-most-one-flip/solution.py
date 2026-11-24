from typing import List

class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        def find_path():
            # returns list of cells on a path, or None
            parent = {}
            stack = [(0, 0)]
            seen = {(0, 0)}
            while stack:
                r, c = stack.pop()
                if r == m - 1 and c == n - 1:
                    path = []
                    cur = (r, c)
                    while cur != (0, 0):
                        path.append(cur)
                        cur = parent[cur]
                    return path
                # push right first so down is popped first (down preferred)
                for nr, nc in ((r, c + 1), (r + 1, c)):
                    if nr < m and nc < n and grid[nr][nc] == 1 and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        parent[(nr, nc)] = (r, c)
                        stack.append((nr, nc))
            return None

        path = find_path()
        if path is None:
            return True
        for r, c in path:
            if (r, c) != (m - 1, n - 1):
                grid[r][c] = 0
        return find_path() is None
