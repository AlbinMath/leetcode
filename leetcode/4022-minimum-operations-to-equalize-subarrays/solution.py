
class Solution:
    def minOperations(self, nums, k, queries):
        n = len(nums)

        # Check remainder compatibility in O(1) per query.
        bad = [0] * n
        for i in range(1, n):
            bad[i] = bad[i - 1] + (
                nums[i] % k != nums[i - 1] % k
            )

        # Prefix sums: subarray sum in O(1).
        pref = [0] * (n + 1)
        for i, x in enumerate(nums):
            pref[i + 1] = pref[i] + x

        # Coordinate compression.
        vals = sorted(set(nums))
        rank = {x: i for i, x in enumerate(vals)}
        m = len(vals)

        # Persistent segment tree.
        left = [0]
        right = [0]
        cnt = [0]
        sm = [0]
        roots = [0]

        def insert(old, lo, hi, p, value):
            cur = len(cnt)
            left.append(left[old])
            right.append(right[old])
            cnt.append(cnt[old] + 1)
            sm.append(sm[old] + value)

            if lo < hi:
                mid = (lo + hi) // 2
                if p <= mid:
                    left[cur] = insert(
                        left[old], lo, mid, p, value
                    )
                else:
                    right[cur] = insert(
                        right[old], mid + 1, hi, p, value
                    )

            return cur

        for x in nums:
            roots.append(
                insert(roots[-1], 0, m - 1, rank[x], x)
            )

        def kth(a, b, lo, hi, target):
            if lo == hi:
                return vals[lo]

            mid = (lo + hi) // 2
            c = cnt[left[b]] - cnt[left[a]]

            if target <= c:
                return kth(left[a], left[b], lo, mid, target)

            return kth(
                right[a], right[b], mid + 1, hi, target - c
            )

        # Count and sum of values whose compressed index < limit.
        def query_less(a, b, lo, hi, limit):
            if hi < limit:
                return cnt[b] - cnt[a], sm[b] - sm[a]

            if lo >= limit:
                return 0, 0

            mid = (lo + hi) // 2

            c1, s1 = query_less(
                left[a], left[b], lo, mid, limit
            )
            c2, s2 = query_less(
                right[a], right[b], mid + 1, hi, limit
            )

            return c1 + c2, s1 + s2

        ans = []

        for l, r in queries:
            if bad[r] != bad[l]:
                ans.append(-1)
                continue

            length = r - l + 1
            a = roots[l]
            b = roots[r + 1]

            # Median of the queried subarray.
            median = kth(
                a, b, 0, m - 1, (length + 1) // 2
            )
            mid_idx = rank[median]

            # Values strictly smaller than the median.
            left_count, left_sum = query_less(
                a, b, 0, m - 1, mid_idx
            )

            # O(1) subarray sum.
            total_sum = pref[r + 1] - pref[l]

            right_count = length - left_count - 1
            right_sum = total_sum - left_sum - median

            # Total operations to make all values equal to median.
            cost = (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

            ans.append(cost // k)

        return ans

