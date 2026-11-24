class Solution:
    def makeStringGood(self, s: str) -> int:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        INF = float('inf')
        best = INF

        for f in range(1, n + 1):
            dp = [0, INF]
            prev_surplus = [0, 0]  # before the first letter nothing is carried

            for c in cnt:
                new_dp = [INF, INF]
                new_surplus = [c, max(0, c - f)]
                for t in (0, 1):
                    for pt in (0, 1):
                        if dp[pt] == INF:
                            continue
                        x = prev_surplus[pt]
                        if t == 0:
                            cost = c  # all c characters are deleted or moved on
                        else:
                            cost = max(0, c - f)  # surplus
                            if c < f:
                                cost += max(0, f - c - x)  # insertions
                        v = dp[pt] + cost
                        if v < new_dp[t]:
                            new_dp[t] = v
                dp = new_dp
                prev_surplus = new_surplus
            best = min(best, dp[0], dp[1])

        return best
