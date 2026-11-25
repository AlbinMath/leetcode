class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        for j in range(n):
            prev = grid[0][j]
            for i in range(1, m):
                if grid[i][j] <= prev:
                    prev += 1
                    res += prev - grid[i][j]
                else:
                    prev = grid[i][j]

        return res
