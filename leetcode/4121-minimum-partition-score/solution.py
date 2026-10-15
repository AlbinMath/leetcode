class Solution:
    def minPartitionScore(self, nums, k):
        n = len(nums)
        P = [0] * (n + 1)
        for i, v in enumerate(nums):
            P[i + 1] = P[i] + v

        INF = float('inf')
        prev = [INF] * (n + 1)
        prev[0] = 0

        for t in range(1, k + 1):
            cur = [INF] * (n + 1)

            # cur[i] needs i >= t, and j in [t-1, i-1]
            def compute(lo, hi, optlo, opthi):
                if lo > hi:
                    return
                mid = (lo + hi) // 2
                best = INF
                bj = optlo
                top = min(mid - 1, opthi)
                for j in range(optlo, top + 1):
                    if prev[j] == INF:
                        continue
                    d = P[mid] - P[j]
                    val = prev[j] + d * (d + 1) // 2
                    if val < best:
                        best = val
                        bj = j
                cur[mid] = best
                compute(lo, mid - 1, optlo, bj)
                compute(mid + 1, hi, bj, opthi)

            compute(t, n, t - 1, n - 1)
            prev = cur

        return prev[n]
