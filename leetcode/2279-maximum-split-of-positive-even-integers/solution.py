from typing import List

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        res = []
        x = 2
        while finalSum >= x:
            res.append(x)
            finalSum -= x
            x += 2
        res[-1] += finalSum  # leftover (0 or an even number smaller than x)
        return res
