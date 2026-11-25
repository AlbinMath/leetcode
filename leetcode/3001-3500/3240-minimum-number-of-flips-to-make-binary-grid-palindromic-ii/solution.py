class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        # groups of 4
        for i in range(m // 2):
            for j in range(n // 2):
                k = (grid[i][j] + grid[i][n - 1 - j]
                     + grid[m - 1 - i][j] + grid[m - 1 - i][n - 1 - j])
                res += min(k, 4 - k)

        diff = both1 = 0

        # middle row pairs
        if m % 2:
            mid = m // 2
            for j in range(n // 2):
                a, b = grid[mid][j], grid[mid][n - 1 - j]
                if a != b:
                    diff += 1
                elif a == 1:
                    both1 += 1

        # middle column pairs
        if n % 2:
            mid = n // 2
            for i in range(m // 2):
                a, b = grid[i][mid], grid[m - 1 - i][mid]
                if a != b:
                    diff += 1
                elif a == 1:
                    both1 += 1

        # center cell
        if m % 2 and n % 2 and grid[m // 2][n // 2] == 1:
            res += 1

        res += diff
        if diff == 0 and both1 % 2:
            res += 2

        return res
