class Solution(object):
    def minBitwiseArray(self, nums):
        res = []
        for x in nums:
            if x % 2 == 0:
                res.append(-1)
                continue
            low = (x + 1) & -(x + 1)      # 2^t, where t = number of trailing ones
            res.append(x ^ (low >> 1))    # clear bit t-1
        return res
