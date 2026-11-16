from typing import List
from functools import lru_cache
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        tops = defaultdict(list)
        for p in allowed:
            tops[p[:2]].append(p[2])

        @lru_cache(maxsize=None)
        def can(row: str) -> bool:
            if len(row) == 1:
                return True

            def build(i: int, cur: List[str]) -> bool:
                if i == len(row) - 1:
                    return can("".join(cur))
                for t in tops.get(row[i:i + 2], ()):
                    cur.append(t)
                    if build(i + 1, cur):
                        return True
                    cur.pop()
                return False

            return build(0, [])

        return can(bottom)
