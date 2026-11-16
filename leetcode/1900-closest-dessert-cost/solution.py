from typing import List

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        best = baseCosts[0]

        def better(c: int) -> None:
            nonlocal best
            d, bd = abs(c - target), abs(best - target)
            if d < bd or (d == bd and c < best):
                best = c

        m = len(toppingCosts)

        def dfs(i: int, cost: int) -> None:
            better(cost)
            if i == m or cost >= target:
                return  # adding more only moves further above target
            dfs(i + 1, cost)
            dfs(i + 1, cost + toppingCosts[i])
            dfs(i + 1, cost + 2 * toppingCosts[i])

        for b in baseCosts:
            dfs(0, b)
        return best
