class Solution(object):
    def smallestSubarrays(self, nums):
        n = len(nums)
        last = [-1] * 31
        res = [1] * n
        for i in range(n - 1, -1, -1):
            x = nums[i]
            far = i
            for b in range(31):
                if (x >> b) & 1:
                    last[b] = i
                if last[b] != -1 and last[b] > far:
                    far = last[b]
            res[i] = far - i + 1
        return res
