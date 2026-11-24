from typing import List

class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        full = (1 << n) - 1
        INF = float('inf')

        f = [[INF] * n for _ in range(1 << n)]
        for last in range(n):
            f[full][last] = abs(last - nums[0])

        for mask in range(full - 1, 0, -1):
            if not mask & 1:
                continue  # every state contains node 0
            for last in range(n):
                if not mask >> last & 1:
                    continue
                best = INF
                for j in range(n):
                    if mask >> j & 1:
                        continue
                    v = abs(last - nums[j]) + f[mask | (1 << j)][j]
                    if v < best:
                        best = v
                f[mask][last] = best

        res = [0]
        mask, last = 1, 0
        while mask != full:
            target = f[mask][last]
            for j in range(n):
                if mask >> j & 1:
                    continue
                if abs(last - nums[j]) + f[mask | (1 << j)][j] == target:
                    res.append(j)
                    mask |= 1 << j
                    last = j
                    break
        return res
