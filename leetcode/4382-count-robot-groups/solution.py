from typing import List

class Solution:
    def countGroups(self, position: List[int], speed: List[int], distance: int) -> int:
        n = len(position)
        d = distance
        T = [None] * n          # (num, den) or None for infinity
        stack = []
        groups = 0

        for i in range(n - 1, -1, -1):
            p, s = position[i], speed[i]
            res = None
            while stack:
                j = stack[-1]
                g = position[j] - p
                if g <= d:
                    t = (0, 1)
                elif s > speed[j]:
                    t = (g - d, s - speed[j])
                else:
                    stack.pop()          # can never catch j
                    continue
                tj = T[j]
                if tj is None or t[0] * tj[1] <= tj[0] * t[1]:
                    res = t
                    break
                stack.pop()              # j is absorbed before i reaches it
            T[i] = res
            if res is None:
                groups += 1
            stack.append(i)

        return groups
