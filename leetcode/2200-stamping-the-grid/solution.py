class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])

        # prefix sum of grid
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                P[i + 1][j + 1] = P[i][j + 1] + P[i + 1][j] - P[i][j] + grid[i][j]

        # difference array for stamps
        D = [[0] * (n + 2) for _ in range(m + 2)]
        for r in range(m - stampHeight + 1):
            for c in range(n - stampWidth + 1):
                r2, c2 = r + stampHeight, c + stampWidth
                if P[r2][c2] - P[r][c2] - P[r2][c] + P[r][c] == 0:
                    D[r][c] += 1
                    D[r][c2] -= 1
                    D[r2][c] -= 1
                    D[r2][c2] += 1

        # accumulate and verify coverage
        cover = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                cover[i + 1][j + 1] = (
                    cover[i][j + 1] + cover[i + 1][j] - cover[i][j] + D[i][j]
                )
                if grid[i][j] == 0 and cover[i + 1][j + 1] == 0:
                    return False
        return True
