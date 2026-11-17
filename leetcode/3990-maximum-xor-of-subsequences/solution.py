class Solution(object):
    def maxXorSubsequences(self, nums):
        basis = [0] * 30
        for x in nums:
            for b in range(29, -1, -1):
                if not (x >> b) & 1:
                    continue
                if basis[b] == 0:
                    basis[b] = x
                    break
                x ^= basis[b]

        res = 0
        for b in range(29, -1, -1):
            if basis[b] and (res ^ basis[b]) > res:
                res ^= basis[b]
        return res
