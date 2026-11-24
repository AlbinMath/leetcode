from bisect import bisect_left, insort
from typing import List

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        rooms.sort(key=lambda r: -r[1])
        order = sorted(range(len(queries)), key=lambda i: -queries[i][1])

        ids = []              # sorted room IDs with size >= current minSize
        ans = [-1] * len(queries)
        p = 0

        for qi in order:
            pref, min_size = queries[qi]

            while p < len(rooms) and rooms[p][1] >= min_size:
                insort(ids, rooms[p][0])
                p += 1

            if not ids:
                continue

            k = bisect_left(ids, pref)
            best = -1
            if k > 0:
                best = ids[k - 1]
            if k < len(ids):
                if best == -1 or ids[k] - pref < pref - best:
                    best = ids[k]
            ans[qi] = best

        return ans
