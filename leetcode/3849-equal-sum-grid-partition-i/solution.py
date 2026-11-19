from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(map(sum, grid))
        if total % 2:
            return False
        half = total // 2

        # horizontal cuts: after row i, for i in 0..m-2
        acc = 0
        for i in range(m - 1):
            acc += sum(grid[i])
            if acc == half:
                return True

        # vertical cuts: after column j, for j in 0..n-2
        col = [0] * n
        for row in grid:
            for j, v in enumerate(row):
                col[j] += v
        acc = 0
        for j in range(n - 1):
            acc += col[j]
            if acc == half:
                return True

        return False
