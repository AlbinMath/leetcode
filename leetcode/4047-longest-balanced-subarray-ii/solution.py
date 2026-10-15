class Solution:
    def longestBalanced(self, nums):
        n = len(nums)
        mn = [0] * (4 * n)
        mx = [0] * (4 * n)
        ad = [0] * (4 * n)

        def update(node, l, r, ql, qr, v):
            if ql <= l and r <= qr:
                mn[node] += v
                mx[node] += v
                ad[node] += v
                return
            mid = (l + r) // 2
            if ql <= mid:
                update(2 * node, l, mid, ql, qr, v)
            if qr > mid:
                update(2 * node + 1, mid + 1, r, ql, qr, v)
            a, b = 2 * node, 2 * node + 1
            mn[node] = min(mn[a], mn[b]) + ad[node]
            mx[node] = max(mx[a], mx[b]) + ad[node]

        def find(node, l, r, qr, acc):
            if l > qr:
                return -1
            if mn[node] + acc > 0 or mx[node] + acc < 0:
                return -1
            if l == r:
                return l
            mid = (l + r) // 2
            acc += ad[node]
            res = find(2 * node, l, mid, qr, acc)
            if res != -1:
                return res
            return find(2 * node + 1, mid + 1, r, qr, acc)

        last = {}
        ans = 0
        for r, v in enumerate(nums):
            p = last.get(v, -1)
            update(1, 0, n - 1, p + 1, r, 1 if v % 2 == 0 else -1)
            last[v] = r
            l = find(1, 0, n - 1, r, 0)
            if l != -1:
                ans = max(ans, r - l + 1)
        return ans
