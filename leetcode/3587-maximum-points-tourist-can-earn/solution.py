class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [0] * n

        for day in range(k):
            new = [0] * n
            for c in range(n):
                best = dp[c] + stayScore[day][c]
                for p in range(n):
                    if p != c:
                        best = max(best, dp[p] + travelScore[p][c])
                new[c] = best
            dp = new

        return max(dp)
