class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        NEG = float('-inf')
        res = NEG

        def best_len2(a):
            best = NEG
            e2 = NEG
            for j in range(1, len(a)):
                e2 = a[j] + max(a[j - 1], e2)
                best = max(best, e2)
            return best

        for row in grid:
            res = max(res, best_len2(row))
        for col in zip(*grid):
            res = max(res, best_len2(col))

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                res = max(res, grid[i][j])

        return res
