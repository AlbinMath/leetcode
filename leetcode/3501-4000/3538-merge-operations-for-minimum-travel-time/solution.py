from typing import List

class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        INF = float('inf')
        T = [0] * (n + 1)
        for i in range(n):
            T[i + 1] = T[i] + time[i]
        dp = [[[INF] * (k + 1) for _ in range(n)] for _ in range(n)]
        for j in range(1, n):
            removed = j - 1
            if removed > k:
                break
            dp[j][0][removed] = (position[j] - position[0]) * time[0]

        best = INF
        for j in range(1, n):
            for p in range(j):
                for c in range(k + 1):
                    cur = dp[j][p][c]
                    if cur == INF:
                        continue
                    mt = T[j + 1] - T[p + 1]  # merged time of j
                    if j == n - 1:
                        if c == k:
                            best = min(best, cur)
                        continue
                    for nxt in range(j + 1, n):
                        c2 = c + (nxt - j - 1)
                        if c2 > k:
                            break
                        v = cur + (position[nxt] - position[j]) * mt
                        if v < dp[nxt][j][c2]:
                            dp[nxt][j][c2] = v
        return best
