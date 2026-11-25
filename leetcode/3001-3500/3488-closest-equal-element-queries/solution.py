from collections import defaultdict
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)

        ans = [-1] * n
        for lst in pos.values():
            m = len(lst)
            if m == 1:
                continue
            for k, i in enumerate(lst):
                best = n
                for j in (lst[k - 1], lst[(k + 1) % m]):
                    d = abs(i - j)
                    best = min(best, d, n - d)
                ans[i] = best

        return [ans[q] for q in queries]
