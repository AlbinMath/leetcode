from itertools import chain
from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        banned = {f for f, b in zip(fronts, backs) if f == b}
        return min((x for x in chain(fronts, backs) if x not in banned), default=0)
