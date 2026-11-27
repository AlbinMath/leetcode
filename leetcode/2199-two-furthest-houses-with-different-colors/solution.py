from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        if colors[0] != colors[-1]:
            return n - 1
        i = 0
        while colors[i] == colors[-1]:
            i += 1          # leftmost house differing from the end color
        j = n - 1
        while colors[j] == colors[0]:
            j -= 1          # rightmost house differing from the start color
        return max(n - 1 - i, j)
