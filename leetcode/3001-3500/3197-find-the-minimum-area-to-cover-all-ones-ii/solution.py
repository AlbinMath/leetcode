from typing import List

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def area(r1, r2, c1, c2):
            # bounding box of 1s in rows [r1, r2), cols [c1, c2)
            top, bot, left, right = m, -1, n, -1
            for r in range(r1, r2):
                for c in range(c1, c2):
                    if grid[r][c]:
                        if r < top: top = r
                        if r > bot: bot = r
                        if c < left: left = c
                        if c > right: right = c
            if bot == -1:
                return 0
            return (bot - top + 1) * (right - left + 1)

        ans = m * n

        # three vertical strips
        for a in range(1, n):
            for b in range(a + 1, n):
                ans = min(ans, area(0, m, 0, a) + area(0, m, a, b) + area(0, m, b, n))

        # three horizontal strips
        for a in range(1, m):
            for b in range(a + 1, m):
                ans = min(ans, area(0, a, 0, n) + area(a, b, 0, n) + area(b, m, 0, n))

        # vertical cut, then split one side horizontally
        for c in range(1, n):
            for r in range(1, m):
                # left split horizontally, right whole
                ans = min(ans, area(0, r, 0, c) + area(r, m, 0, c) + area(0, m, c, n))
                # right split horizontally, left whole
                ans = min(ans, area(0, m, 0, c) + area(0, r, c, n) + area(r, m, c, n))

        # horizontal cut, then split one side vertically
        for r in range(1, m):
            for c in range(1, n):
                # top split vertically, bottom whole
                ans = min(ans, area(0, r, 0, c) + area(0, r, c, n) + area(r, m, 0, n))
                # bottom split vertically, top whole
                ans = min(ans, area(0, r, 0, n) + area(r, m, 0, c) + area(r, m, c, n))

        return ans
