class Solution(object):
    def maximumAND(self, nums, k, m):
        ans = 0
        for b in range(31, -1, -1):
            c = ans | (1 << b)
            costs = []
            for x in nums:
                d = c & ~x
                if d == 0:
                    costs.append(0)
                else:
                    h = d.bit_length() - 1
                    y = ((x >> (h + 1)) << (h + 1)) | (1 << h) | (c & ((1 << h) - 1))
                    costs.append(y - x)
            costs.sort()
            if sum(costs[:m]) <= k:
                ans = c
        return ans
