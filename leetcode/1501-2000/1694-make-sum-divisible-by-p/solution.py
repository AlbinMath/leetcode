class Solution:
    def minSubarray(self, nums, p):
        r = sum(nums) % p
        if r == 0:
            return 0
        d, s, ans = {0: -1}, 0, len(nums)
        for i, x in enumerate(nums):
            s = (s + x) % p
            d[s] = i
            j = d.get((s - r) % p)
            if j is not None:
                ans = min(ans, i - j)
        return ans if ans < len(nums) else -1
