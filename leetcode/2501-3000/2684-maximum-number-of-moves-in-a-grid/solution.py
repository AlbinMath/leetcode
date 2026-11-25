class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        reach = [True] * m  # reachable rows in the current column

        for c in range(n - 1):
            nxt = [False] * m
            for r in range(m):
                if not reach[r]:
                    continue
                for nr in (r - 1, r, r + 1):
                    if 0 <= nr < m and grid[nr][c + 1] > grid[r][c]:
                        nxt[nr] = True
            if not any(nxt):
                return c
            reach = nxt

        return n - 1
