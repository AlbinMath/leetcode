class Solution(object):
    def maxValue(self, nums, k):
        n = len(nums)

        def build(arr):
            # res[i] = set of ORs from choosing exactly k of the first i elements
            dp = [set() for _ in range(k + 1)]
            dp[0].add(0)
            res = [frozenset()] * (len(arr) + 1)
            for i, x in enumerate(arr):
                for j in range(min(k, i + 1), 0, -1):
                    if dp[j - 1]:
                        dp[j] |= {v | x for v in dp[j - 1]}
                res[i + 1] = frozenset(dp[k])
            return res

        pre = build(nums)
        suf = build(nums[::-1])  # suf[m] = ORs from choosing k of the last m elements

        best = 0
        for i in range(k, n - k + 1):
            A = pre[i]
            B = suf[n - i]
            for a in A:
                for b in B:
                    v = a ^ b
                    if v > best:
                        best = v
        return best
