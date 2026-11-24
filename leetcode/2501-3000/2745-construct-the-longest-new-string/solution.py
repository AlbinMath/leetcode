class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x == y:
            return 2 * (x + y + z)
        return 2 * (2 * min(x, y) + 1 + z)
