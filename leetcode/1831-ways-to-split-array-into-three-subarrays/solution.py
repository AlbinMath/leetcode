class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        total = pre[n]

        ans = 0
        lo = hi = 0
        for i in range(1, n - 1):                 # i = size of left
            L = pre[i]
            lo = max(lo, i + 1)
            while lo < n and pre[lo] < 2 * L:
                lo += 1
            hi = max(hi, lo)
            while hi < n and 2 * pre[hi] <= total + L:
                hi += 1
            ans += hi - lo                        # valid k in [lo, hi)
        return ans % MOD
