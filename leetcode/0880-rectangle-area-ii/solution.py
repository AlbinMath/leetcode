from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7
        xs = sorted({r[0] for r in rectangles} | {r[2] for r in rectangles})
        ans = 0
        for i in range(len(xs) - 1):
            x1, x2 = xs[i], xs[i + 1]
            ys = sorted((r[1], r[3]) for r in rectangles
                        if r[0] <= x1 and r[2] >= x2)
            covered = 0
            cur_lo = cur_hi = -1
            for lo, hi in ys:
                if lo > cur_hi:
                    covered += cur_hi - cur_lo
                    cur_lo, cur_hi = lo, hi
                else:
                    cur_hi = max(cur_hi, hi)
            covered += cur_hi - cur_lo
            ans += covered * (x2 - x1)
        return ans % MOD
