class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        NEG = float('-inf')
        ans = NEG

        for a in "01234":
            for b in "01234":
                if a == b:
                    continue
                pa = [0] * (n + 1)
                pb = [0] * (n + 1)
                for i, ch in enumerate(s):
                    pa[i + 1] = pa[i] + (ch == a)
                    pb[i + 1] = pb[i] + (ch == b)

                INF = float('inf')
                best = [INF] * 4   # index = (pa%2)*2 + (pb%2) of left endpoint
                l = 0
                for r in range(k, n + 1):
                    while r - l >= k and pb[r] - pb[l] >= 2:
                        st = (pa[l] & 1) * 2 + (pb[l] & 1)
                        v = pa[l] - pb[l]
                        if v < best[st]:
                            best[st] = v
                        l += 1
                    need = ((pa[r] & 1) ^ 1) * 2 + (pb[r] & 1)
                    if best[need] != INF:
                        ans = max(ans, pa[r] - pb[r] - best[need])
        return ans
