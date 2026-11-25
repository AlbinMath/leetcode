class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [0] * (n + 1)

        for i, v in enumerate(nums):
            lo = (i + 1) % n
            hi = (i - v) % n
            if lo <= hi:
                diff[lo] += 1
                diff[hi + 1] -= 1
            else:  # range wraps around
                diff[lo] += 1
                diff[n] -= 1
                diff[0] += 1
                diff[hi + 1] -= 1

        best_k, best, cur = 0, -1, 0
        for k in range(n):
            cur += diff[k]
            if cur > best:
                best, best_k = cur, k
        return best_k
