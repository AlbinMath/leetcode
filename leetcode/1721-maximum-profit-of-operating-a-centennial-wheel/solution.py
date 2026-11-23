class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = boarded = rotations = 0
        best_profit = 0
        ans = -1
        n = len(customers)
        i = 0

        while i < n or waiting > 0:
            if i < n:
                waiting += customers[i]
                i += 1
            take = min(4, waiting)
            waiting -= take
            boarded += take
            rotations += 1
            profit = boarded * boardingCost - rotations * runningCost
            if profit > best_profit:
                best_profit = profit
                ans = rotations

        return ans
