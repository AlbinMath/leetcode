class Solution(object):
    def matrixScore(self, grid):
        m, n = len(grid), len(grid[0])

        # Column 0 becomes all 1s after row flips: each row contributes 2^(n-1)
        score = m * (1 << (n - 1))

        for j in range(1, n):
            # Number of ones in column j after normalizing rows so grid[i][0] == 1
            ones = sum(grid[i][j] ^ grid[i][0] for i in range(m))
            # Flip the column if that gives more ones
            score += max(ones, m - ones) * (1 << (n - 1 - j))

        return score
