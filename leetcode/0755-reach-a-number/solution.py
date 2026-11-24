class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k, s = 0, 0

        while s < target or (s - target) % 2:
            k += 1
            s += k

        return k
