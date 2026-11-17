class Solution(object):
    def substringXorQueries(self, s, queries):
        n = len(s)
        best = {}  # value -> (length, left, right)
        for i in range(n):
            if s[i] == '0':
                if 0 not in best or 1 < best[0][0]:
                    best[0] = (1, i, i)
                continue
            v = 0
            for j in range(i, min(n, i + 31)):
                v = (v << 1) | (s[j] == '1')
                L = j - i + 1
                if v not in best or L < best[v][0]:
                    best[v] = (L, i, j)

        res = []
        for a, b in queries:
            t = a ^ b
            if t in best:
                res.append([best[t][1], best[t][2]])
            else:
                res.append([-1, -1])
        return res
