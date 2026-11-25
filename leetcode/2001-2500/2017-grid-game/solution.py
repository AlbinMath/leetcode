class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top = sum(grid[0])  # will become sum of top cells after column i
        bottom = 0          # sum of bottom cells before column i
        res = float('inf')

        for i in range(len(grid[0])):
            top -= grid[0][i]
            res = min(res, max(top, bottom))
            bottom += grid[1][i]

        return res
