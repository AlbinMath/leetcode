from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7

        H = sorted(hFences + [1, m])
        V = sorted(vFences + [1, n])

        dh = {H[j] - H[i] for i in range(len(H)) for j in range(i + 1, len(H))}

        best = -1
        for i in range(len(V)):
            for j in range(i + 1, len(V)):
                d = V[j] - V[i]
                if d > best and d in dh:
                    best = d

        return -1 if best == -1 else best * best % MOD
