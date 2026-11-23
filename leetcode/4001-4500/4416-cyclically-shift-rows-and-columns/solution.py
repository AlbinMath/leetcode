class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]],
                    rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        # shift rows left
        rows = [grid[i][rowShift[i]:] + grid[i][:rowShift[i]] for i in range(n)]
        # shift columns up
        res = [[0] * n for _ in range(n)]
        for j in range(n):
            k = colShift[j]
            for i in range(n):
                res[i][j] = rows[(i + k) % n][j]
        return res
