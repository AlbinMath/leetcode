from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)

        def check(x: int) -> int:
            rot_top = rot_bottom = 0
            for t, b in zip(tops, bottoms):
                if t != x and b != x:
                    return -1
                if t != x:
                    rot_top += 1      # must rotate to bring x to the top
                elif b != x:
                    rot_bottom += 1   # must rotate to bring x to the bottom
            return min(rot_top, rot_bottom)

        r = check(tops[0])
        if r != -1:
            return r
        return check(bottoms[0])
