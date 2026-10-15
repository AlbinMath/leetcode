class Solution:
    def countOfPeaks(self, nums, queries):
        n = len(nums)
        size = 1
        while size < n:
            size *= 2

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a
            return (a[0], b[1], a[2] + b[2] + (b[0] - a[1]) * b[0])

        def leaf(i):
            if 1 <= i <= n - 2 and nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return (i, i, 0)
            return None

        tree = [None] * (2 * size)
        for i in range(n):
            tree[size + i] = leaf(i)
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def refresh(i):
            if i < 0 or i >= n:
                return
            pos = size + i
            tree[pos] = leaf(i)
            pos >>= 1
            while pos:
                tree[pos] = merge(tree[2 * pos], tree[2 * pos + 1])
                pos >>= 1

        def query(lo, hi):
            lo += size
            hi += size + 1
            left = right = None
            while lo < hi:
                if lo & 1:
                    left = merge(left, tree[lo])
                    lo += 1
                if hi & 1:
                    hi -= 1
                    right = merge(tree[hi], right)
                lo >>= 1
                hi >>= 1
            return merge(left, right)

        ans = []
        for q in queries:
            if q[0] == 1:
                l, r = q[1], q[2]
                res = query(l + 1, r - 1) if r - l >= 2 else None
                if res is None:
                    ans.append(0)
                else:
                    first, last, B = res
                    ans.append((first - l) * (r - first) + r * (last - first) - B)
            else:
                idx, val = q[1], q[2]
                nums[idx] = val
                refresh(idx - 1)
                refresh(idx)
                refresh(idx + 1)
        return ans
