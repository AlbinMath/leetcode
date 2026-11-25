class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for t in range(k // 2):
            a, b = x + t, x + k - 1 - t
            grid[a][y:y + k], grid[b][y:y + k] = grid[b][y:y + k], grid[a][y:y + k]
        return grid
