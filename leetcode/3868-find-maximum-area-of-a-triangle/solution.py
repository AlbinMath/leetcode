from typing import List

class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        def solve(pts):
            lo, hi = {}, {}
            for x, y in pts:
                if x not in lo:
                    lo[x] = hi[x] = y
                else:
                    if y < lo[x]: lo[x] = y
                    if y > hi[x]: hi[x] = y
            min_x, max_x = min(lo), max(lo)
            best = 0
            for x in lo:
                base = hi[x] - lo[x]
                height = max(x - min_x, max_x - x)
                best = max(best, base * height)
            return best

        ans = max(solve(coords), solve([[y, x] for x, y in coords]))
        return ans if ans > 0 else -1
