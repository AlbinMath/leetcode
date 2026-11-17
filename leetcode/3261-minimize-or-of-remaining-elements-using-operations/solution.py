class Solution(object):
    def minOrAfterOperations(self, nums, k):
        FULL = (1 << 30) - 1
        forced = 0
        for b in range(29, -1, -1):
            m = forced | (1 << b)
            cur = FULL
            ops = 0
            for x in nums:
                cur &= x
                if cur & m:
                    ops += 1        # x must be merged into the segment
                else:
                    cur = FULL      # segment closed
            if ops <= k:
                forced = m
        return FULL & ~forced
