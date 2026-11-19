from typing import List

class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        def solve(segs):
            segs.sort()
            n = len(segs)
            P = [0] * (n + 1)
            for i, (l, r, c) in enumerate(segs):
                P[i + 1] = P[i] + (r - l + 1) * c
            best = 0
            j = 0
            for i in range(n):
                s = segs[i][0]
                e = s + k - 1
                if j < i:
                    j = i
                while j < n and segs[j][1] <= e:
                    j += 1
                total = P[j] - P[i]
                if j < n and segs[j][0] <= e:
                    total += (e - segs[j][0] + 1) * segs[j][2]
                best = max(best, total)
            return best

        a = solve([[l, r, c] for l, r, c in coins])
        b = solve([[-r, -l, c] for l, r, c in coins])
        return max(a, b)
