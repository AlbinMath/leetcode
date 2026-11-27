from typing import List

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int],
                rowCosts: List[int], colCosts: List[int]) -> int:
        sr, sc = startPos
        hr, hc = homePos
        total = 0
        if hr > sr:
            total += sum(rowCosts[sr + 1:hr + 1])
        elif hr < sr:
            total += sum(rowCosts[hr:sr])
        if hc > sc:
            total += sum(colCosts[sc + 1:hc + 1])
        elif hc < sc:
            total += sum(colCosts[hc:sc])
        return total
