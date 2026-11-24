from functools import lru_cache

class Solution:
    def maxValue(self, events, k):
        events.sort()
        n = len(events)
        starts = [e[0] for e in events]

        @lru_cache(None)
        def f(i, j):
            if i == n or j == 0:
                return 0
            nxt = bisect_right(starts, events[i][1])
            return max(f(i + 1, j), events[i][2] + f(nxt, j - 1))

        return f(0, k)
