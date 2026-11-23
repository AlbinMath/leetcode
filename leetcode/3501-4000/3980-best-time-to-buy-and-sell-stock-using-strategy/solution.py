from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        P = [0] * (n + 1)   # prefix sums of prices
        S = [0] * (n + 1)   # prefix sums of strategy[i] * prices[i]
        for i in range(n):
            P[i + 1] = P[i] + prices[i]
            S[i + 1] = S[i] + strategy[i] * prices[i]

        h = k // 2
        best = 0
        for i in range(n - k + 1):
            new = P[i + k] - P[i + h]        # second half sells
            old = S[i + k] - S[i]            # original contribution of the window
            best = max(best, new - old)
        return S[n] + best
