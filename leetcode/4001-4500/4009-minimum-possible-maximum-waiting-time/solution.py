from typing import List

class Solution:
    def minMaxWaitingTime(self, demand: List[int], fuel: List[int]) -> int:
        F0, F1 = fuel
        cur = {(0, 0, 0): 0}
        pref = 0
        best = -1
        for p in demand:
            nxt = {}
            for (s0, d0, d1), mx in cur.items():
                s1 = pref - s0
                # dispenser 0
                if s0 + p <= F0:
                    key = (s0 + p, p, max(d1 - d0, 0))
                    val = max(mx, d0)
                    if key not in nxt or val < nxt[key]:
                        nxt[key] = val
                # dispenser 1
                if s1 + p <= F1:
                    key = (s0, max(d0 - d1, 0), p)
                    val = max(mx, d1)
                    if key not in nxt or val < nxt[key]:
                        nxt[key] = val
            if not nxt:
                break
            cur = nxt
            pref += p
            best = min(cur.values())
        return best
