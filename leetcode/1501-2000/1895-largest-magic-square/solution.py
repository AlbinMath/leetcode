class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = [[0] * (n + 2) for _ in range(m + 2)]
        col = [[0] * (n + 2) for _ in range(m + 2)]
        d1 = [[0] * (n + 2) for _ in range(m + 2)]
        d2 = [[0] * (n + 2) for _ in range(m + 2)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                v = grid[i - 1][j - 1]
                row[i][j] = row[i][j - 1] + v
                col[i][j] = col[i - 1][j] + v
                d1[i][j] = d1[i - 1][j - 1] + v
                d2[i][j] = d2[i - 1][j + 1] + v

        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    target = d1[r + k][c + k] - d1[r][c]
                    if d2[r + k][c + 1] - d2[r][c + k + 1] != target:
                        continue
                    ok = True
                    for x in range(k):
                        if row[r + x + 1][c + k] - row[r + x + 1][c] != target:
                            ok = False
                            break
                        if col[r + k][c + x + 1] - col[r][c + x + 1] != target:
                            ok = False
                            break
                    if ok:
                        return k
        return 1
