from typing import List

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        ans = float('inf')
        cur = set()

        for x in arr:
            cur = {v & x for v in cur}
            cur.add(x)
            for v in cur:
                ans = min(ans, abs(v - target))
            if ans == 0:
                return 0

        return ans
