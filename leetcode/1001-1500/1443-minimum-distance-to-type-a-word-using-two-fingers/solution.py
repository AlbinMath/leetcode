class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a: int, b: int) -> int:
            if a == 26 or b == 26:
                return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        INF = float('inf')
        # dp[o]: min cost, last-typed finger on previous letter, other finger on o (26 = unplaced)
        dp = [INF] * 27
        dp[26] = 0
        prev = ord(word[0]) - 65

        for ch in word[1:]:
            cur = ord(ch) - 65
            ndp = [INF] * 27
            for o in range(27):
                if dp[o] == INF:
                    continue
                # same finger moves prev -> cur
                ndp[o] = min(ndp[o], dp[o] + dist(prev, cur))
                # other finger moves o -> cur; the finger on prev becomes "other"
                ndp[prev] = min(ndp[prev], dp[o] + dist(o, cur))
            dp = ndp
            prev = cur

        return min(dp)
