from typing import List

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        n = len(locations)
        dp = [[0] * (fuel + 1) for _ in range(n)]
        dp[start][fuel] = 1

        for f in range(fuel, 0, -1):
            for c in range(n):
                ways = dp[c][f]
                if not ways:
                    continue
                for j in range(n):
                    if j == c:
                        continue
                    cost = abs(locations[c] - locations[j])
                    if cost <= f:
                        dp[j][f - cost] = (dp[j][f - cost] + ways) % MOD

        return sum(dp[finish]) % MOD
