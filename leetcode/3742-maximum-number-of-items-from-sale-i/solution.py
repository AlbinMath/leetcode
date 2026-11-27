from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        g = [0] * n
        for i in range(n):
            fi = items[i][0]
            cnt = 0
            for j in range(n):
                if j != i and items[j][0] % fi == 0:
                    cnt += 1
            g[i] = cnt

        order = sorted(range(n), key=lambda i: -items[i][1])
        dp = [0] * (budget + 1)  # best value with total cost <= c, using items processed so far
        ans = 0

        for m in order:
            p = items[m][1]
            if p > budget:
                continue
            val = 1 + g[m]
            for c in range(budget - p + 1):
                cand = dp[c] + val + (budget - c - p) // p
                if cand > ans:
                    ans = cand
            for c in range(budget, p - 1, -1):
                v = dp[c - p] + val
                if v > dp[c]:
                    dp[c] = v
        return ans
