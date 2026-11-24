from bisect import bisect_right
from typing import List

class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        ans = 0
        for r in range(k):
            tails = []
            length = 0
            for i in range(r, len(arr), k):
                x = arr[i]
                pos = bisect_right(tails, x)
                if pos == len(tails):
                    tails.append(x)
                else:
                    tails[pos] = x
                length += 1
            ans += length - len(tails)
        return ans
