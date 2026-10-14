
class Solution:
    def popcountDepth(self, nums, queries):
        n = len(nums)
        bit = [[0] * (n + 1) for _ in range(6)]

        def depth(x):
            d = 0
            while x > 1:
                x = bin(x).count('1')
                d += 1
            return d

        def update(k, i, delta):
            i += 1
            while i <= n:
                bit[k][i] += delta
                i += i & -i

        def prefix(k, i):
            if i < 0:
                return 0
            i += 1
            res = 0
            while i > 0:
                res += bit[k][i]
                i -= i & -i
            return res

        depths = [depth(x) for x in nums]

        for i, d in enumerate(depths):
            update(d, i, 1)

        ans = []

        for q in queries:
            if q[0] == 1:
                _, l, r, k = q
                ans.append(prefix(k, r) - prefix(k, l - 1))
            else:
                _, idx, val = q
                old = depths[idx]
                new = depth(val)

                if old != new:
                    update(old, idx, -1)
                    update(new, idx, 1)
                    depths[idx] = new

                nums[idx] = val

        return ans

