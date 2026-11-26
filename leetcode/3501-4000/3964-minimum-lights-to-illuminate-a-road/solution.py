from typing import List

class Solution:
    def minLights(self, lights: List[int]) -> int:
        n = len(lights)
        diff = [0] * (n + 1)
        for i, v in enumerate(lights):
            if v > 0:
                diff[max(0, i - v)] += 1
                diff[min(n - 1, i + v) + 1] -= 1

        covered = [False] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            covered[i] = cur > 0

        res = 0
        i = 0
        while i < n:
            if covered[i]:
                i += 1
            else:
                res += 1
                i += 3
        return res
