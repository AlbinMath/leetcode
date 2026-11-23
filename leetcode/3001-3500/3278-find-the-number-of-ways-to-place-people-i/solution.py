from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0
        for i in range(n):
            xa, ya = points[i]
            for j in range(n):
                if i == j:
                    continue
                xb, yb = points[j]
                if xa <= xb and ya >= yb:
                    ok = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        x, y = points[k]
                        if xa <= x <= xb and yb <= y <= ya:
                            ok = False
                            break
                    if ok:
                        count += 1
        return count
