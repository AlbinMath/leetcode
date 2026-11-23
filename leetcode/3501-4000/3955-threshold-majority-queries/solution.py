class Solution:
    def subarrayMajority(self, nums, queries):
        n, q = len(nums), len(queries)
        vals = sorted(set(nums))
        rank = {v: i for i, v in enumerate(vals)}
        a = [rank[v] for v in nums]
        D = len(vals)
        K = D + 1

        S = max(1, int(n / (q ** 0.5)))
        order = sorted(range(q), key=lambda i: (queries[i][0] // S, queries[i][1]))

        cnt = [0] * D
        ans = [-1] * q
        cur_block = -1
        prev_end = 0
        R = 0
        best = 0

        for qi in order:
            l, r, t = queries[qi]
            b = l // S
            end = (b + 1) * S

            if b != cur_block:
                for i in range(prev_end, R):      # clear previous block's right part
                    cnt[a[i]] = 0
                cur_block = b
                prev_end = end
                R = end
                best = 0

            if r < end:
                # same block: brute force (cnt is all zero here)
                bst = 0
                for i in range(l, r + 1):
                    x = a[i]
                    c = cnt[x] + 1
                    cnt[x] = c
                    k = c * K + K - 1 - x
                    if k > bst:
                        bst = k
                for i in range(l, r + 1):
                    cnt[a[i]] = 0
            else:
                while R <= r:
                    x = a[R]
                    c = cnt[x] + 1
                    cnt[x] = c
                    k = c * K + K - 1 - x
                    if k > best:
                        best = k
                    R += 1
                save = best
                bst = best
                for i in range(l, end):
                    x = a[i]
                    c = cnt[x] + 1
                    cnt[x] = c
                    k = c * K + K - 1 - x
                    if k > bst:
                        bst = k
                for i in range(l, end):
                    cnt[a[i]] -= 1
                best = save

            if bst // K >= t:
                ans[qi] = vals[K - 1 - bst % K]
        return ans
