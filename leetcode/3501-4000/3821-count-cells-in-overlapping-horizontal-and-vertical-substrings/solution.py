from typing import List

class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        m, n = len(grid), len(grid[0])
        L = len(pattern)
        N = m * n
        if L > N:
            return 0

        def covered(text: str) -> List[bool]:
            s = pattern + '#' + text
            z = [0] * len(s)
            l = r = 0
            for i in range(1, len(s)):
                if i < r:
                    z[i] = min(r - i, z[i - l])
                while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] > r:
                    l, r = i, i + z[i]
            diff = [0] * (N + 1)
            for start in range(N - L + 1):
                if z[L + 1 + start] >= L:
                    diff[start] += 1
                    diff[start + L] -= 1
            res = [False] * N
            cur = 0
            for i in range(N):
                cur += diff[i]
                res[i] = cur > 0
            return res

        row_text = ''.join(''.join(row) for row in grid)
        col_text = ''.join(grid[i][j] for j in range(n) for i in range(m))

        h = covered(row_text)     # index i*n + j
        v = covered(col_text)     # index j*m + i

        count = 0
        for i in range(m):
            for j in range(n):
                if h[i * n + j] and v[j * m + i]:
                    count += 1
        return count
