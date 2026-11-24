from bisect import bisect_left

class Solution:
    def maximizeTheProfit(self, n, offers):
        offers.sort(key=lambda o: o[1])
        ends = [-1]
        best = [0]
        for s, e, g in offers:
            idx = bisect_left(ends, s) - 1   # last end < s
            best.append(max(best[-1], best[idx] + g))
            ends.append(e)
        return best[-1]
