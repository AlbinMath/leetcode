
class Solution:
    def distantSubarrays(self, nums, goal, k):
        n = len(nums)
        total = n * (n + 1) // 2

        if k == 0:
            return total

        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        # A subarray is NOT distant if:
        # goal - k < sum < goal + k
        low = goal - k + 1
        high = goal + k - 1

        from bisect import bisect_left, bisect_right

        values = sorted(set(prefix))
        m = len(values)
        rank = {v: i + 1 for i, v in enumerate(values)}
        bit = [0] * (m + 1)

        def add(i):
            while i <= m:
                bit[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        close = 0

        for p in prefix:
            # Previous prefix q satisfying:
            # low <= p - q <= high
            left = p - high
            right = p - low

            l = bisect_left(values, left) + 1
            r = bisect_right(values, right)

            close += query(r) - query(l - 1)
            add(rank[p])

        return total - close

