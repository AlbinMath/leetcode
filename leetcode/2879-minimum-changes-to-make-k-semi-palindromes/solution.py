class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)
        INF = float('inf')

        # divisors[L] = proper divisors of L (d < L)
        divisors = [[] for _ in range(n + 1)]
        for L in range(2, n + 1):
            for d in range(1, L):
                if L % d == 0:
                    divisors[L].append(d)

        # cost[i][j]: min changes to make s[i..j] a semi-palindrome
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                best = INF
                for d in divisors[L]:
                    cnt = 0
                    m = L // d  # size of each group
                    for r in range(d):
                        lo = i + r
                        hi = lo + (m - 1) * d
                        while lo < hi:
                            if s[lo] != s[hi]:
                                cnt += 1
                            lo += d
                            hi -= d
                    if cnt < best:
                        best = cnt
                cost[i][j] = best

        # dp[p][j]: min cost to split first j chars into p parts
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for j in range(2 * p, n + 1):
                best = INF
                for i in range(2 * (p - 1), j - 1):  # last part s[i..j-1] has length >= 2
                    if dp[p - 1][i] != INF and cost[i][j - 1] != INF:
                        v = dp[p - 1][i] + cost[i][j - 1]
                        if v < best:
                            best = v
                dp[p][j] = best

        return dp[k][n]
