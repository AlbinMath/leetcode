class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0

        for _ in range(k):
            ndp = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for dx, dy in moves:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n:
                            ndp[x][y] += dp[i][j] / 8
            dp = ndp

        return sum(map(sum, dp))
