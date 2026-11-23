class Solution(object):
    def minMergeCost(self, lists):
        n = len(lists)
        full = 1 << n
        ln = [0] * full
        med = [0] * full

        for mask in range(1, full):
            merged = []
            for i in range(n):
                if (mask >> i) & 1:
                    merged.extend(lists[i])
            merged.sort()
            ln[mask] = len(merged)
            med[mask] = merged[(len(merged) - 1) // 2]

        INF = float('inf')
        dp = [INF] * full
        for i in range(n):
            dp[1 << i] = 0

        for mask in range(1, full):
            if mask & (mask - 1) == 0:
                continue
            low = mask & -mask
            rest = mask ^ low
            best = INF
            sub = rest
            while True:
                a = sub | low          # part containing the lowest bit
                b = mask ^ a
                if b:
                    c = dp[a] + dp[b] + ln[mask] + abs(med[a] - med[b])
                    if c < best:
                        best = c
                if sub == 0:
                    break
                sub = (sub - 1) & rest
            dp[mask] = best

        return dp[full - 1]
