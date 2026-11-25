from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        base = 0
        for i in range(n - 1):
            if nums[i] != -1 and nums[i + 1] != -1:
                base = max(base, abs(nums[i] - nums[i + 1]))

        segs = []
        nb = []
        i = 0
        while i < n:
            if nums[i] == -1:
                j = i
                while j + 1 < n and nums[j + 1] == -1:
                    j += 1
                a = nums[i - 1] if i > 0 else None
                b = nums[j + 1] if j < n - 1 else None
                if a is not None:
                    nb.append(a)
                if b is not None:
                    nb.append(b)
                if a is not None or b is not None:
                    segs.append((a, b, j - i + 1))
                i = j + 1
            else:
                i += 1

        if not nb:
            return base
        mn, mx = min(nb), max(nb)

        def ok(d: int) -> bool:
            x, y = mn + d, mx - d
            vals = (x, y)
            for a, b, ln in segs:
                if a is None or b is None:
                    k = a if a is not None else b
                    if not any(abs(k - p) <= d for p in vals):
                        return False
                    continue
                good = False
                for p in vals:
                    if abs(a - p) > d:
                        continue
                    for q in vals:
                        if abs(b - q) > d:
                            continue
                        if p == q or (ln >= 2 and abs(x - y) <= d):
                            good = True
                            break
                    if good:
                        break
                if not good:
                    return False
            return True

        lo, hi = base, max(base, (mx - mn + 1) // 2)
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
