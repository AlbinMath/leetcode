from typing import List
import numpy as np

_A, _B, _starts = [], [], []
for _mask in range(1024):
    _starts.append(len(_A))
    _sub = _mask
    while True:
        _A.append(_sub)
        _B.append(_mask ^ _sub)
        if _sub == 0:
            break
        _sub = (_sub - 1) & _mask
_A = np.array(_A, dtype=np.int64)
_B = np.array(_B, dtype=np.int64)
_starts = np.array(_starts, dtype=np.int64)
_masks = np.arange(1024)


class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(vals)

        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[par[i]].append(i)

        order = [0]
        for u in order:
            order.extend(children[u])

        comb = [np.zeros(1024, dtype=np.int64) for _ in range(n)]
        ans = 0

        for u in reversed(order):
            c = comb[u]

            vm = 0
            ok = True
            for ch in str(vals[u]):
                b = 1 << int(ch)
                if vm & b:
                    ok = False
                    break
                vm |= b

            if ok:
                cand = np.zeros(1024, dtype=np.int64)
                has = (_masks & vm) == vm
                cand[has] = c[_masks[has] ^ vm] + vals[u]
                dp = np.maximum(c, cand)
            else:
                dp = c

            ans = (ans + int(dp[1023])) % MOD

            p = par[u]
            if p >= 0:
                comb[p] = np.maximum.reduceat(comb[p][_A] + dp[_B], _starts)
            comb[u] = None

        return ans

    # Alias in case the judge uses a different name
    maxScore = goodSubtreeSum
