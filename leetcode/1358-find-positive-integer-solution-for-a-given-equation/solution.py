
from typing import List

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        x, y = 1, 1000
        while x <= 1000 and y >= 1:
            v = customfunction.f(x, y)
            if v < z:
                x += 1
            elif v > z:
                y -= 1
            else:
                res.append([x, y])
                x += 1
                y -= 1
        return res
