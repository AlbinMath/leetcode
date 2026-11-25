class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        # child 1: main diagonal
        total = sum(fruits[i][i] for i in range(n))

        def solve(g):
            NEG = float('-inf')
            prev = [NEG] * n
            prev[n - 1] = g[0][n - 1]
            for i in range(1, n - 1):
                cur = [NEG] * n
                for j in range(i + 1, n):
                    best = prev[j]
                    if j > 0 and prev[j - 1] > best:
                        best = prev[j - 1]
                    if j + 1 < n and prev[j + 1] > best:
                        best = prev[j + 1]
                    if best > NEG:
                        cur[j] = best + g[i][j]
                prev = cur
            return prev[n - 1]

        # child 2: upper-right triangle, stops at (n-2, n-1)
        total += solve(fruits)

        # child 3: transpose and reuse
        t = [list(r) for r in zip(*fruits)]
        total += solve(t)

        return total
