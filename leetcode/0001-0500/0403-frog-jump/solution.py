from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        jumps = {s: set() for s in stones}
        jumps[0].add(0)
        for s in stones:
            for k in jumps[s]:
                for nxt in (k - 1, k, k + 1):
                    if nxt > 0 and s + nxt in jumps:
                        jumps[s + nxt].add(nxt)
        return len(jumps[stones[-1]]) > 0
