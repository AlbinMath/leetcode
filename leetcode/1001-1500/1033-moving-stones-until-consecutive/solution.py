from typing import List

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x, y, z = sorted((a, b, c))
        if z - x == 2:
            return [0, 0]
        mn = 1 if (y - x <= 2 or z - y <= 2) else 2
        return [mn, z - x - 2]
