class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                on_diag = (i == j) or (i + j == n - 1)
                if on_diag != (grid[i][j] != 0):
                    return False
        return True
