class Solution(object):
    def reorderedPowerOf2(self, n):
        target = sorted(str(n))
        return any(sorted(str(1 << i)) == target for i in range(30))
