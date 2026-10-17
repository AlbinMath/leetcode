from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        pos = defaultdict(list)
        for i, c in enumerate(ring):
            pos[c].append(i)

        # nxt[p] = min steps to spell key[i+1:] with ring position p at 12:00
        nxt = [0] * n
        for i in range(len(key) - 1, -1, -1):
            cur = [0] * n
            for p in range(n):
                best = float('inf')
                for q in pos[key[i]]:
                    d = abs(p - q)
                    d = min(d, n - d)
                    v = d + 1 + nxt[q]
                    if v < best:
                        best = v
                cur[p] = best
            nxt = cur
        return nxt[0]
