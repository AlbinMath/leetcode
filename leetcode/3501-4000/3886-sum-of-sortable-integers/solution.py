
from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k:
                continue

            arr = []
            for i in range(0, n, k):
                a = nums[i:i + k]
                a.sort()
                arr.append(a)

            # Check if each block can be rotated into sorted order
            ok = True
            for i in range(0, n, k):
                a = nums[i:i + k]
                if sum(a[j] > a[(j + 1) % k] for j in range(k)) > 1:
                    ok = False
                    break

            if not ok:
                continue

            # Check whether sorted rotations can make the full array sorted
            for i in range(0, n, k):
                a = nums[i:i + k]
                if i > 0 and max(nums[i-k:i]) > min(a):
                    ok = False
                    break

            if ok:
                ans += k

        return ans

