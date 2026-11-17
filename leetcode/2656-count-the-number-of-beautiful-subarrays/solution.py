class Solution(object):
    def beautifulSubarrays(self, nums):
        cnt = {0: 1}
        x = 0
        ans = 0
        for v in nums:
            x ^= v
            c = cnt.get(x, 0)
            ans += c
            cnt[x] = c + 1
        return ans
