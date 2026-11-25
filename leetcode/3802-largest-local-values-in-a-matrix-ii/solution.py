class Solution:
    def countLocalMaximums(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        groups = {}
        for i in range(n):
            for j in range(m):
                x = matrix[i][j]
                if x > 0:
                    groups.setdefault(x, []).append((i, j))

        res = 0
        for x, cells in groups.items():
            # prefix sums of indicator (matrix > x)
            P = [[0] * (m + 1) for _ in range(n + 1)]
            for i in range(n):
                row = matrix[i]
                Pi, Pn = P[i], P[i + 1]
                run = 0
                for j in range(m):
                    if row[j] > x:
                        run += 1
                    Pn[j + 1] = Pi[j + 1] + run

            for r, c in cells:
                r1, r2 = max(0, r - x), min(n - 1, r + x)
                c1, c2 = max(0, c - x), min(m - 1, c + x)
                s = P[r2 + 1][c2 + 1] - P[r1][c2 + 1] - P[r2 + 1][c1] + P[r1][c1]
                if s:
                    for dr in (-x, x):
                        for dc in (-x, x):
                            rr, cc = r + dr, c + dc
                            if 0 <= rr < n and 0 <= cc < m and matrix[rr][cc] > x:
                                s -= 1
                if s == 0:
                    res += 1

        return res
