class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [0] * n
        for row in grid:
            for j, v in enumerate(row):
                ans[j] = max(ans[j], len(str(v)))
        return ans
