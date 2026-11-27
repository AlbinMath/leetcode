from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda c: c[0] - c[1])
        n = len(costs) // 2
        total = 0
        for i in range(n):
            total += costs[i][0]
        for i in range(n, 2 * n):
            total += costs[i][1]
        return total
