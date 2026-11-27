from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda p: p[1])
        cur_end = float('-inf')
        count = 0
        for left, right in pairs:
            if left > cur_end:
                count += 1
                cur_end = right
        return count
