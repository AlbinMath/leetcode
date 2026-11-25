class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        top, bottom = m, -1
        left, right = n, -1

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    top = min(top, i)
                    bottom = max(bottom, i)
                    left = min(left, j)
                    right = max(right, j)

        return (bottom - top + 1) * (right - left + 1)
