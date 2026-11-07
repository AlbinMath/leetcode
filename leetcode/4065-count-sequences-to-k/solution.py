from typing import List
from collections import defaultdict

class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        vec = {1: (0, 0, 0), 2: (1, 0, 0), 3: (0, 1, 0),
               4: (2, 0, 0), 5: (0, 0, 1), 6: (1, 1, 0)}

        t = [0, 0, 0]
        for idx, p in enumerate((2, 3, 5)):
            while k % p == 0:
                k //= p
                t[idx] += 1
        if k != 1:
            return 0
        target = tuple(t)

        dp = {(0, 0, 0): 1}
        for v in nums:
            a, b, c = vec[v]
            nd = defaultdict(int)
            for (x, y, z), cnt in dp.items():
                nd[(x, y, z)] += cnt
                nd[(x + a, y + b, z + c)] += cnt
                nd[(x - a, y - b, z - c)] += cnt
            dp = nd
        return dp.get(target, 0)
