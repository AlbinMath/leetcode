class Solution(object):
    def minXor(self, nums, k):
        n = len(nums)
        INF = float('inf')
        P = [0] * (n + 1)
        for i, v in enumerate(nums):
            P[i + 1] = P[i] ^ v

        prev = [INF] * (n + 1)
        prev[0] = 0
        for p in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(p, n + 1):
                best = INF
                pi = P[i]
                for j in range(p - 1, i):
                    d = prev[j]
                    if d == INF:
                        continue
                    x = pi ^ P[j]
                    if x < d:
                        x = d
                    if x < best:
                        best = x
                cur[i] = best
            prev = cur
        return prev[n]
