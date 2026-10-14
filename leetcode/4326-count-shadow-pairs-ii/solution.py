
from bisect import bisect_left

class Solution(object):
    def shadowPairs(self, nums):
        n = len(nums)
        INF = 10**18
        order = sorted(range(n), key=lambda i: (nums[i], i))
        pos = [0] * n

        for r, i in enumerate(order):
            pos[i] = r

        sorted_vals = [nums[i] for i in order]

        size = 4 * n
        mx = [-1] * size
        se = [-2] * size
        cnt = [0] * size

        def pull(o):
            a, b = 2 * o, 2 * o + 1

            if mx[a] > mx[b]:
                mx[o], cnt[o] = mx[a], cnt[a]
                se[o] = max(se[a], mx[b])
            elif mx[a] < mx[b]:
                mx[o], cnt[o] = mx[b], cnt[b]
                se[o] = max(se[b], mx[a])
            else:
                mx[o], cnt[o] = mx[a], cnt[a] + cnt[b]
                se[o] = max(se[a], se[b])

        def push(o):
            m = mx[o]
            for c in (2 * o, 2 * o + 1):
                if mx[c] > m:
                    mx[c] = m

        def insert(o, l, r, p):
            if l == r:
                mx[o] = INF
                se[o] = -2
                cnt[o] = 1
                return

            push(o)
            m = (l + r) >> 1

            if p <= m:
                insert(2 * o, l, m, p)
            else:
                insert(2 * o + 1, m + 1, r, p)

            pull(o)

        def update(o, l, r, qr, v):
            if l > qr or mx[o] < v:
                return 0

            if r <= qr and se[o] < v:
                res = cnt[o]
                if mx[o] > v:
                    mx[o] = v
                return res

            push(o)
            m = (l + r) >> 1

            res = update(2 * o, l, m, qr, v)
            res += update(2 * o + 1, m + 1, r, qr, v)

            pull(o)
            return res

        ans = 0

        for j in range(n):
            v = nums[j]
            k = bisect_left(sorted_vals, v)

            if k > 0:
                ans += update(1, 0, n - 1, k - 1, v)

            insert(1, 0, n - 1, pos[j])

        return ans

