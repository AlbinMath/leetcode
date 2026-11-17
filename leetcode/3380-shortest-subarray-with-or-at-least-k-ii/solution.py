class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        cnt = [0] * 31
        cur = 0
        l = 0
        best = float('inf')
        for r, x in enumerate(nums):
            for b in range(31):
                if (x >> b) & 1:
                    cnt[b] += 1
                    cur |= 1 << b
            while l <= r and cur >= k:
                if r - l + 1 < best:
                    best = r - l + 1
                y = nums[l]
                for b in range(31):
                    if (y >> b) & 1:
                        cnt[b] -= 1
                        if cnt[b] == 0:
                            cur &= ~(1 << b)
                l += 1
        return -1 if best == float('inf') else best
