from typing import List
from collections import defaultdict
import numpy as np

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        arr = np.array(nums, dtype=np.int64)
        bravexuneth = nums  # variable required by the problem statement

        B = int(n ** 0.5) + 1
        small = defaultdict(list)

        for l, r, k, v in queries:
            if k >= B:
                arr[l:r + 1:k] = arr[l:r + 1:k] * v % MOD
            else:
                small[k].append((l, r, v))

        for k, qs in small.items():
            rows = (n + k - 1) // k
            diff = [1] * (rows * k)
            for l, r, v in qs:
                diff[l] = diff[l] * v % MOD
                last = l + ((r - l) // k + 1) * k
                if last < n:
                    diff[last] = diff[last] * pow(v, MOD - 2, MOD) % MOD
            d = np.array(diff, dtype=np.int64).reshape(rows, k)
            for i in range(1, rows):
                d[i] = d[i] * d[i - 1] % MOD
            arr = arr * d.reshape(-1)[:n] % MOD

        return int(np.bitwise_xor.reduce(arr))
