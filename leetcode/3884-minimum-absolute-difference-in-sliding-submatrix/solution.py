class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                vals = sorted({grid[x][y]
                               for x in range(i, i + k)
                               for y in range(j, j + k)})
                if len(vals) > 1:
                    ans[i][j] = min(b - a for a, b in zip(vals, vals[1:]))

        return ans
