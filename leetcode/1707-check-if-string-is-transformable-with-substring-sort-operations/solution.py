from collections import deque

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = [deque() for _ in range(10)]
        for i, ch in enumerate(s):
            pos[int(ch)].append(i)

        for ch in t:
            d = int(ch)
            if not pos[d]:
                return False
            p = pos[d][0]
            for x in range(d):
                if pos[x] and pos[x][0] < p:
                    return False
            pos[d].popleft()

        return True
