from typing import List
from itertools import permutations

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        res = []
        for top, left, right, bottom in permutations(words, 4):
            if (top[0] == left[0] and top[3] == right[0]
                    and bottom[0] == left[3] and bottom[3] == right[3]):
                res.append([top, left, right, bottom])
        res.sort()
        return res
