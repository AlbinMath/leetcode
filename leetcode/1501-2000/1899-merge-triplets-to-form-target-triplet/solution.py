from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        got = [False, False, False]
        for a, b, c in triplets:
            if a <= x and b <= y and c <= z:
                if a == x:
                    got[0] = True
                if b == y:
                    got[1] = True
                if c == z:
                    got[2] = True
        return all(got)
