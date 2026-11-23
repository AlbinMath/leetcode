from typing import List

class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nums = sorted(nums)
        full = (1 << n) - 1

        pw = [pow(10, len(str(x)), k) for x in nums]
        val = [x % k for x in nums]

        can = [[False] * k for _ in range(1 << n)]
        can[full][0] = True

        for mask in range(full - 1, -1, -1):
            row = can[mask]
            for r in range(k):
                for j in range(n):
                    if mask >> j & 1:
                        continue
                    nr = (r * pw[j] + val[j]) % k
                    if can[mask | (1 << j)][nr]:
                        row[r] = True
                        break

        if not can[0][0]:
            return []

        res = []
        mask, r = 0, 0
        for _ in range(n):
            for j in range(n):  # nums is sorted, so the first hit is the smallest
                if mask >> j & 1:
                    continue
                nr = (r * pw[j] + val[j]) % k
                if can[mask | (1 << j)][nr]:
                    res.append(nums[j])
                    mask |= 1 << j
                    r = nr
                    break
        return res
