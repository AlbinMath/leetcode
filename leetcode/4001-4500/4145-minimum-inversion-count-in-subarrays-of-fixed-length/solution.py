from typing import List

class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)
        tree = [0] * (m + 1)

        def update(i, d):
            while i <= m:
                tree[i] += d
                i += i & -i

        def query(i):  # number of stored values with rank <= i
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & -i
            return s

        a = [rank[x] for x in nums]

        inv = 0
        size = 0
        for i in range(k):
            inv += size - query(a[i])   # elements already present that are larger
            update(a[i], 1)
            size += 1
        best = inv

        for r in range(k, n):
            l = r - k
            # remove nums[l]: it is leftmost, inverted with smaller elements to its right
            update(a[l], -1)
            size -= 1
            inv -= query(a[l] - 1)
            # add nums[r]: it is rightmost, inverted with larger elements to its left
            inv += size - query(a[r])
            update(a[r], 1)
            size += 1
            best = min(best, inv)
        return best
