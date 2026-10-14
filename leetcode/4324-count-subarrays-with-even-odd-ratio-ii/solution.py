
class Solution:
    def countRatioSubarrays(self, nums, a, b):
        n = len(nums)
        pref = [0] * (n + 1)

        for i, x in enumerate(nums):
            pref[i + 1] = pref[i] + (b if x % 2 == 0 else -a)

        # Coordinate compression
        vals = sorted(set(pref))
        rank = {x: i + 1 for i, x in enumerate(vals)}
        m = len(vals)
        bit = [0] * (m + 1)

        def add(i, v=1):
            while i <= m:
                bit[i] += v
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        # Count valid pairs with at least one odd.
        ans = 0
        odd = [0] * (n + 1)
        for i, x in enumerate(nums):
            odd[i + 1] = odd[i] + (x % 2)

        # For each right endpoint, insert eligible left prefixes.
        left = 0
        for right in range(1, n + 1):
            while left < right and odd[left] < odd[right]:
                add(rank[pref[left]])
                left += 1

            idx = rank[pref[right]]
            ans += query(m) - query(idx - 1)

        return ans

