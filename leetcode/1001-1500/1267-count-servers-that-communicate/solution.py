class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_count = [0] * m
        col_count = [0] * n

        # Pass 1: Count servers in each row and column
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1

        # Pass 2: Count servers that can communicate
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (row_count[r] > 1 or col_count[c] > 1):
                    ans += 1

        return ans
