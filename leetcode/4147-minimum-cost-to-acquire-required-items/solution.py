class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        m = min(need1, need2)
        M = max(need1, need2)

        option1 = need1 * cost1 + need2 * cost2
        option2 = m * costBoth + (need1 - m) * cost1 + (need2 - m) * cost2
        option3 = M * costBoth

        return min(option1, option2, option3)
