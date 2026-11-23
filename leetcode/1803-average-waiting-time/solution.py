class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = 0
        total = 0
        for a, d in customers:
            t = max(t, a) + d
            total += t - a
        return total / len(customers)
