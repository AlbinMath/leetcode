class Solution(object):
    def minimumDifference(self, nums, k):
        best = float('inf')
        cur = set()
        for x in nums:
            cur = {v | x for v in cur}
            cur.add(x)
            for v in cur:
                d = abs(v - k)
                if d < best:
                    best = d
            if best == 0:
                return 0
        return best
